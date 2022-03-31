import bpy
from bpy.types import NodeSocket

class MultiQubits(NodeSocket):
    bl_idname = 'qns_MultiQubits'
    bl_label = "Multi Qubits"

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (99/255, 99/255, 199/255, 1.0)
