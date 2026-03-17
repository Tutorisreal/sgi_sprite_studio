import bpy
import os
import math

def setup_sgi_render(scene, pixel_mode=False):
    """Configures technical SGI render parameters for sprites."""
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    
    # Cycles is required for the Shadow Catcher in Blender 2.93
    scene.render.engine = 'CYCLES'
    
    if pixel_mode:
        scene.render.resolution_x, scene.render.resolution_y = 64, 64
        scene.render.filter_size = 0.01 
    else:
        scene.render.resolution_x, scene.render.resolution_y = 512, 512
        scene.render.filter_size = 1.5 
        
    if not scene.camera:
        bpy.ops.object.camera_add(location=(0, -12, 8), rotation=(math.radians(60), 0, 0))
        scene.camera = bpy.context.object
        
    scene.camera.data.type = 'ORTHO'
    scene.camera.data.ortho_scale = 8.0

class RENDER_OT_sgi_setup(bpy.types.Operator):
    """Sets up the SGI studio environment."""
    bl_idname = "render.sgi_setup"
    bl_label = "Prepare SGI Studio"

    def execute(self, context):
        setup_sgi_render(context.scene)
        bpy.ops.mesh.primitive_plane_add(size=25)
        plane = bpy.context.active_object
        plane.name = "SGI_Shadow_Floor"
        
        # Fixed for 2.93 Cycles API
        plane.cycles.is_shadow_catcher = True
        
        self.report({'INFO'}, "SGI Studio v2.0 Ready")
        return {'FINISHED'}

class RENDER_OT_sgi_action(bpy.types.Operator):
    """Handles all v2.0 rendering modes."""
    bl_idname = "render.sgi_action"
    bl_label = "SGI Render"
    mode: bpy.props.StringProperty()
    pixel: bpy.props.BoolProperty(default=False)

    def execute(self, context):
        scene = context.scene
        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "Select an object first!")
            return {'CANCELLED'}

        setup_sgi_render(scene, pixel_mode=self.pixel)
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop', "SGI_Output", obj.name)
        if not os.path.exists(desktop): os.makedirs(desktop)

        orig_rot = obj.rotation_euler[2]

        if self.mode == "STILL":
            scene.render.filepath = os.path.join(desktop, f"{obj.name}_render.png")
            bpy.ops.render.render(write_still=True)
            
        elif self.mode == "SINGLE_ANIM":
            anim_dir = os.path.join(desktop, "Animation", "")
            if not os.path.exists(anim_dir): os.makedirs(anim_dir)
            scene.render.filepath = anim_dir
            bpy.ops.render.render(animation=True)
            
        elif self.mode == "BATCH":
            for i in range(8):
                obj.rotation_euler[2] = math.radians(i * 45)
                scene.render.filepath = os.path.join(desktop, f"angle_{i}.png")
                bpy.ops.render.render(write_still=True)
                
        elif self.mode == "ANIM_8DIR":
            for d in range(8):
                obj.rotation_euler[2] = math.radians(d * 45)
                dir_path = os.path.join(desktop, f"Dir_{d}")
                if not os.path.exists(dir_path): os.makedirs(dir_path)
                for f in range(scene.frame_start, scene.frame_end + 1):
                    scene.frame_set(f)
                    scene.render.filepath = os.path.join(dir_path, f"f_{f:03d}.png")
                    bpy.ops.render.render(write_still=True)

        obj.rotation_euler[2] = orig_rot
        self.report({'INFO'}, f"v2.0 Renders saved to {desktop}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RENDER_OT_sgi_setup)
    bpy.utils.register_class(RENDER_OT_sgi_action)

def unregister():
    bpy.utils.unregister_class(RENDER_OT_sgi_setup)
    bpy.utils.unregister_class(RENDER_OT_sgi_action)
