import bpy
from bpy.types import NodeSocket

class ClassicalBits(NodeSocket):
    bl_idname = 'qns_ClassicalBits'
    bl_label = "Classical Bits"

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (199/255, 199/255, 41/255, 1.0)
