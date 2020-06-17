bl_info = {
    "name": "Vertex Light",
    "category": "Object",
}

import bpy
import bmesh
from math import *
from mathutils import *

class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}

    selected_faces_only = bpy.props.BoolProperty(
        name="Selected faces only",
        description="Apply changes only to selected faces",
        default = False
        )
    clear_previous = bpy.props.BoolProperty(
        name="Clear Previous Color",
        description="Remove existing \"color\"",
        default = False
        )
    clear_alpha = bpy.props.FloatProperty(
        name = "Base Color Factor",
        description = "How much of base color to be added",
        default = 0.0,
        min = -1.0,
        max = 1.0
        )
    clear_color = bpy.props.FloatVectorProperty(
        name="Base color",
        description="add specified color to vertexes",
        default = (1.0,1.0,1.0)
        )
    light_enabled = bpy.props.BoolProperty(
        name="Enable Light",
        description="Eneables light",
        default = False
        )
    alpha = bpy.props.IntProperty(
        name = "horizontal angle",
        description = "Set horizontal axis angle",
        default = 45,
        min = 0,
        max = 360
        )
    beta = bpy.props.IntProperty(
        name = "vertical angle",
        description = "Set vertical axis angle",
        default = 45,
        min = 0,
        max = 360
        )
    light_color = bpy.props.FloatVectorProperty(
        name="light color",
        description="color of light",
        default = (1,1,1)
        )
    light_amt = bpy.props.FloatProperty(
        name = "Light Amount",
        description = "How much of the light will be aplied",
        default = 0.5,
        min = 0.0,
        max = 1.0
        )
    angle_allowance = bpy.props.FloatProperty(
        name = "Light Angle allowance",
        description = "How much of the angle is allowed",
        default = 0,
        min = -0.99,
        max = 10.0
        )
    smooth_enabled = bpy.props.BoolProperty(
        name="Enable color smoothing",
        description="Make edges less apparent by smoothing color of vertexes",
        default = False
        )
    smooth_selected_only = bpy.props.BoolProperty(
        name="Only selected vertices",
        description="Apply smoothness only to selected vertices",
        default = False
        )
    smooth_amt = bpy.props.FloatProperty(
        name = "Smooth Amount",
        description = "How smooth it will be",
        default = 0.5,
        min = 0.0,
        max = 1.0
        )

    def execute(self, context):
        scene = context.scene
        obj = scene.objects.active
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        faces = bm.faces
        #clear lights
        colors = bm.loops.layers.color.active
        if not colors:
            colors = bm.loops.layers.color.new("Col")
        for face in faces:
            if ((self.selected_faces_only and face.select) or(not self.selected_faces_only)):
                for loop in face.loops:
                    if (self.clear_previous):
                        loop[colors] = (0,0,0)
                    loop[colors] = Vector(loop[colors])+self.clear_alpha*Vector(self.clear_color)
        #apply light
        if (self.light_enabled):
            colors = bm.loops.layers.color.active
            light = Vector(self.light_color)
            amount = self.light_amt
            a = radians(self.alpha)
            b = radians(self.beta)
            light_direction = Vector((cos(b)*cos(a),cos(b)*sin(a),sin(b)))
            if not colors:
                colors = bm.loops.layers.color.new("Col")
            for face in faces:
                if ((self.selected_faces_only and face.select) or (not self.selected_faces_only)):
                    n = face.normal
                    lightness = Vector(n).dot(Vector(light_direction).normalized())
                    lightness = (lightness+self.angle_allowance)/(1+self.angle_allowance)   #remap
                    lightness = lightness if lightness > 0 else 0
                    for loop in face.loops:
                        loop[colors] = Vector(loop[colors]) + amount *(light*lightness)
        #smooth vertexes
        if (self.smooth_enabled):
            verts = bm.verts
            colors = bm.loops.layers.color.active
            if not colors:
                colors = bm.loops.layers.color.new("Col")
            factor = self.smooth_amt
            for v in verts:
                if ((self.smooth_selected_only and v.select) or (not self.smooth_selected_only)):
                    sum = Vector((0,0,0))
                    count = len(v.link_loops)
                    if count == 0:
                        continue
                    for loop in v.link_loops:
                        sum += Vector(loop[colors])
                        #loop[colors] = (n.x,n.y,n.z)
                    mean = sum/count
                    for loop in v.link_loops:
                        loop[colors] = (Vector(loop[colors])*(1-factor)+mean*factor)
        bm.to_mesh(obj.data)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either,
    # so we have to check this to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
    # Can avoid strange issues like keymap still referring to operators already unregistered...
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()