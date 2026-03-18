import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio ULTRA PRO",
    "author": "Tutorisreal",
    "version": (5, 0),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI ULTRA PRO",
    "description": "Enterprise SGI rendering. Fixed selection for Rigs and SNES 32px mode.",
    "category": "Render",
}

def register():
    operators.register()
    ui.register()

def unregister():
    ui.unregister()
    operators.unregister()

if __name__ == "__main__":
    register()
