import bpy
from bpy.types import Node
from ..commons import *

# Derived from the Node base type.
class SuperpositionInputNode(Node, LinearQuantumCircuitTreeNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'qnn_SuperpositionInput'
    # Label for nice name display
    bl_label = "Superposition Input"
    # Icon identifier
    bl_icon = 'HOME'

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    
    

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.outputs.new('qns_MultiQubits', "Superposition Input")

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
        pass

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "Superposition Input"