"""
Microvellum 
Entry Doors
Stores the logic and product defs for entry doors.
"""

import bpy
import math
import os
import fd_library
from mv import fd_types, unit, utils

DOOR_FRAME_PATH = os.path.join(os.path.dirname(__file__),"Door Frames")
DOOR_PANEL = os.path.join(os.path.dirname(__file__),"Door Panels")
DOOR_HANDLE = os.path.join(os.path.dirname(__file__),"Door Handles","Door_Handle.blend")
MATERIAL_FILE = os.path.join(os.path.dirname(__file__),"materials","materials.blend")

SINGLE_PANEL_WIDTH = unit.inch(42)
DOUBLE_PANEL_WIDTH = unit.inch(84)
DOOR_HEIGHT = unit.inch(83)
DOOR_DEPTH = unit.inch(6)
HANDLE_HEIGHT = unit.inch(37)

class Entry_Door(fd_types.Assembly):
    library_name = "Entry Doors"
    category_name = ""
    assembly_name = ""
    property_id = "cabinetlib.entry_door_prompts"
    type_assembly = "PRODUCT"
    mirror_z = False
    mirror_y = False
    width = 0
    height = 0
    depth = 0
    
    door_frame = ""
    door_panel = ""
    double_door = False
    
    def draw(self):
        self.create_assembly()
        
        if self.door_panel != "":
            self.add_tab(name='Main Options',tab_type='VISIBLE')
            self.add_prompt(name="Reverse Swing",prompt_type='CHECKBOX',value=False,tab_index=0)
            self.add_prompt(name="Door Rotation",prompt_type='ANGLE',value=0.0,tab_index=0)
            if self.double_door != True:
                self.add_prompt(name="Door Swing",prompt_type='COMBOBOX',items=["Left Swing","Right Swing"],value=False,tab_index=0)
        
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Door_Rotation = self.get_var('Door Rotation')
        Reverse_Swing = self.get_var("Reverse Swing")
        if self.double_door != True:
            Swing = self.get_var('Door Swing')

        door_frame = self.add_assembly(os.path.join(DOOR_FRAME_PATH,self.door_frame))
        door_frame.set_name("Door Frame")
        door_frame.x_dim('Width',[Width])
        door_frame.y_dim('Depth',[Depth])
        door_frame.z_dim('Height',[Height])
        door_frame.assign_material("Frame",MATERIAL_FILE,"White")   
        
        if self.door_panel != "":
            door_panel = self.add_assembly(os.path.join(DOOR_PANEL,self.door_panel))
            door_panel.set_name("Door Panel")
            if self.double_door != True:
                door_panel.x_loc('IF(Door_Swing==1,Width-INCH(3),INCH(3))',[Width, Swing])
                door_panel.y_loc('IF(Reverse_Swing,IF(Door_Swing==0,INCH(1.75),0),IF(Door_Swing==0,Depth,Depth-INCH(1.75)))',[Swing, Reverse_Swing, Depth])
                door_panel.z_rot('IF(Door_Swing==1,radians(180)+IF(Reverse_Swing,Door_Rotation,-Door_Rotation),IF(Reverse_Swing,-Door_Rotation,Door_Rotation))',
                                 [Door_Rotation, Swing, Reverse_Swing])
                
            else:
                door_panel.x_loc(value = unit.inch(3))
                door_panel.y_loc('Depth-IF(Reverse_Swing,INCH(4.25),INCH(0))',[Reverse_Swing, Depth])
                door_panel.z_rot('IF(Reverse_Swing,-Door_Rotation,Door_Rotation)',[Door_Rotation, Reverse_Swing])                

            door_panel.x_dim('Width-INCH(6)',[Width])
            door_panel.z_dim('Height-INCH(3.25)',[Height])
            door_panel.assign_material("Door",MATERIAL_FILE,"White")
            door_panel.assign_material("Glass",MATERIAL_FILE,"Glass")
            door_panel.assign_material("Hinge",MATERIAL_FILE,"Stainless Steel")
            
            door_handle = self.add_object(DOOR_HANDLE)
            door_handle.obj.parent = door_panel.obj_bp
            door_handle.set_name("Door Handle")
            door_handle.x_loc('Width-INCH(9)',[Width])
            door_handle.y_loc(value = unit.inch(-0.875))
            door_handle.z_loc(value = HANDLE_HEIGHT)

        if self.double_door == True:
            door_panel.x_dim('(Width-INCH(6))*0.5',[Width])
            door_handle.x_loc('(Width*0.5)-INCH(6)',[Width])
        
            door_panel_right = self.add_assembly(os.path.join(DOOR_PANEL,self.door_panel))
            door_panel_right.set_name("Door Panel Right")
            door_panel_right.x_loc('Width-INCH(3)',[Width])
            door_panel_right.y_loc('Depth-INCH(1.75)-IF(Reverse_Swing,INCH(4.25),INCH(0))',[Reverse_Swing, Depth])
            door_panel_right.z_rot('radians(180)+IF(Reverse_Swing,Door_Rotation,-Door_Rotation)',[Door_Rotation, Reverse_Swing])
            door_panel_right.x_dim('(Width-INCH(6))*0.5',[Width])
            door_panel_right.z_dim('Height-INCH(3.25)',[Height])     
            door_panel_right.assign_material("Door",MATERIAL_FILE,"White")   
            door_panel_right.assign_material("Glass",MATERIAL_FILE,"Glass")  
            door_panel_right.assign_material("Hinge",MATERIAL_FILE,"Stainless Steel")  
                
            Dpr_Width = door_panel_right.get_var('dim_x','Dpr_Width')
            
            door_handle_right = self.add_object(DOOR_HANDLE)
            door_handle_right.set_name("Door Handle Right")
            door_handle_right.obj.parent = door_panel_right.obj_bp
            door_handle_right.x_loc('Dpr_Width-INCH(3)', [Dpr_Width])
            door_handle_right.y_loc(value = unit.inch(-0.875))
            door_handle_right.z_loc(value = HANDLE_HEIGHT)
                
        self.update()       
  
class PRODUCT_Entry_Door_Frame(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Frame"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"   
  
class PRODUCT_Entry_Door_Double_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Double Panel"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Double.blend"
 
class PRODUCT_Entry_Door_Inset_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Inset Panel"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Inset.blend"
 
class PRODUCT_Entry_Door_Glass_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Panel"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass.blend"
        
class PRODUCT_Entry_Door_Glass_Georgian_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Georgian Panel"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass_Georgian.blend"
        
class PRODUCT_Entry_Door_Glass_Border_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Door Glass Border Panel"
        self.width = SINGLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass_Marginal_Border.blend"
        
class PRODUCT_Entry_Double_Door_Double_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Double Panel"
        self.width = DOUBLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.double_door = True
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Double.blend"
        
class PRODUCT_Entry_Double_Door_Inset_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Inset Panel"
        self.width = DOUBLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.double_door = True
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Inset.blend"
        
class PRODUCT_Entry_Double_Door_Glass_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Panel"
        self.width = DOUBLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.double_door = True
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass.blend"
        
class PRODUCT_Entry_Double_Door_Glass_Georgian_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Georgian Panel"
        self.width = DOUBLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.double_door = True
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass_Georgian.blend"
        
class PRODUCT_Entry_Double_Door_Glass_Border_Panel(Entry_Door):
    
    def __init__(self):
        self.category_name = "Entry Doors"
        self.assembly_name = "Entry Double Door Glass Border Panel"
        self.width = DOUBLE_PANEL_WIDTH
        self.height = DOOR_HEIGHT
        self.depth = DOOR_DEPTH
        
        self.double_door = True
        self.door_frame = "Door_Frame.blend"
        self.door_panel = "Door_Panel_Glass_Marginal_Border.blend"
        
class PROMPTS_Entry_Door_Prompts(bpy.types.Operator):
    bl_idname = "cabinetlib.entry_door_prompts"
    bl_label = "Entry Door Prompts" 
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name")
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)

    door_rotation = bpy.props.FloatProperty(name="Door Rotation",subtype='ANGLE',min=0,max=math.radians(110))
    
    door_swing = bpy.props.EnumProperty(name="Door Swing",items=[('Left Swing',"Left Swing","Left Swing"),
                                                                 ('Right Swing',"Right Swing","Right Swing")])
    product = None
    
    open_door_prompt = None
    
    door_swing_prompt = None
    
    @classmethod
    def poll(cls, context):
        return True

    def check(self, context):
        self.product.obj_x.location.x = self.width
         
        if self.product.obj_bp.mv.mirror_y:
            self.product.obj_y.location.y = -self.depth
        else:
            self.product.obj_y.location.y = self.depth
         
        if self.product.obj_bp.mv.mirror_z:
            self.product.obj_z.location.z = -self.height
        else:
            self.product.obj_z.location.z = self.height
             
        if self.open_door_prompt:
            self.open_door_prompt.set_value(self.door_rotation)
            
        if self.door_swing_prompt:
            self.door_swing_prompt.set_value(self.door_swing)            
             
        self.product.obj_bp.location = self.product.obj_bp.location
        self.product.obj_bp.location = self.product.obj_bp.location
            
        return True

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self,context,event):
        obj = bpy.data.objects[self.object_name]
        obj_product_bp = utils.get_bp(obj,'PRODUCT')
        self.product = fd_types.Assembly(obj_product_bp)
        if self.product.obj_bp:
            self.depth = math.fabs(self.product.obj_y.location.y)
            self.height = math.fabs(self.product.obj_z.location.z)
            self.width = math.fabs(self.product.obj_x.location.x)
            
            try:
                self.open_door_prompt = self.product.get_prompt("Door Rotation")
                self.door_rotation = self.open_door_prompt.value() 
            except:
                pass
            
            try:
                self.door_swing_prompt = self.product.get_prompt("Door Swing")  
                self.door_swing = self.door_swing_prompt.value()         
            except:
                pass
                
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=480)

    def draw_product_size(self,layout):
        row = layout.row()
        box = row.box()
        col = box.column(align=True)

        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_x):
            row1.label('Width: ' + str(unit.inch(math.fabs(self.product.obj_x.location.x))))
        else:
            row1.label('Width:')
            row1.prop(self,'width',text="")
            row1.prop(self.product.obj_x,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_z):
            row1.label('Height: ' + str(unit.inch(math.fabs(self.product.obj_z.location.z))))
        else:
            row1.label('Height:')
            row1.prop(self,'height',text="")
            row1.prop(self.product.obj_z,'hide',text="")
        
        row1 = col.row(align=True)
        if self.object_has_driver(self.product.obj_y):
            row1.label('Depth: ' + str(unit.inch(math.fabs(self.product.obj_y.location.y))))
        else:
            row1.label('Depth:')
            row1.prop(self,'depth',text="")
            row1.prop(self.product.obj_y,'hide',text="")
            
    def object_has_driver(self,obj):
        if obj.animation_data:
            if len(obj.animation_data.drivers) > 0:
                return True
            
    def draw_product_prompts(self,layout):

        if "Main Options" in self.product.obj_bp.mv.PromptPage.COL_MainTab:
            door_swing = self.product.get_prompt("Door Swing")
            reverse_swing = self.product.get_prompt("Reverse Swing")
            
            box = layout.box()
            col = box.column(align=True)
            col.label("Main Options:")
            row = col.row()
            row.label("Open Door")
            row.prop(self,'door_rotation',text="",slider=True)   
            if door_swing:
                col = box.column()
                row = col.row()                
                row.label("Door Swing")
                row.prop(self, 'door_swing',text="")
            col = box.column()
            row = col.row()                
            row.label("Reverse Swing")
            row.prop(reverse_swing,'CheckBoxValue',text="")            
    
    def draw_product_placment(self,layout):
        box = layout.box()
        row = box.row()
        row.label('Location:')
        row.prop(self.product.obj_bp,'location',index=0,text="")

    def draw(self, context):
        layout = self.layout
        if self.product.obj_bp:
            if self.product.obj_bp.name in context.scene.objects:
                box = layout.box()
                
                split = box.split(percentage=.8)
                split.label(self.product.obj_bp.mv.name_object + " | " + self.product.obj_bp.cabinetlib.spec_group_name,icon='LATTICE_DATA')
                split.menu('MENU_Current_Cabinet_Menu',text="Menu",icon='DOWNARROW_HLT')
                
                self.draw_product_size(box)
                self.draw_product_prompts(box)
                self.draw_product_placment(box)        
        
def register():
    bpy.utils.register_class(PROMPTS_Entry_Door_Prompts)