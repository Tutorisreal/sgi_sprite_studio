import bpy

class RENDER_MT_sgi_ultimate_menu(bpy.types.Menu):
    """The menu that appears in the Top Bar > Render."""
    bl_label = "SGI Sprite Studio"
    bl_idname = "RENDER_MT_sgi_ultimate_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='WORLD_DATA', text="1. Setup SGI Studio")
        layout.separator()
        
        col = layout.column()
        col.label(text="High-Res SGI (512px)")
        op1 = col.operator("render.sgi_action", text="Render Still", icon='RENDER_STILL')
        op1.mode = "STILL"; op1.pixel = False
        op2 = col.operator("render.sgi_action", text="8-Dir Batch", icon='IMAGE_DATA')
        op2.mode = "BATCH"; op2.pixel = False
        op3 = col.operator("render.sgi_action", text="8-Dir Animation", icon='RENDER_ANIMATION')
        op3.mode = "ANIM"; op3.pixel = False

        layout.separator()
        col = layout.column()
        col.label(text="Retro Pixel SGI (64px)")
        op4 = col.operator("render.sgi_action", text="Pixel Still", icon='TEXTURE')
        op4.mode = "STILL"; op4.pixel = True
        op5 = col.operator("render.sgi_action", text="Pixel 8-Dir Animation", icon='PLAY')
        op5.mode = "ANIM"; op5.pixel = True

def draw_top_bar(self, context):
    self.layout.menu("RENDER_MT_sgi_ultimate_menu", icon='RENDER_STILL')

def register():
    bpy.utils.register_class(RENDER_MT_sgi_ultimate_menu)
    bpy.types.TOPBAR_MT_render.append(draw_top_bar)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_top_bar)
    bpy.utils.unregister_class(RENDER_MT_sgi_ultimate_menu)
