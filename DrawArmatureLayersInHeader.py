bl_info = {
    "name": "Custom armature layers on top",
    "author": "Rentegra",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "3D View > Header",
    "description": "Draws the Bone Layer diagram into the 3D View Header when an armature object is selected.",
    "warning": "",
    "wiki_url": "",
    "category": "UI",
}


import bpy

class BL_HT_MyClass(bpy.types.Header):
    bl_space_type = 'TOPBAR'
    def draw(self, context):
        layout = self.layout
        arm = context.active_object.data
        col = layout.column()
        col.scale_y = 0.75
        col.prop(arm, "layers", text="")

    @classmethod   
    def poll(cls, context):
        return context.active_object.type == "ARMATURE"
    
    bpy.types.VIEW3D_HT_header.append(draw)

def register():
    bpy.utils.register_class(BL_HT_MyClass)

def unregister():
    bpy.utils.unregister_class(BL_HT_MyClass)