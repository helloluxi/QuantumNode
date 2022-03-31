import bpy
from bpy.types import NodeSocket

class SingleQubit(NodeSocket):
    bl_idname = 'qns_SingleQubit'
    bl_label = "Single Qubit"

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.0, 214/255, 163/255, 1.0)
