import bpy

class RENDER_MT_sgi_ultimate_menu(bpy.types.Menu):
    """Pro UI Layout with SNES and HD categories."""
    bl_label = "SGI Sprite Studio PRO"
    bl_idname = "RENDER_MT_sgi_ultimate_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='WORLD_DATA', text="1. Initialize Studio")
        layout.separator()
        
        # SNES / PIXEL SECTION
        box = layout.box()
        box.label(text="Retro (32px / 64px)", icon='STRANDS')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="SNES Still (32px)")
        op.mode = "STILL"; op.res = 32
        op = row.operator("render.sgi_action", text="SNES 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 32

        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="Pixel Still (64px)")
        op.mode = "STILL"; op.res = 64
        op = row.operator("render.sgi_action", text="Pixel 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 64

        layout.separator()

        # HD SECTION
        box = layout.box()
        box.label(text="High-Definition SGI", icon='RENDER_STILL')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="256px HD Still")
        op.mode = "STILL"; op.res = 256
        op = row.operator("render.sgi_action", text="256px 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 256

        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="512px Ultra Still")
        op.mode = "STILL"; op.res = 512
        op = row.operator("render.sgi_action", text="512px 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 512

def draw_top_bar(self, context):
    self.layout.menu("RENDER_MT_sgi_ultimate_menu", icon='SOLO_ON')

def register():
    bpy.utils.register_class(RENDER_MT_sgi_ultimate_menu)
    bpy.types.TOPBAR_MT_render.append(draw_top_bar)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_top_bar)
    bpy.utils.unregister_class(RENDER_MT_sgi_ultimate_menu)
