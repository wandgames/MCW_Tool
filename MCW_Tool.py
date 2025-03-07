bl_info = {
    "name": "MCW Tool",
    "author": "Wand GAMES",
    "version": (0,0,1),
    "blender": (4, 0, 2),
    "location": "3D Viewport > Sidebar > MCW Tool",
    "description":"This is a tool for building our Modular Cyberpunk Weapons",
    "category": "Mesh"
}

import bpy
import mathutils

# Define the serial code options in a dropdown
class MCWToolProperties(bpy.types.PropertyGroup):
    serial_code: bpy.props.EnumProperty(
        name="Serial Code",
        description="Choose a serial code for pistol parts",
        items=[
            ("B000000", "B000000", ""),
            ("B0000F0", "B0000F0", ""),
            ("B0000L0", "B0000L0", ""),
            ("B000S00", "B000S00", ""),
            ("B000SF0", "B000SF0", ""),
            ("B000SL0", "B000SL0", ""),
            ("B00000R", "B00000R", ""),
            ("B0000FR", "B0000FR", ""),
            ("B0000LR", "B0000LR", ""),
            ("B000S0R", "B000S0R", ""),
            ("B000SLR", "B000SLR", ""),
            ("B000SFR", "B000SFR", ""),
            
            ("B00A000", "B00A000", ""),
            ("B00A0F0", "B00A0F0", ""),
            ("B00A0L0", "B00A0L0", ""),
            ("B00AS00", "B00AS00", ""),
            ("B00ASF0", "B00ASF0", ""),
            ("B00ASL0", "B00ASL0", ""),
            ("B00A00R", "B00A00R", ""),
            ("B00A0FR", "B00A0FR", ""),
            ("B00A0LR", "B00A0LR", ""),
            ("B00AS0R", "B00AS0R", ""),
            ("B00ASLR", "B00ASLR", ""),
            ("B00ASFR", "B00ASFR", ""),
            
            ("BE00000", "BE00000", ""),
            ("BE000F0", "BE000F0", ""),
            ("BE000L0", "BE000L0", ""),
            ("BE00S00", "BE00S00", ""),
            ("BE00SF0", "BE00SF0", ""),
            ("BE00SL0", "BE00SL0", ""),
            ("BE0000R", "BE0000R", ""),
            ("BE000FR", "BE000FR", ""),
            ("BE000LR", "BE000LR", ""),
            ("BE00S0R", "BE00S0R", ""),
            ("BE00SLR", "BE00SLR", ""),
            ("BE00SFR", "BE00SFR", ""),
            
            ("BE0A000", "BE0A000", ""),
            ("BE0A0F0", "BE0A0F0", ""),
            ("BE0A0L0", "BE0A0L0", ""),
            ("BE0AS00", "BE0AS00", ""),
            ("BE0ASF0", "BE0ASF0", ""),
            ("BE0ASL0", "BE0ASL0", ""),
            ("BE0A00R", "BE0A00R", ""),
            ("BE0A0FR", "BE0A0FR", ""),
            ("BE0A0LR", "BE0A0LR", ""),
            ("BE0AS0R", "BE0AS0R", ""),
            ("BE0ASLR", "BE0ASLR", ""),
            ("BE0ASFR", "BE0ASFR", ""),
            
            ("BEC0000", "BEC0000", ""),
            ("BEC00F0", "BEC00F0", ""),
            ("BEC00L0", "BEC00L0", ""),
            ("BEC0S00", "BEC0S00", ""),
            ("BEC0SF0", "BEC0SF0", ""),
            ("BEC0SL0", "BEC0SL0", ""),
            ("BEC000R", "BEC000R", ""),
            ("BEC00FR", "BEC00FR", ""),
            ("BEC00LR", "BEC00LR", ""),
            ("BEC0S0R", "BEC0S0R", ""),
            ("BEC0SLR", "BEC0SLR", ""),
            ("BEC0SFR", "BEC0SFR", ""),
            
            ("BECA000", "BECA000", ""),
            ("BECA0F0", "BECA0F0", ""),
            ("BECA0L0", "BECA0L0", ""),
            ("BECAS00", "BECAS00", ""),
            ("BECASF0", "BECASF0", ""),
            ("BECASL0", "BECASL0", ""),
            ("BECA00R", "BECA00R", ""),
            ("BECA0FR", "BECA0FR", ""),
            ("BECA0LR", "BECA0LR", ""),
            ("BECAS0R", "BECAS0R", ""),
            ("BECASLR", "BECASLR", ""),
            ("BECASFR", "BECASFR", ""),
            
            ("P000000", "P000000", ""),
            ("P0000F0", "P0000F0", ""),
            ("P0000L0", "P0000L0", ""),
            ("P000S00", "P000S00", ""),
            ("P000SF0", "P000SF0", ""),
            ("P000SL0", "P000SL0", ""),
            ("P00000R", "P00000R", ""),
            ("P0000FR", "P0000FR", ""),
            ("P0000LR", "P0000LR", ""),
            ("P000S0R", "P000S0R", ""),
            ("P000SLR", "P000SLR", ""),
            ("P000SFR", "P000SFR", ""),
            
            ("P00A000", "P00A000", ""),
            ("P00A0F0", "P00A0F0", ""),
            ("P00A0L0", "P00A0L0", ""),
            ("P00AS00", "P00AS00", ""),
            ("P00ASF0", "P00ASF0", ""),
            ("P00ASL0", "P00ASL0", ""),
            ("P00A00R", "P00A00R", ""),
            ("P00A0FR", "P00A0FR", ""),
            ("P00A0LR", "P00A0LR", ""),
            ("P00AS0R", "P00AS0R", ""),
            ("P00ASLR", "P00ASLR", ""),
            ("P00ASFR", "P00ASFR", ""),
            
            ("PE00000", "PE00000", ""),
            ("PE000F0", "PE000F0", ""),
            ("PE000L0", "PE000L0", ""),
            ("PE00S00", "PE00S00", ""),
            ("PE00SF0", "PE00SF0", ""),
            ("PE00SL0", "PE00SL0", ""),
            ("PE0000R", "PE0000R", ""),
            ("PE000FR", "PE000FR", ""),
            ("PE000LR", "PE000LR", ""),
            ("PE00S0R", "PE00S0R", ""),
            ("PE00SLR", "PE00SLR", ""),
            ("PE00SFR", "PE00SFR", ""),
            
            ("PE0A000", "PE0A000", ""),
            ("PE0A0F0", "PE0A0F0", ""),
            ("PE0A0L0", "PE0A0L0", ""),
            ("PE0AS00", "PE0AS00", ""),
            ("PE0ASF0", "PE0ASF0", ""),
            ("PE0ASL0", "PE0ASL0", ""),
            ("PE0A00R", "PE0A00R", ""),
            ("PE0A0FR", "PE0A0FR", ""),
            ("PE0A0LR", "PE0A0LR", ""),
            ("PE0AS0R", "PE0AS0R", ""),
            ("PE0ASLR", "PE0ASLR", ""),
            ("PE0ASFR", "PE0ASFR", ""),
            
            ("PEC0000", "PEC0000", ""),
            ("PEC00F0", "PEC00F0", ""),
            ("PEC00L0", "PEC00L0", ""),
            ("PEC0S00", "PEC0S00", ""),
            ("PEC0SF0", "PEC0SF0", ""),
            ("PEC0SL0", "PEC0SL0", ""),
            ("PEC000R", "PEC000R", ""),
            ("PEC00FR", "PEC00FR", ""),
            ("PEC00LR", "PEC00LR", ""),
            ("PEC0S0R", "PEC0S0R", ""),
            ("PEC0SLR", "PEC0SLR", ""),
            ("PEC0SFR", "PEC0SFR", ""),
            
            ("PECA000", "PECA000", ""),
            ("PECA0F0", "PECA0F0", ""),
            ("PECA0L0", "PECA0L0", ""),
            ("PECAS00", "PECAS00", ""),
            ("PECASF0", "PECASF0", ""),
            ("PECASL0", "PECASL0", ""),
            ("PECA00R", "PECA00R", ""),
            ("PECA0FR", "PECA0FR", ""),
            ("PECA0LR", "PECA0LR", ""),
            ("PECAS0R", "PECAS0R", ""),
            ("PECASLR", "PECASLR", ""),
            ("PECASFR", "PECASFR", ""),
    
        ],
        default="B000000"
    )

# Function to hide/unhide objects based on serial code
def apply_serial_code(operator, serial_code):
    reset_all_objects()
    attachment_position_add = 0
    silencer_position_obj_name = ""
    current_silencer = ""
    
    objects_to_hide = []
    
    structure = list(serial_code)
    
    if structure[0] == "P":
        objects_to_hide.append('HandleWithMag.001')
        objects_to_hide.append('Mag.001')
        objects_to_hide.append('MainBarrel.001')
        objects_to_hide.append('MuzzleTube.001')
        objects_to_hide.append('Silencer.001')
    else:
        objects_to_hide.append('Handle.001')
        objects_to_hide.append('ChargerPort.001')
        objects_to_hide.append('LaserBarrel.001')
        objects_to_hide.append('PABarrel.001')
        objects_to_hide.append('PlasmaSilencer.001')
     
    if structure[1] == "E":
         objects_to_hide.append('Muzzle.001')
         objects_to_hide.append('BPShield.001')
         objects_to_hide.append('MiniBottomPieceCore.001')
         objects_to_hide.append('MiniBottomPieceAttachment.001')
         if structure[2] == "C":
            objects_to_hide.append('BottomPiece.001')
            objects_to_hide.append('BottomAttachmentHolderShort.001')
            current_holder = "BottomAttachmentHolder.001"
         else:
            objects_to_hide.append('Coolant.001') 
            objects_to_hide.append('BottomAttachmentHolder.001')
            current_holder = "BottomAttachmentHolderShort.001"
    else:
        attachment_position_add = 0.027
        objects_to_hide.append('PowerAttachment.001')
        objects_to_hide.append('PABarrel.001')
        objects_to_hide.append('MuzzleTube.001')
        objects_to_hide.append('BottomPiece.001')
        objects_to_hide.append('BottomAttachmentHolderShort.001')
        objects_to_hide.append('BottomAttachmentHolder.001')
        objects_to_hide.append('ConnectiveMuzzle.001')
        objects_to_hide.append('Coolant.001')
        
        current_holder = 'MiniBottomPieceAttachment.001'
        
    if structure[3] == "0":
        objects_to_hide.append('AlternativeShotModule.001')
    
    if structure[4] == "S":
        if structure[0] == "P":
            objects_to_hide.append('Silencer.001')
            current_silencer = 'PlasmaSilencer.001'
        else:
            objects_to_hide.append('PlasmaSilencer.001')
            current_silencer = "Silencer.001"
            
            
        if structure[1] != "E":
            silencer_position_obj_name = 'MainBarrel.001'
        else:
            silencer_position_obj_name = 'MuzzleTube.001'
    else:
        objects_to_hide.append('Silencer.001')
        objects_to_hide.append('PlasmaSilencer.001')
    
    current_attachment = ""
    if structure[5] == "F":
        objects_to_hide.append('Laser.001')
        current_attachment = 'Flash.001';
        
    elif structure[5] == "L":
        objects_to_hide.append('Flash.001')
        current_attachment = 'Laser.001';
    else:
        objects_to_hide.append('Laser.001')
        objects_to_hide.append('Flash.001')
    
    if structure[6] == "R":
        objects_to_hide.append('AnalogSight.001')
    else:
        objects_to_hide.append('RedDotSight.001')
    
    
    if current_attachment != "":
        holder_obj = bpy.data.objects.get(current_holder)
        attachment_obj = bpy.data.objects.get(current_attachment)
        y_offset =  (-0.96 * abs(attachment_obj.dimensions.y)) + holder_obj.dimensions.y/2
        
        bbox_corners = [attachment_obj.matrix_world @ mathutils.Vector(corner) for corner in attachment_obj.bound_box]
        y_min = min(corner.y for corner in bbox_corners)
        y_start = (abs(y_min) - abs(attachment_obj.location.y))
    
        y_offset = -1*(holder_obj.dimensions.y / 2.1) + y_start  - attachment_position_add
             
        offset = mathutils.Vector((0, y_offset, -0.0185))
        
        location = holder_obj.location + offset
        attachment_obj.location = location
    
    if current_silencer != "":
       
        silencer_position_obj = bpy.data.objects.get(silencer_position_obj_name)
        operator.report({'INFO'}, f"Obj: {silencer_position_obj}") 
        
        bbox_corners = [silencer_position_obj.matrix_world @ mathutils.Vector(corner) for corner in silencer_position_obj.bound_box]
        y_min = min(corner.y for corner in bbox_corners)
        
        current_silencer = bpy.data.objects.get(current_silencer)
        
        bbox_corners = [current_silencer.matrix_world @ mathutils.Vector(corner) for corner in current_silencer.bound_box]
        y_silencer_max = min(corner.y for corner in bbox_corners)
        
        y_offset =  abs(current_silencer.location.y) - abs(y_silencer_max)
        
        offset = mathutils.Vector((0, y_offset, 0))
        
        location = silencer_position_obj.location
        current_silencer.location.y = y_min + y_offset + 0.012
     
    for obj_name in objects_to_hide:
        obj = bpy.data.objects.get(obj_name)
        operator.report({'INFO'}, f"Hiding: {obj_name}") 
        operator.report({'INFO'}, f"Object: {obj}") 
        obj.hide_viewport = True  # Unhide in viewport
        obj.hide_render = True
        
            
            
# Function to unhide all objects
def reset_all_objects():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':  # Unhide only mesh objects (adjust as needed)
            obj.hide_viewport = False  # Unhide in viewport
            obj.hide_render = False  # Unhide in render
    

# Operator to apply the serial code
class OBJECT_OT_ApplySerial(bpy.types.Operator):
    """Apply Serial Code to Hide/Unhide Parts"""
    bl_idname = "object.apply_serial"
    bl_label = "Apply Serial Code"

    def execute(self, context):
        props = context.scene.mcw_tool_props
        self.report({'INFO'}, f"Applying Serial Code: {props.serial_code}")
        apply_serial_code(self, props.serial_code)
        return {'FINISHED'}
    
# Operator to reset all objects
class OBJECT_OT_ResetAll(bpy.types.Operator):
    """Reset All Objects to be Visible"""
    bl_idname = "object.reset_all"
    bl_label = "Reset All Objects"

    def execute(self, context):
        reset_all_objects()  # Unhide all objects in the scene
        self.report({'INFO'}, "All objects are now visible.")
        return {'FINISHED'}
    
# UI Panel
class VIEW3D_PT_MCW_Tool(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "MCW Pistol"
    bl_category = "MCW Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.mcw_tool_props

        layout.prop(props, "serial_code", text="Select Serial Code")  # Dropdown for serial code
        layout.operator("object.apply_serial", text="Apply Serial Code")  # Button to apply
        layout.operator("object.reset_all", text="Reset All Objects")

# Register functions
def register():
    bpy.utils.register_class(MCWToolProperties)
    bpy.utils.register_class(OBJECT_OT_ApplySerial)
    bpy.utils.register_class(OBJECT_OT_ResetAll)
    bpy.utils.register_class(VIEW3D_PT_MCW_Tool)
    bpy.types.Scene.mcw_tool_props = bpy.props.PointerProperty(type=MCWToolProperties)

def unregister():
    bpy.utils.unregister_class(MCWToolProperties)
    bpy.utils.unregister_class(OBJECT_OT_ApplySerial)
    bpy.utils.unregister_class(OBJECT_OT_ResetAll)
    bpy.utils.unregister_class(VIEW3D_PT_MCW_Tool)
    del bpy.types.Scene.mcw_tool_props

# Run in Blender
if __name__ == "__main__":
    register()
