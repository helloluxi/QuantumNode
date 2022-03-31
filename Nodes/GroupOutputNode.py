import bpy
from bpy.types import Node
from ..commons import *

# Derived from the Node base type.
class GroupOutputNode(Node, LinearQuantumCircuitTreeNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'qnn_GroupOutput'
    # Label for nice name display
    bl_label = "Group Output"
    # Icon identifier
    bl_icon = 'PREV_KEYFRAME'

    def refresh(self, context):
        if len(self.inputs) > self.inputSize:
            while len(self.inputs) > self.inputSize:
                self.inputs.remove(self.inputs[-1])
        elif len(self.inputs) < self.inputSize:
            while len(self.inputs) < self.inputSize:
                self.inputs.new('qns_MultiQubits', getattr(self, f'input{len(self.inputs)+1}'))
        else:
            for i in range(len(self.inputs)):
                socket = self.inputs[i]
                if socket.name != getattr(self, f'input{i+1}') or socket.bl_idname != ('qns_SingleQubit' if i < self.boolInputSize else 'qns_MultiQubits'):
                    from_sockets = [link.from_socket for link in socket.links]
                    self.inputs.remove(socket)
                    self.inputs.new('qns_SingleQubit' if i < self.boolInputSize else 'qns_MultiQubits', getattr(self, f'input{i+1}'))
                    self.inputs.move(self.inputSize - 1, i)
                    socket = self.inputs[i]
                    for from_socket in from_sockets:
                        self.id_data.links.new(from_socket, socket)

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    inputSize: bpy.props.IntProperty(default=1, min=1, max=8, update=refresh)
    boolInputSize: bpy.props.IntProperty(default=0, min=0, max=8, update=refresh)
    input1: bpy.props.StringProperty(default='input1', update=refresh)
    input2: bpy.props.StringProperty(default='input2', update=refresh)
    input3: bpy.props.StringProperty(default='input3', update=refresh)
    input4: bpy.props.StringProperty(default='input4', update=refresh)
    input5: bpy.props.StringProperty(default='input5', update=refresh)
    input6: bpy.props.StringProperty(default='input6', update=refresh)
    input7: bpy.props.StringProperty(default='input7', update=refresh)
    input8: bpy.props.StringProperty(default='input8', update=refresh)


    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        for i in range(self.inputSize):
            self.inputs.new('qns_SingleQubit' if i < self.boolInputSize else 'qns_MultiQubits', getattr(self, f'input{i+1}'))

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
        layout.prop(self, 'inputSize')
        layout.prop(self, 'boolInputSize')
        for i in range(8):
            layout.prop(self, f'input{i+1}')

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Group Output"
