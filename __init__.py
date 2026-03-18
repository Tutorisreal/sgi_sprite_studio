import bpy
from . import operators
from . import ui

bl_info = {
    "name": "Ultimate SGI Sprite Studio MAX PRO",
    "author": "Tutorisreal",
    "version": (4, 0),
    "blender": (2, 93, 0),
    "location": "Top Bar > Render > SGI MAX PRO",
    "description": "Enterprise-grade SGI rendering. 16-Dir support, Auto-Lighting, and Smart Selection.",
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
