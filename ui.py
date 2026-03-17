import bpy

class RENDER_MT_sgi_ultimate_menu(bpy.types.Menu):
    """v2.0 Top Bar Menu Interface."""
    bl_label = "SGI Sprite Studio"
    bl_idname = "RENDER_MT_sgi_ultimate_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='WORLD_DATA', text="1. Setup SGI Studio")
        layout.separator()
        
        # High-Res Section
        col = layout.column()
        col.label(text="High-Res SGI (512px)")
        op1 = col.operator("render.sgi_action", text="Render Still", icon='RENDER_STILL')
        op1.mode = "STILL"; op1.pixel = False
        
        op_anim1 = col.operator("render.sgi_action", text="Render Animation", icon='RENDER_ANIMATION')
        op_anim1.mode = "SINGLE_ANIM"; op_anim1.pixel = False
        
        op2 = col.operator("render.sgi_action", text="8-Dir Batch", icon='IMAGE_DATA')
        op2.mode = "BATCH"; op2.pixel = False
        
        op3 = col.operator("render.sgi_action", text="8-Dir Animation", icon='RENDER_ANIMATION')
        op3.mode = "ANIM_8DIR"; op3.pixel = False

        layout.separator()
        
        # Retro Pixel Section
        col = layout.column()
        col.label(text="Retro Pixel SGI (64px)")
        op4 = col.operator("render.sgi_action", text="Pixel Still", icon='TEXTURE')
        op4.mode = "STILL"; op4.pixel = True
        
        op_anim2 = col.operator("render.sgi_action", text="Pixel Render Animation", icon='RENDER_ANIMATION')
        op_anim2.mode = "SINGLE_ANIM"; op_anim2.pixel = True
        
        op5 = col.operator("render.sgi_action", text="Pixel 8-Dir Batch", icon='FILE_IMAGE')
        op5.mode = "BATCH"; op5.pixel = True
        
        op6 = col.operator("render.sgi_action", text="Pixel 8-Dir Animation", icon='PLAY')
        op6.mode = "ANIM_8DIR"; op6.pixel = True

def draw_top_bar(self, context):
    self.layout.menu("RENDER_MT_sgi_ultimate_menu", icon='RENDER_STILL')

def register():
    bpy.utils.register_class(RENDER_MT_sgi_ultimate_menu)
    bpy.types.TOPBAR_MT_render.append(draw_top_bar)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_top_bar)
    bpy.utils.unregister_class(RENDER_MT_sgi_ultimate_menu)
