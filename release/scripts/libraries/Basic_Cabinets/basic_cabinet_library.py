import bpy
from mv import utils, unit
from . import basic_cabinets
from . import basic_cabinet_exteriors

LIBRARY_NAME = "Cabinets - Basic Library"
BASE_CATEGORY_NAME = "Base Cabinets"
SINK_CATEGORY_NAME = "Sink Cabinets"
TALL_CATEGORY_NAME = "Tall Cabinets"
UPPER_CATEGORY_NAME = "Upper Cabinets"
OUTSIDE_CORNER_CATEGORY_NAME = "Outside Corner Cabinets"
INSIDE_CORNER_CATEGORY_NAME = "Inside Corner Cabinets"
TRANSITION_CATEGORY_NAME = "Transition Cabinets"
STARTER_CATEGORY_NAME = "Starter Cabinets"
DRAWER_CATEGORY_NAME = "Drawer Cabinets"
BLIND_CORNER_CATEGORY_NAME = "Blind Corner Cabinets"

def get_props():
    return bpy.context.scene.lm_basic_cabinets.size_defaults

#---------PRODUCT: BASE CABINETS
        
class PRODUCT_1_Door_Base(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_1_door
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_2_Door_Base(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_2_door
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_2_Door_2_Drawer_Base(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_2_door
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Double_Door_Drawer()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_1_Door_1_Drawer_Base(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_1_door
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Single_Door_Drawer()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_1_Drawer(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.width = props.width_drawer
        self.exterior = basic_cabinet_exteriors.Drawers()
        self.exterior.drawer_qty = 1           
        
class PRODUCT_2_Drawer(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_drawer
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Drawers()
        self.exterior.drawer_qty = 2         
        
class PRODUCT_3_Drawer(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.width = props.width_drawer
        self.exterior = basic_cabinet_exteriors.Drawers()
        self.exterior.drawer_qty = 3           
        
class PRODUCT_4_Drawer(basic_cabinets.Base_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BASE_CATEGORY_NAME
        self.width = props.width_drawer
        self.exterior = basic_cabinet_exteriors.Drawers()
        self.exterior.drawer_qty = 4

#---------PRODUCT: Sink CABINETS

class PRODUCT_1_Door_Sink(basic_cabinets.Sink_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_1_door
        self.library_name = LIBRARY_NAME
        self.category_name = SINK_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_2_Door_Sink(basic_cabinets.Sink_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_2_door
        self.library_name = LIBRARY_NAME
        self.category_name = SINK_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'BASE'
        
class PRODUCT_2_Door_2_False_Front_Sink(basic_cabinets.Sink_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_2_door
        self.library_name = LIBRARY_NAME
        self.category_name = SINK_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Double_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.exterior.use_false_front = True
        
class PRODUCT_2_Door_1_False_Front_Sink(basic_cabinets.Sink_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_2_door
        self.library_name = LIBRARY_NAME
        self.category_name = SINK_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Double_Door_Single_Drawer()
        self.exterior.door_type = 'BASE'   
        self.exterior.use_false_front = True     
        
class PRODUCT_1_Door_1_False_Front_Sink(basic_cabinets.Sink_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.width = props.width_1_door
        self.library_name = LIBRARY_NAME
        self.category_name = SINK_CATEGORY_NAME
        self.exterior = basic_cabinet_exteriors.Single_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.exterior.use_false_front = True
        
#---------PRODUCT: TALL CABINETS

class PRODUCT_1_Door_Tall(basic_cabinets.Tall_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.width = props.width_1_door
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'TALL'
        
class PRODUCT_2_Door_Tall(basic_cabinets.Tall_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = TALL_CATEGORY_NAME
        self.width = props.width_2_door
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'TALL'
        
#---------PRODUCT: UPPER CABINETS              
        
class PRODUCT_1_Door_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_1_door
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'UPPER'
        
class PRODUCT_Stacked_1_Door_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_1_door
        self.exterior = basic_cabinet_exteriors.Single_Door_Double_Stack()
        self.exterior.door_type = 'UPPER'        
        
class PRODUCT_2_Door_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_2_door
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'UPPER'
        
class PRODUCT_Stacked_2_Door_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_2_door
        self.exterior = basic_cabinet_exteriors.Double_Door_Double_Stack()
        self.exterior.door_type = 'UPPER'        
        
class PRODUCT_1_Door_Flip_Up_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_1_door
        self.exterior = basic_cabinet_exteriors.Flip_Up_Door()
        self.exterior.door_type = 'UPPER'
        
class PRODUCT_Stacked_1_Door_Flip_Up_Upper(basic_cabinets.Upper_Standard):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = UPPER_CATEGORY_NAME
        self.width = props.width_1_door
        self.exterior = basic_cabinet_exteriors.Flip_Up_Door_Double_Stack()
        self.exterior.door_type = 'UPPER'
        
#---------PRODUCT: INSIDE CORNER CABINETS        
        
class PRODUCT_Base_Pie_Cut_Corner(basic_cabinets.Base_Inside_Corner):
    
    def __init__(self):
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.pie_cut = True
        self.exterior = basic_cabinet_exteriors.Pie_Cut_Doors()
        self.exterior.door_type = 'BASE'

class PRODUCT_Upper_Pie_Cut_Corner(basic_cabinets.Upper_Inside_Corner):
    
    def __init__(self):
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = INSIDE_CORNER_CATEGORY_NAME
        self.pie_cut = True
        self.exterior = basic_cabinet_exteriors.Pie_Cut_Doors()
        self.exterior.door_type = 'UPPER'

#TODO: Create Diagonal Inserts. Need ro researh how door overlays work
# class PRODUCT_Base_Diagonal_Corner(basic_cabinets.Base_Inside_Corner):
#     
#     def __init__(self):
#         super().__init__()
#         self.library_name = LIBRARY_NAME
#         self.category_name = INSIDE_CORNER_CATEGORY_NAME
#         self.pie_cut = False
#         self.exterior = basic_cabinet_exteriors.Double_Door()
#         self.exterior.door_type = 'BASE'
# 
# class PRODUCT_Upper_Diagonal_Corner(basic_cabinets.Upper_Inside_Corner):
#     
#     def __init__(self):
#         super().__init__()
#         self.library_name = LIBRARY_NAME
#         self.category_name = INSIDE_CORNER_CATEGORY_NAME
#         self.pie_cut = False
#         self.exterior = basic_cabinet_exteriors.Diagonal_Single_Door()
#         self.exterior.door_type = 'UPPER'

#---------PRODUCT: BLIND CORNER CABINETS

class PRODUCT_1_Door_Blind_Left_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   
        
class PRODUCT_1_Door_Blind_Right_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   
        
class PRODUCT_2_Door_Blind_Left_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   
        
class PRODUCT_2_Door_Blind_Right_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'BASE'     
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}         
        
class PRODUCT_1_Door_1_Drawer_Blind_Left_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Single_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   
        
class PRODUCT_1_Door_1_Drawer_Blind_Right_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Single_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}           
        
class PRODUCT_2_Door_2_Drawer_Blind_Left_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Double_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   

class PRODUCT_2_Door_2_Drawer_Blind_Right_Corner_Base(basic_cabinets.Base_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Double_Door_Drawer()
        self.exterior.door_type = 'BASE'
        self.prompts = {'Blind Panel Width':props.base_cabinet_depth}   
        
class PRODUCT_1_Door_Blind_Left_Corner_Tall(basic_cabinets.Tall_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'TALL'
        self.prompts = {'Blind Panel Width':props.tall_cabinet_depth}   
        
class PRODUCT_1_Door_Blind_Right_Corner_Tall(basic_cabinets.Tall_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'TALL'   
        self.prompts = {'Blind Panel Width':props.tall_cabinet_depth}        
        
class PRODUCT_2_Door_Blind_Left_Corner_Tall(basic_cabinets.Tall_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'TALL'
        self.prompts = {'Blind Panel Width':props.tall_cabinet_depth}   
        
class PRODUCT_2_Door_Blind_Right_Corner_Tall(basic_cabinets.Tall_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'TALL'    
        self.prompts = {'Blind Panel Width':props.tall_cabinet_depth}       
        
class PRODUCT_1_Door_Blind_Left_Corner_Upper(basic_cabinets.Upper_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'UPPER'
        self.prompts = {'Blind Panel Width':props.upper_cabinet_depth}
        
class PRODUCT_1_Door_Blind_Right_Corner_Upper(basic_cabinets.Upper_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Single_Door()
        self.exterior.door_type = 'UPPER'  
        self.prompts = {'Blind Panel Width':props.upper_cabinet_depth}      
        
class PRODUCT_2_Door_Blind_Left_Corner_Upper(basic_cabinets.Upper_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Left"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'UPPER'
        self.prompts = {'Blind Panel Width':props.upper_cabinet_depth}
        
class PRODUCT_2_Door_Blind_Right_Corner_Upper(basic_cabinets.Upper_Blind):
    
    def __init__(self):
        props = get_props()
        super().__init__()
        self.library_name = LIBRARY_NAME
        self.category_name = BLIND_CORNER_CATEGORY_NAME
        self.blind_side = "Right"
        self.exterior = basic_cabinet_exteriors.Double_Door()
        self.exterior.door_type = 'UPPER'
        self.prompts = {'Blind Panel Width':props.upper_cabinet_depth}
        