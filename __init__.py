import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio",
    "author": "Tutorisreal",
    "version": (2, 0),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI Sprite Studio",
    "description": "Professional SGI-style pre-rendering with major 8-directional and animation updates.",
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
