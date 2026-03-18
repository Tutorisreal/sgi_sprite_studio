import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio PRO",
    "author": "Tutorisreal",
    "version": (3, 1),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI Sprite Studio",
    "description": "Pro SGI pre-rendering. Improved selection logic for SNES and HD modes.",
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
