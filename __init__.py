# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "LinearQuantumCircuit",
    "author" : "Xi Lu",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Nodes"
}

import bpy

from .commons import *
from nodeitems_utils import NodeItem

from .Nodes.SuperpositionInputNode import SuperpositionInputNode
from .Nodes.SuperpositionOutputNode import SuperpositionOutputNode
from .Nodes.ClassicalInputNode import ClassicalInputNode
from .Nodes.GarbageNode import GarbageNode
from .Nodes.ArbitraryNode import ArbitraryNode
from .Nodes.FunctionNode import FunctionNode
from .Nodes.GroupInputNode import GroupInputNode
from .Nodes.GroupOutputNode import GroupOutputNode
from .Nodes.StructPackNode import StructPackNode
from .Nodes.StructUnpackNode import StructUnpackNode

from .Sockets.SingleQubit import SingleQubit
from .Sockets.MultiQubits import MultiQubits
from .Sockets.ClassicalBits import ClassicalBits

# all categories in a list
node_categories = [
    # identifier, label, items list
    LinearQuantumCircuitNodeCategory('qnAdd_IO', "IO", items=[
        NodeItem("qnn_SuperpositionInput"),
        NodeItem("qnn_ClassicalInput"),
        NodeItem("qnn_Output"),
        NodeItem("qnn_Garbage"),
    ]),
    LinearQuantumCircuitNodeCategory('qnAdd_GeneralFunction', "General Function", items=[
        NodeItem("qnn_Function"),
        NodeItem("qnn_Arbitrary"),
        NodeItem("qnn_StructPack"),
        NodeItem("qnn_StructUnpack"),
    ]),
    LinearQuantumCircuitNodeCategory('qnAdd_Function', "Special Function", items=[
        NodeItem("qnn_Function", label="Copy", settings={
            "input1": repr('a'),
            "output1": repr('a'),
            "label": repr('Copy')
        }),
        NodeItem("qnn_Function", label="Add", settings={
            "inputSize": repr(2),
            "input1": repr('a'),
            "input2": repr('b'),
            "output1": repr('a+b'),
            "label": repr('Add')
        }),
        NodeItem("qnn_Function", label="Multiply", settings={
            "inputSize": repr(2),
            "input1": repr('a'),
            "input2": repr('b'),
            "output1": repr('a*b'),
            "label": repr('Multiply')
        }),
        NodeItem("qnn_Function", label="Compare", settings={
            "inputSize": repr(2),
            "boolOutputSize": repr(1),
            "input1": repr('a'),
            "input2": repr('b'),
            "output1": repr('a>b'),
            "label": repr('Compare')
        }),
        NodeItem("qnn_Function", label="CompareE", settings={
            "inputSize": repr(2),
            "boolOutputSize": repr(1),
            "input1": repr('a'),
            "input2": repr('b'),
            "output1": repr('a>=b'),
            "label": repr('CompareE')
        }),
        NodeItem("qnn_Function", label="Logic And", settings={
            "boolInputSize": repr(1),
            "boolOutputSize": repr(1),
            "ctrl": repr('a'),
            "input1": repr('b'),
            "output1": repr('a&b'),
            "label": repr('Logic And')
        }),
        NodeItem("qnn_Function", label="Logic Or", settings={
            "boolInputSize": repr(1),
            "boolOutputSize": repr(1),
            "ctrl": repr('a'),
            "input1": repr('b'),
            "output1": repr('a|b'),
            "label": repr('Logic Or')
        }),
        NodeItem("qnn_Function", label="Logic Xor", settings={
            "boolInputSize": repr(1),
            "boolOutputSize": repr(1),
            "ctrl": repr('a'),
            "input1": repr('b'),
            "output1": repr('a^b'),
            "label": repr('Logic Xor')
        }),
        NodeItem("qnn_Function", label="Select", settings={
            "inputSize": repr(2),
            "outputSize": repr(1),
            "input1": repr('True expression'),
            "input2": repr('False expression'),
            "output1": repr('result'),
            "label": repr('Select')
        }),
        NodeItem("qnn_Function", label="Nothing", settings={
            "inputSize": repr(1),
            "outputSize": repr(0),
            "label": repr('Nothing')
        }),
    ]),
    LinearQuantumCircuitNodeCategory('qnAdd_ElementaryGates', "Elementary Operations", items=[
        NodeItem("qnn_Arbitrary", label="X", settings={
            "boolInputSize": repr(1),
            "boolOutputSize": repr(1),
            "input1": repr('a'),
            "output1": repr('!a'),
            "label": repr('X')
        }),
        NodeItem("qnn_Arbitrary", label="CNOT", settings={
            "inputSize": repr(2),
            "outputSize": repr(2),
            "boolInputSize": repr(2),
            "boolOutputSize": repr(2),
            "input1": repr('ctrl'),
            "input2": repr('targ'),
            "output1": repr('ctrl'),
            "output2": repr('targ'),
            "label": repr('CNOT')
        }),
        NodeItem("qnn_Arbitrary", label="CCNOT", settings={
            "inputSize": repr(3),
            "outputSize": repr(3),
            "boolInputSize": repr(3),
            "boolOutputSize": repr(3),
            "input1": repr('ctrl1'),
            "input2": repr('ctrl2'),
            "input3": repr('targ'),
            "output1": repr('ctrl1'),
            "output2": repr('ctrl2'),
            "output3": repr('targ'),
            "label": repr('CCNOT')
        }),
        NodeItem("qnn_Arbitrary", label="X (sync)", settings={
            "boolInputSize": repr(0),
            "boolOutputSize": repr(0),
            "input1": repr('qubit'),
            "label": repr('X')
        }),
        NodeItem("qnn_Function", label="CNOT (sync)", settings={
            "outputSize": repr(0),
            "boolInputSize": repr(1),
            "input1": repr('targ'),
            "label": repr('CNOT')
        }),
        NodeItem("qnn_Function", label="CCNOT (sync)", settings={
            "inputSize": repr(2),
            "outputSize": repr(0),
            "boolInputSize": repr(2),
            "input1": repr('ctrl'),
            "input2": repr('targ'),
            "label": repr('CCNOT')
        }),
    ]),
    LinearQuantumCircuitNodeCategory('qnAdd_Group', "Group", items=[
        NodeItem("qnn_GroupInput"),
        NodeItem("qnn_GroupOutput"),
    ]),
]

classes = (
    LinearQuantumCircuitTree,
)

socket_classes = (
    SingleQubit,
    MultiQubits,
    ClassicalBits,
)

node_classes = (
    SuperpositionInputNode,
    SuperpositionOutputNode,
    ClassicalInputNode,
    GarbageNode,
    FunctionNode,
    ArbitraryNode,
    GroupInputNode,
    GroupOutputNode,
    StructPackNode,
    StructUnpackNode,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    for cls in socket_classes:
        register_class(cls)
    for cls in node_classes:
        register_class(cls)
    from nodeitems_utils import register_node_categories
    register_node_categories('CUSTOM_NODES', node_categories)

def unregister():
    from nodeitems_utils import unregister_node_categories
    unregister_node_categories('CUSTOM_NODES')
    from bpy.utils import unregister_class
    for cls in node_classes:
        unregister_class(cls)
    for cls in socket_classes:
        unregister_class(cls)
    for cls in reversed(classes):
        unregister_class(cls)
