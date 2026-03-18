import bpy

class RENDER_MT_sgi_ultimate_menu(bpy.types.Menu):
    """Pro UI Layout with SNES and HD categories."""
    bl_label = "SGI Sprite Studio PRO"
    bl_idname = "RENDER_MT_sgi_ultimate_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.sgi_setup", icon='WORLD_DATA', text="Initialize Studio")
        layout.separator()
        
        # RETRO / SNES SECTION
        box = layout.box()
        box.label(text="Retro / Handheld", icon='STRANDS')
        
        # 32x32 SNES
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="32px SNES Still")
        op.mode = "STILL"; op.res = 32
        op = row.operator("render.sgi_action", text="32px SNES 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 32

        # 64x64 Classic
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="64px Still")
        op.mode = "STILL"; op.res = 64
        op = row.operator("render.sgi_action", text="64px 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 64

        layout.separator()

        # HIGH-RES SECTION
        box = layout.box()
        box.label(text="High-Definition SGI", icon='RENDER_STILL')
        
        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="256px HD")
        op.mode = "STILL"; op.res = 256
        op = row.operator("render.sgi_action", text="256px 8-Dir")
        op.mode = "ANIM_8DIR"; op.res = 256

        row = box.row(align=True)
        op = row.operator("render.sgi_action", text="512px Ultra")
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
