import bpy
from bpy.types import NodeTree, NodeCustomGroup
from mathutils import Vector

# Derived from the NodeTree base type, similar to Menu, Operator, Panel, etc.
class LinearQuantumCircuitTree(NodeTree):
    # Description string
    '''A custom node tree type that will show up in the editor type list'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'LinearQuantumNode'
    # Label for nice name display
    bl_label = "Linear Quantum Circuit Node"
    # Icon identifier
    bl_icon = 'RNA'


# Mix-in class for all custom nodes in this tree type.
# Defines a poll function to enable instantiation.
class LinearQuantumCircuitTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'LinearQuantumNode'


### Node Categories ###
# Node categories are a python system for automatically
# extending the Add menu, toolbar panels and search operator.
# For more examples see release/scripts/startup/nodeitems_builtins.py
from nodeitems_utils import NodeCategory

# our own base class with an appropriate poll function,
# so the categories only show up in our own tree type
class LinearQuantumCircuitNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'LinearQuantumNode'
