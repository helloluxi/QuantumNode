import bpy
from bpy.types import Node
from ..commons import *

# Derived from the Node base type.
class StructUnpackNode(Node, LinearQuantumCircuitTreeNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'qnn_StructUnpack'
    # Label for nice name display
    bl_label = "Struct Unpack"
    # Icon identifier
    bl_icon = 'STICKY_UVS_DISABLE'

    def refresh(self, context):
        if len(self.outputs) > self.outputSize:
            while len(self.outputs) > self.outputSize:
                self.outputs.remove(self.outputs[-1])
        elif len(self.outputs) < self.outputSize:
            while len(self.outputs) < self.outputSize:
                self.outputs.new('qns_MultiQubits', getattr(self, f'output{len(self.outputs)+1}'))
        else:
            for i in range(len(self.outputs)):
                socket = self.outputs[i]
                if socket.name != getattr(self, f'output{i+1}') or socket.bl_idname != ('qns_SingleQubit' if i < self.boolOutputSize else 'qns_MultiQubits'):
                    to_sockets = [link.to_socket for link in socket.links]
                    self.outputs.remove(socket)
                    self.outputs.new('qns_SingleQubit' if i < self.boolOutputSize else 'qns_MultiQubits', getattr(self, f'output{i+1}'))
                    self.outputs.move(self.outputSize - 1, i)
                    socket = self.outputs[i]
                    for to_socket in to_sockets:
                        self.id_data.links.new(socket, to_socket)
            if self.inputs[0].name != self.structName:
                from_sockets = [link.from_socket for link in self.inputs[0].links]
                self.inputs.clear()
                self.inputs.new(socket.bl_idname, self.structName)
                for from_socket in from_sockets:
                    self.id_data.links.new(from_socket, self.inputs[0])

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    outputSize: bpy.props.IntProperty(default=1, min=1, max=8, update=refresh)
    boolOutputSize: bpy.props.IntProperty(default=0, min=0, max=8, update=refresh)
    structName: bpy.props.StringProperty(default='struct', update=refresh)
    output1: bpy.props.StringProperty(default='output1', update=refresh)
    output2: bpy.props.StringProperty(default='output2', update=refresh)
    output3: bpy.props.StringProperty(default='output3', update=refresh)
    output4: bpy.props.StringProperty(default='output4', update=refresh)
    output5: bpy.props.StringProperty(default='output5', update=refresh)
    output6: bpy.props.StringProperty(default='output6', update=refresh)
    output7: bpy.props.StringProperty(default='output7', update=refresh)
    output8: bpy.props.StringProperty(default='output8', update=refresh)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        for i in range(self.outputSize):
            self.outputs.new('qns_SingleQubit' if i < self.boolOutputSize else 'qns_MultiQubits', getattr(self, f'output{i+1}'))
        self.inputs.new('qns_MultiQubits', self.structName)

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        pass

    # Free function to clean up on removal.
    def free(self):
        pass

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        pass

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
        layout.prop(self, 'outputSize')
        layout.prop(self, 'boolOutputSize')
        layout.prop(self, 'structName')
        for i in range(8):
            layout.prop(self, f'output{i+1}')

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Struct Unpack"