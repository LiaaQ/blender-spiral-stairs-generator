bl_info = {
    "name": "Stairs Generator",
    "description": "Generates spiraling stairs",
    "author": "Natalie Teplicka",
    "version": (1, 0, 0),
    "blender": (4, 3, 2),
    "location": "View3D > UI Panel > Staircase",
    "category": "Add Mesh"
}

import bpy
import math

class OBJECT_OT_staircase(bpy.types.Operator):
    """Generate a spiral staircase with customizable parameters"""
    bl_idname = "object.generate_spiral_staircase"
    bl_label = "Generate Spiral Staircase"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        scene = context.scene
        
        # Retrieve the parameters from the scene properties
        step_count = scene.step_count
        step_width = scene.step_width
        step_depth = scene.step_depth
        step_height = scene.step_height
        radius = scene.radius
        
        angle_step = (2 * math.pi) / step_count  # Full circle divided by step count
        
        # Loop to create each step
        for i in range(step_count):
            angle = i * angle_step
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            z = i * step_height
            
            # Create a single step as a simple cube
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
            step = bpy.context.object
            
            # Scale step dimensions
            step.scale[0] = step_width
            step.scale[1] = step_depth 
            step.scale[2] = step_height
            
            # Rotate step to align with the spiral path
            step.rotation_euler[2] = angle  # Rotate around Z axis to face inward
            
        return {'FINISHED'}
    
# Panel to host the options
class VIEW3D_PT_staircase_panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Spiral Staircase Generator"
    bl_idname = "VIEW3D_PT_staircase_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Staircase'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Create UI controls for parameters
        layout.prop(scene, "step_count")
        layout.prop(scene, "step_width")
        layout.prop(scene, "step_depth")
        layout.prop(scene, "step_height")
        layout.prop(scene, "radius")
        
        # Add button to execute the operator
        layout.operator("object.generate_spiral_staircase", text="Generate Spiral Staircase")

# Function to initialize properties in the scene
def init_properties():
    bpy.types.Scene.step_count = bpy.props.IntProperty(name="Step Count", default=30, min=3)
    bpy.types.Scene.step_width = bpy.props.FloatProperty(name="Step Width", default=1.0)
    bpy.types.Scene.step_depth = bpy.props.FloatProperty(name="Step Depth", default=0.3)
    bpy.types.Scene.step_height = bpy.props.FloatProperty(name="Step Height", default=0.2)
    bpy.types.Scene.radius = bpy.props.FloatProperty(name="Radius", default=0.8)

# Cleanup function for removing properties
def clear_properties():
    del bpy.types.Scene.step_count
    del bpy.types.Scene.step_width
    del bpy.types.Scene.step_depth
    del bpy.types.Scene.step_height
    del bpy.types.Scene.radius

# Register classes and properties
def register():
    bpy.utils.register_class(OBJECT_OT_staircase)
    bpy.utils.register_class(VIEW3D_PT_staircase_panel)
    init_properties()

def unregister():
    clear_properties()
    bpy.utils.unregister_class(OBJECT_OT_staircase)
    bpy.utils.unregister_class(VIEW3D_PT_staircase_panel)

if __name__ == "__main__":
    # if our class is not already registered -> doesn't work
    if OBJECT_OT_staircase.bl_idname not in bpy.types.Operator.__subclasses__():
        register()
