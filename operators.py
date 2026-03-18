import bpy
import os
import math

def setup_sgi_render(scene, res=512):
    """Pro Render Engine Specs."""
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.engine = 'CYCLES'
    
    scene.render.resolution_x, scene.render.resolution_y = res, res
    
    # Adaptive Anti-Aliasing (Crisp for pixel art, smooth for HD)
    scene.render.filter_size = 0.01 if res <= 64 else 1.5

class RENDER_OT_sgi_setup(bpy.types.Operator):
    """Builds the Floor and the SGI Lighting Rig."""
    bl_idname = "render.sgi_setup"
    bl_label = "Initialize MAX PRO Studio"

    def execute(self, context):
        setup_sgi_render(context.scene)
        
        # Add Shadow Floor
        if "SGI_Shadow_Floor" not in bpy.data.objects:
            bpy.ops.mesh.primitive_plane_add(size=50)
            plane = bpy.context.active_object
            plane.name = "SGI_Shadow_Floor"
            plane.cycles.is_shadow_catcher = True
            
        # Add Classic 3-Point SGI Sun Light
        if "SGI_Main_Light" not in bpy.data.objects:
            bpy.ops.object.light_add(type='SUN', location=(5, -5, 10), rotation=(math.radians(45), 0, math.radians(45)))
            light = bpy.context.active_object
            light.name = "SGI_Main_Light"
            light.data.energy = 3.0
            light.data.angle = math.radians(5) # Sharp shadows for retro look
        
        self.report({'INFO'}, "MAX PRO Studio: Floor and Lighting Online.")
        return {'FINISHED'}

class RENDER_OT_sgi_action(bpy.types.Operator):
    """Handles 4, 8, and 16-directional batching."""
    bl_idname = "render.sgi_action"
    bl_label = "SGI Render"
    mode: bpy.props.StringProperty()
    res: bpy.props.IntProperty(default=512)
    dirs: bpy.props.IntProperty(default=8) # Variable directions!

    def execute(self, context):
        scene = context.scene
        
        # SMART SELECT: Grab selected items, completely ignore anything starting with "SGI_"
        targets = [obj for obj in context.selected_objects if not obj.name.startswith("SGI_")]
        
        if not targets and context.active_object and not context.active_object.name.startswith("SGI_"):
            targets = [context.active_object]

        if not scene.camera:
            self.report({'ERROR'}, "PRO PIPELINE HALTED: Add a Camera!")
            return {'CANCELLED'}
        if not targets:
            self.report({'ERROR'}, "PRO PIPELINE HALTED: Select your character/rig!")
            return {'CANCELLED'}

        setup_sgi_render(scene, res=self.res)
        base_path = os.path.join(os.path.expanduser('~'), 'Desktop', "SGI_MAX_PRO_OUTPUT")

        for obj in targets:
            obj_dir = os.path.join(base_path, obj.name, f"Res_{self.res}")
            if not os.path.exists(obj_dir): os.makedirs(obj_dir)

            orig_rot = obj.rotation_euler[2]

            if self.mode == "STILL":
                scene.render.filepath = os.path.join(obj_dir, f"{obj.name}_still.png")
                bpy.ops.render.render(write_still=True)
                
            elif self.mode == "ANIM_MULTI":
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

        self.report({'INFO'}, f"SUCCESS: {self.dirs}-Direction Render saved to Desktop!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RENDER_OT_sgi_setup)
    bpy.utils.register_class(RENDER_OT_sgi_action)

def unregister():
    bpy.utils.unregister_class(RENDER_OT_sgi_setup)
    bpy.utils.unregister_class(RENDER_OT_sgi_action)
