import bpy
import os
import math

def setup_sgi_render(scene, res=512):
    """Technical SGI parameters. Cycles is forced for Shadow Catcher support."""
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.engine = 'CYCLES'
    
    scene.render.resolution_x, scene.render.resolution_y = res, res
    
    # Adaptive Anti-Aliasing (Sharper for low-res sprites)
    scene.render.filter_size = 0.01 if res <= 64 else 1.5

class RENDER_OT_sgi_setup(bpy.types.Operator):
    """Initializes the SGI environment without forcing a camera."""
    bl_idname = "render.sgi_setup"
    bl_label = "Prepare SGI Studio"

    def execute(self, context):
        setup_sgi_render(context.scene)
        if "SGI_Shadow_Floor" not in bpy.data.objects:
            bpy.ops.mesh.primitive_plane_add(size=25)
            plane = bpy.context.active_object
            plane.name = "SGI_Shadow_Floor"
            plane.cycles.is_shadow_catcher = True
        
        self.report({'INFO'}, "SGI Pro Studio Ready")
        return {'FINISHED'}

class RENDER_OT_sgi_action(bpy.types.Operator):
    """Handles multi-object batch rendering and animations."""
    bl_idname = "render.sgi_action"
    bl_label = "SGI Render"
    mode: bpy.props.StringProperty()
    res: bpy.props.IntProperty(default=512)

    def execute(self, context):
        scene = context.scene
        # Broadened filter: Includes anything selected except the shadow floor
        targets = [obj for obj in context.selected_objects if obj.name != "SGI_Shadow_Floor"]
        
        if not scene.camera:
            self.report({'ERROR'}, "No active camera! Please add one manually.")
            return {'CANCELLED'}
        if not targets:
            self.report({'ERROR'}, "Nothing selected! Select your character in the viewport.")
            return {'CANCELLED'}

        setup_sgi_render(scene, res=self.res)
        base_path = os.path.join(os.path.expanduser('~'), 'Desktop', "SGI_PRO_OUTPUT")

        for obj in targets:
            obj_dir = os.path.join(base_path, obj.name, f"Res_{self.res}")
            if not os.path.exists(obj_dir): os.makedirs(obj_dir)

            orig_rot = obj.rotation_euler[2]

            if self.mode == "STILL":
                scene.render.filepath = os.path.join(obj_dir, f"{obj.name}_still.png")
                bpy.ops.render.render(write_still=True)
                
            elif self.mode == "ANIM_8DIR":
                for d in range(8):
                    obj.rotation_euler[2] = math.radians(d * 45)
                    dir_path = os.path.join(obj_dir, f"Dir_{d}")
                    if not os.path.exists(dir_path): os.makedirs(dir_path)
                    
                    for f in range(scene.frame_start, scene.frame_end + 1):
                        scene.frame_set(f)
                        scene.render.filepath = os.path.join(dir_path, f"f_{f:03d}.png")
                        bpy.ops.render.render(write_still=True)

            obj.rotation_euler[2] = orig_rot

        self.report({'INFO'}, f"Batch Complete: {base_path}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RENDER_OT_sgi_setup)
    bpy.utils.register_class(RENDER_OT_sgi_action)

def unregister():
    bpy.utils.unregister_class(RENDER_OT_sgi_setup)
    bpy.utils.unregister_class(RENDER_OT_sgi_action)
