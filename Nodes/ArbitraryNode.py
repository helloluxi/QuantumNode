import bpy
from bpy.types import Node
from ..commons import *

# Derived from the Node base type.
class ArbitraryNode(Node, LinearQuantumCircuitTreeNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'qnn_Arbitrary'
    # Label for nice name display
    bl_label = "Arbitrary"
    # Icon identifier
    bl_icon = 'RNA'

    def getInputName(self, idx):
        return getattr(self, f'input{idx+1}')

    def getOutputName(self, idx):
        return getattr(self, f'output{idx+1}')

    def getInputIdName(self, idx):
        return 'qns_SingleQubit' if idx < self.boolInputSize else 'qns_MultiQubits'

    def getOutputIdName(self, idx):
        return 'qns_SingleQubit' if idx < self.boolOutputSize else 'qns_MultiQubits'

    def refresh(self, context):
        if len(self.inputs) > self.inputSize:
            while len(self.inputs) > self.inputSize:
                self.inputs.remove(self.inputs[-1])
        elif len(self.inputs) < self.inputSize:
            while len(self.inputs) < self.inputSize:
                self.inputs.new(self.getInputIdName(len(self.inputs)), self.getInputName(len(self.inputs)))
        elif len(self.outputs) > self.outputSize:
            while len(self.outputs) > self.outputSize:
                self.outputs.remove(self.outputs[-1])
        elif len(self.outputs) < self.outputSize:
            while len(self.outputs) < self.outputSize:
                self.outputs.new(self.getOutputIdName(len(self.outputs)), self.getOutputName(len(self.outputs)))
        else:
            for i in range(len(self.inputs)):
                socket = self.inputs[i]
                if socket.name != self.getInputName(i) or socket.bl_idname != self.getInputIdName(i):
                    from_sockets = [link.from_socket for link in socket.links]
                    self.inputs.remove(socket)
                    self.inputs.new(self.getInputIdName(i), self.getInputName(i))
                    self.inputs.move(self.inputSize - 1, i)
                    socket = self.inputs[i]
                    for from_socket in from_sockets:
                        self.id_data.links.new(from_socket, socket)
            for i in range(len(self.outputs)):
                socket = self.outputs[i]
                if socket.name != self.getOutputName(i) or socket.bl_idname != self.getOutputIdName(i):
                    to_sockets = [link.to_socket for link in socket.links]
                    self.outputs.remove(socket)
                    self.outputs.new(self.getOutputIdName(i), self.getOutputName(i))
                    self.outputs.move(self.outputSize - 1, i)
                    socket = self.outputs[i]
                    for to_socket in to_sockets:
                        self.id_data.links.new(socket, to_socket)

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties

    inputSize: bpy.props.IntProperty(default=1, min=1, max=8, update=refresh)
    outputSize: bpy.props.IntProperty(default=1, min=0, max=8, update=refresh)
    boolInputSize: bpy.props.IntProperty(default=0, min=0, max=8, update=refresh)
    boolOutputSize: bpy.props.IntProperty(default=0, min=0, max=8, update=refresh)
    input1: bpy.props.StringProperty(default='input1', update=refresh)
    input2: bpy.props.StringProperty(default='input2', update=refresh)
    input3: bpy.props.StringProperty(default='input3', update=refresh)
    input4: bpy.props.StringProperty(default='input4', update=refresh)
    input5: bpy.props.StringProperty(default='input5', update=refresh)
    input6: bpy.props.StringProperty(default='input6', update=refresh)
    input7: bpy.props.StringProperty(default='input7', update=refresh)
    input8: bpy.props.StringProperty(default='input8', update=refresh)
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
        for i in range(self.inputSize):
            self.inputs.new('qns_MultiQubits' if i >= self.boolInputSize else 'qns_SingleQubit', getattr(self, f'input{i+1}'))
        for i in range(self.outputSize):
            self.outputs.new('qns_MultiQubits' if i >= self.boolOutputSize else 'qns_SingleQubit', getattr(self, f'output{i+1}'))

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        pass

    # Detail buttons in the sidebar.
    # If this function is not defined, the draw_buttons function is used instead
    def draw_buttons_ext(self, context, layout):
        layout.prop(self, 'inputSize')
        layout.prop(self, 'outputSize')
        layout.prop(self, 'boolInputSize')
        layout.prop(self, 'boolOutputSize')
        for i in range(8):
            layout.prop(self, f'input{i+1}')
        for i in range(8):
            layout.prop(self, f'output{i+1}')

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Arbitrary"
