import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio",
    "author": "Tutorisreal",
    "version": (1, 1),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI Sprite Studio",
    "description": "Professional SGI-style pre-rendering with Sheet Joining and Animation.",
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
