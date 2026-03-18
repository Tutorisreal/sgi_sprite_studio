import bpy

class RENDER_MT_sgi_ultimate_menu(bpy.types.Menu):
    """MAX PRO UI Layout."""
    bl_label = "SGI Studio MAX PRO"
    bl_idname = "RENDER_MT_sgi_ultimate_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='OUTLINER_OB_LIGHT', text="1. Build Studio Rig (Lights/Floor)")
        layout.separator()
        
        # HANDHELD TIER
        box = layout.box()
        box.label(text="Handheld Tier (16px / 32px)", icon='MOD_PIXELATE')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="SNES 32px Still")
        op.mode = "STILL"; op.res = 32
        op = row.operator("render.sgi_action", text="SNES 4-Dir")
        op.mode = "ANIM_MULTI"; op.res = 32; op.dirs = 4
        op = row.operator("render.sgi_action", text="SNES 8-Dir")
        op.mode = "ANIM_MULTI"; op.res = 32; op.dirs = 8

        # CONSOLE TIER
        layout.separator()
        box = layout.box()
        box.label(text="Console Tier (64px / 128px)", icon='CONSOLE')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="PS1 64px Still")
        op.mode = "STILL"; op.res = 64
        op = row.operator("render.sgi_action", text="PS1 8-Dir")
        op.mode = "ANIM_MULTI"; op.res = 64; op.dirs = 8
        op = row.operator("render.sgi_action", text="PS1 16-Dir")
        op.mode = "ANIM_MULTI"; op.res = 64; op.dirs = 16

        # HD TIER
        layout.separator()
        box = layout.box()
        box.label(text="High-Definition SGI", icon='RENDER_STILL')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="256px HD Still")
        op.mode = "STILL"; op.res = 256
        op = row.operator("render.sgi_action", text="256px 8-Dir")
        op.mode = "ANIM_MULTI"; op.res = 256; op.dirs = 8
        op = row.operator("render.sgi_action", text="256px 16-Dir")
        op.mode = "ANIM_MULTI"; op.res = 256; op.dirs = 16

        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="512px Ultra Still")
        op.mode = "STILL"; op.res = 512
        op = row.operator("render.sgi_action", text="512px 8-Dir")
        op.mode = "ANIM_MULTI"; op.res = 512; op.dirs = 8

def draw_top_bar(self, context):
    self.layout.menu("RENDER_MT_sgi_ultimate_menu", icon='SOLO_ON')

def register():
    bpy.utils.register_class(RENDER_MT_sgi_ultimate_menu)
    bpy.types.TOPBAR_MT_render.append(draw_top_bar)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_top_bar)
    bpy.utils.unregister_class(RENDER_MT_sgi_ultimate_menu)
