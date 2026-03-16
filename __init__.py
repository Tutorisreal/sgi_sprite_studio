import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio",
    "author": "Tutorisreal",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI Sprite Studio",
    "description": "Professional SGI-style pre-rendering with Sheet Joining and Animation.",
    "category": "Render",
}

def register():
    # Register the logic first
    operators.register()
    # Then register the UI menu
    ui.register()

def unregister():
    # Unregister in reverse order
    ui.unregister()
    operators.unregister()

if __name__ == "__main__":
    register()
