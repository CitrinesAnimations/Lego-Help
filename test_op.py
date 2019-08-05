import bpy

class Test_OT_Operator(bpy.types.Operator):
    bl_idname = "bevel.lego"
    bl_label = "Bevel"
    bl_description = "Bevel"

    def execute(self, context):
        #selected = bpy.context.selected_objects
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.bevel(offset=0.1, offset_pct=0, segments=3, vertex_only=False, clamp_overlap=False, harden_normals=True)
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
        