import bpy

class RENDER_MT_sgi_ultra_menu(bpy.types.Menu):
    bl_label = "SGI ULTRA PRO"
    bl_idname = "RENDER_MT_sgi_ultra_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='WORLD_DATA', text="1. Build Ultra Studio")
        layout.separator()
        
        # SNES SECTION
        box = layout.box()
        box.label(text="Retro Production (32px)", icon='STRANDS')
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="32px 8-Dir")
        op.mode = "ANIM"; op.res = 32; op.dirs = 8
        op = row.operator("render.sgi_action", text="32px 16-Dir")
        op.mode = "ANIM"; op.res = 32; op.dirs = 16

        # HD SECTION
        layout.separator()
        box = layout.box()
        box.label(text="HD Production (512px)", icon='RENDER_STILL')
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="512px 8-Dir")
        op.mode = "ANIM"; op.res = 512; op.dirs = 8
        op = row.operator("render.sgi_action", text="512px 16-Dir")
        op.mode = "ANIM"; op.res = 512; op.dirs = 16

def draw_top_bar(self, context):
    self.layout.menu("RENDER_MT_sgi_ultra_menu", icon='SOLO_ON')

def register():
    bpy.utils.register_class(RENDER_MT_sgi_ultra_menu)
    bpy.types.TOPBAR_MT_render.append(draw_top_bar)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_top_bar)
    bpy.utils.unregister_class(RENDER_MT_sgi_ultra_menu)
