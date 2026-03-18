import bpy
import os
import math

def setup_sgi_render(scene, res=32):
    """Pro-grade render settings for Windows 8.1/Blender 2.93."""
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.engine = 'CYCLES'
    scene.render.resolution_x, scene.render.resolution_y = res, res
    
    # Ultra-sharp filter for 32x32 (SNES style)
    scene.render.filter_size = 0.01 if res <= 64 else 1.5

class RENDER_OT_sgi_setup(bpy.types.Operator):
    bl_idname = "render.sgi_setup"
    bl_label = "Initialize Studio"

    def execute(self, context):
        setup_sgi_render(context.scene)
        # Ensure we are in Object Mode
        if context.active_object and context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
            
        if "SGI_Shadow_Floor" not in bpy.data.objects:
            bpy.ops.mesh.primitive_plane_add(size=30)
            floor = bpy.context.active_object
            floor.name = "SGI_Shadow_Floor"
            floor.cycles.is_shadow_catcher = True
        
        self.report({'INFO'}, "ULTRA PRO Studio Ready.")
        return {'FINISHED'}

class RENDER_OT_sgi_action(bpy.types.Operator):
    bl_idname = "render.sgi_action"
    bl_label = "SGI Render"
    mode: bpy.props.StringProperty()
    res: bpy.props.IntProperty(default=32)
    dirs: bpy.props.IntProperty(default=8)

    def execute(self, context):
        scene = context.scene
        # Target anything selected that isn't the floor or lights
        targets = [obj for obj in context.selected_objects if not obj.name.startswith("SGI_")]
        
        if not targets and context.active_object:
            targets = [context.active_object]

        if not targets:
            self.report({'ERROR'}, "Nothing selected! Click your Rig or Character.")
            return {'CANCELLED'}
        
        if not scene.camera:
            self.report({'ERROR'}, "No active camera found!")
            return {'CANCELLED'}

        setup_sgi_render(scene, res=self.res)
        # Dynamic path for Windows 8.1 Desktop
        base_path = os.path.join(os.path.expanduser('~'), 'Desktop', "SGI_ULTRA_OUTPUT")

        for obj in targets:
            obj_dir = os.path.join(base_path, obj.name, f"Res_{self.res}")
            if not os.path.exists(obj_dir): os.makedirs(obj_dir)

            orig_rot = obj.rotation_euler[2]
            angle_step = 360.0 / self.dirs

            for d in range(self.dirs):
                obj.rotation_euler[2] = math.radians(d * angle_step)
                dir_path = os.path.join(obj_dir, f"Dir_{d:02d}")
                if not os.path.exists(dir_path): os.makedirs(dir_path)
                
                for f in range(scene.frame_start, scene.frame_end + 1):
                    scene.frame_set(f)
                    scene.render.filepath = os.path.join(dir_path, f"f_{f:03d}.png")
                    bpy.ops.render.render(write_still=True)

            obj.rotation_euler[2] = orig_rot

        self.report({'INFO'}, f"ULTRA PRO Batch Complete: {base_path}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RENDER_OT_sgi_setup)
    bpy.utils.register_class(RENDER_OT_sgi_action)

def unregister():
    bpy.utils.unregister_class(RENDER_OT_sgi_setup)
    bpy.utils.unregister_class(RENDER_OT_sgi_action)
