"""
Microvellum 
Cabinets
Stores the logic for the different types of cabinets available in the Face Frame and 
Frameless library. Only controls how the different inserts are combined to assemble a cabinet.
No construction or machining information is stored here.
TODO: Create Face Frame Transition, Create Face Frame Outside Corner
"""

import bpy
from mv import unit, fd_types, utils
from . import cabinet_countertops
from os import path

#ASSEMBLIES
ROOT_DIR = path.dirname(__file__)
CARCASS_DIR = path.join(ROOT_DIR,"Cabinet Assemblies","Basic Carcasses")
SIMPLE_CARCASS = path.join(CARCASS_DIR,"Simple Carcass.blend")
SINK_CARCASS = path.join(CARCASS_DIR,"Sink Carcass.blend")
PIE_CUT_CORNER_CARCASS = path.join(CARCASS_DIR,"Corner Carcass.blend")
DIAGONAL_CORNER_CARCASS = path.join(CARCASS_DIR,"Diagonal Corner Carcass.blend")
PIE_CUT_BASE_ASSEMBLY = path.join(CARCASS_DIR,"Base Corner Assembly.blend")
DIAGONAL_BASE_ASSEMBLY = path.join(CARCASS_DIR,"Diagonal Base Assembly.blend")
BASE_ASSEMBLY = path.join(CARCASS_DIR,"Base Assembly.blend")
CUTPARTS_DIR = path.join(ROOT_DIR,"Cabinet Assemblies","Cut Parts")
PART_WITH_EDGEBANDING = path.join(CUTPARTS_DIR,"Part with Edgebanding.blend")

#PROMPT DEFAULTS
TOE_KICK_HEIGHT = unit.inch(4)
TOE_KICK_SETBACK = unit.inch(3.25)
WIDTH_1_DOOR = unit.inch(18)
BASE_CABINET_HEIGHT = unit.inch(34)
BASE_CABINET_DEPTH = unit.inch(23)

#MATERIAL SLOT NAMES
EXTERIOR = "Exterior"
INTERIOR = "Interior"
EDGES = "Edges"
LEFT_EXTERIOR = "Left_Exterior"
RIGHT_EXTERIOR = "Right_Exterior"

#POINTER_NAMES
EXPOSED_EXTERIOR_SURFACE = "Exposed_Exterior_Surface"
EXPOSED_INTERIOR_SURFACE = "Exposed_Interior_Surface"
SEMI_EXPOSED_SURFACE = "Semi_Exposed_Surface"
EXPOSED_EXTERIOR_EDGE = "Exposed_Exterior_Edge"
EXPOSED_INTERIOR_EDGE = "Exposed_Interior_Edge"
SEMI_EXPOSED_EDGE = "Semi_Exposed_Edge"
CONCEALED_SURFACE = "Concealed_Surface"
CONCEALED_EDGE = "Concealed_Edge"

def update_product_materials(product):
    left_fin_end = product.get_prompt('Left Fin End')
    right_fin_end = product.get_prompt('Right Fin End')
    for child in product.obj_bp.children:
        update_assembly_materials(child, left_fin_end.value(), right_fin_end.value())

def update_assembly_materials(obj_bp,finish_left,finish_right):
    for slot in obj_bp.cabinetlib.material_slots:
        if slot.name == EXTERIOR:
            slot.pointer_name = EXPOSED_EXTERIOR_SURFACE
            
        if slot.name == INTERIOR:
            slot.pointer_name = EXPOSED_EXTERIOR_SURFACE
            
        if slot.name == EDGES:
            slot.pointer_name = EXPOSED_EXTERIOR_SURFACE
            
        if slot.name == LEFT_EXTERIOR:
            slot.pointer_name = EXPOSED_EXTERIOR_SURFACE if finish_left else CONCEALED_SURFACE
            
        if slot.name == RIGHT_EXTERIOR:
            slot.pointer_name = EXPOSED_EXTERIOR_SURFACE if finish_right else CONCEALED_SURFACE
        
    for child in obj_bp.children:
        update_assembly_materials(child,finish_left,finish_right)
        
    utils.assign_materials_from_pointers(obj_bp)

def add_product_width_dimension(product):
    Product_Width = product.get_var('dim_x','Product_Width')
    
    vdim_x = fd_types.Dimension()
    vdim_x.parent(product.obj_bp)
    if product.mirror_z:
        vdim_x.start_z(value = unit.inch(5))
    else:
        vdim_x.start_z(value = -unit.inch(5))
    if product.carcass.carcass_type == 'Upper':
        vdim_x.start_y(value = unit.inch(8))
    else:
        vdim_x.start_y(value = unit.inch(3))
    vdim_x.end_x('Product_Width',[Product_Width])
    
def add_countertop(product):
    product.add_prompt(name="Add Backsplash",prompt_type='CHECKBOX',value=True,tab_index=0)
    product.add_prompt(name="Add Left Backsplash",prompt_type='CHECKBOX',value=False,tab_index=0)
    product.add_prompt(name="Add Right Backsplash",prompt_type='CHECKBOX',value=False,tab_index=0)
    product.add_prompt(name="Side Splash Setback",prompt_type='DISTANCE',value=unit.inch(2.25),tab_index=0)
    product.add_prompt(name="Countertop Overhang Front",prompt_type='DISTANCE',value=unit.inch(1),tab_index=0)
    product.add_prompt(name="Countertop Overhang Back",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    product.add_prompt(name="Countertop Overhang Left",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    product.add_prompt(name="Countertop Overhang Right",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    Countertop_Overhang_Front = product.get_var('Countertop Overhang Front')
    Countertop_Overhang_Left = product.get_var('Countertop Overhang Left')
    Countertop_Overhang_Right = product.get_var('Countertop Overhang Right')
    Countertop_Overhang_Back = product.get_var('Countertop Overhang Back')
    Left_Side_Wall_Filler = product.get_var('Left Side Wall Filler')
    Right_Side_Wall_Filler = product.get_var('Right Side Wall Filler')
    Add_Backsplash = product.get_var('Add Backsplash')
    Add_Left_Backsplash = product.get_var('Add Left Backsplash')
    Add_Right_Backsplash = product.get_var('Add Right Backsplash')
    Side_Splash_Setback = product.get_var('Side Splash Setback')
    
    Width = product.get_var("dim_x","Width")
    Height = product.get_var("dim_z","Height")
    Depth = product.get_var("dim_y","Depth")
    
    ctop = cabinet_countertops.PRODUCT_Straight_Countertop()
    ctop.draw()
    ctop.obj_bp.mv.type_group = 'INSERT'
    ctop.obj_bp.parent = product.obj_bp
    ctop.x_loc('-Countertop_Overhang_Left-Left_Side_Wall_Filler',[Countertop_Overhang_Left,Left_Side_Wall_Filler])
    ctop.y_loc('Countertop_Overhang_Back',[Countertop_Overhang_Back])
    ctop.z_loc('Height',[Height])
    ctop.x_rot(value = 0)
    ctop.y_rot(value = 0)
    ctop.z_rot(value = 0)
    ctop.x_dim('Width+Countertop_Overhang_Left+Countertop_Overhang_Right+Left_Side_Wall_Filler+Right_Side_Wall_Filler',
               [Width,Countertop_Overhang_Left,Countertop_Overhang_Right,Left_Side_Wall_Filler,Right_Side_Wall_Filler])
    ctop.y_dim('Depth-Countertop_Overhang_Front-Countertop_Overhang_Back',[Depth,Countertop_Overhang_Front,Countertop_Overhang_Back])
    ctop.z_dim(value = unit.inch(4))
    ctop.prompt('Add Backsplash','Add_Backsplash',[Add_Backsplash])
    ctop.prompt('Add Left Backsplash','Add_Left_Backsplash',[Add_Left_Backsplash])
    ctop.prompt('Add Right Backsplash','Add_Right_Backsplash',[Add_Right_Backsplash])
    ctop.prompt('Side Splash Setback','Side_Splash_Setback',[Side_Splash_Setback])
    return ctop
    
def add_corner_countertop(product,pie_cut=True):
    product.add_prompt(name="Countertop Overhang Front",prompt_type='DISTANCE',value=unit.inch(1),tab_index=0)
    product.add_prompt(name="Countertop Overhang Left Back",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    product.add_prompt(name="Countertop Overhang Right Back",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    product.add_prompt(name="Countertop Overhang Left",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    product.add_prompt(name="Countertop Overhang Right",prompt_type='DISTANCE',value=unit.inch(0),tab_index=0)
    Countertop_Overhang_Front = product.get_var('Countertop Overhang Front')
    Countertop_Overhang_Left = product.get_var('Countertop Overhang Left')
    Countertop_Overhang_Right = product.get_var('Countertop Overhang Right')
    Countertop_Overhang_Left_Back = product.get_var('Countertop Overhang Left Back')
    Countertop_Overhang_Right_Back = product.get_var('Countertop Overhang Right Back')
    Left_Side_Wall_Filler = product.get_var('Left Side Wall Filler')
    Right_Side_Wall_Filler = product.get_var('Right Side Wall Filler')
    Left_Cabinet_Depth = product.get_var('Left Cabinet Depth')
    Right_Cabinet_Depth = product.get_var('Right Cabinet Depth')
    
    Width = product.get_var("dim_x","Width")
    Height = product.get_var("dim_z","Height")
    Depth = product.get_var("dim_y","Depth")
    
    if pie_cut:
        ctop = cabinet_countertops.PRODUCT_Notched_Corner_Countertop()
    else:
        ctop = cabinet_countertops.PRODUCT_Diagonal_Corner_Countertop()
    ctop.draw()
    ctop.obj_bp.mv.type_group = 'INSERT'
    ctop.obj_bp.parent = product.obj_bp
    ctop.x_loc('-Countertop_Overhang_Left_Back',[Countertop_Overhang_Left_Back])
    ctop.y_loc('Countertop_Overhang_Right_Back',[Countertop_Overhang_Right_Back])
    ctop.z_loc('Height',[Height])
    ctop.x_rot(value = 0)
    ctop.y_rot(value = 0)
    ctop.z_rot(value = 0)
    ctop.x_dim('Width+Countertop_Overhang_Left_Back+Countertop_Overhang_Right+Right_Side_Wall_Filler',
               [Width,Countertop_Overhang_Left_Back,Countertop_Overhang_Right,Right_Side_Wall_Filler])
    ctop.y_dim('Depth-Countertop_Overhang_Right_Back-Countertop_Overhang_Left-Left_Side_Wall_Filler',
               [Depth,Countertop_Overhang_Right_Back,Countertop_Overhang_Left,Left_Side_Wall_Filler])
    ctop.z_dim(value = unit.inch(4))
    ctop.prompt('Left Side Depth',"Left_Cabinet_Depth+Countertop_Overhang_Front+Countertop_Overhang_Left_Back",[Left_Cabinet_Depth,Countertop_Overhang_Front,Countertop_Overhang_Left_Back])
    ctop.prompt('Right Side Depth',"Right_Cabinet_Depth+Countertop_Overhang_Front+Countertop_Overhang_Right_Back",[Right_Cabinet_Depth,Countertop_Overhang_Front,Countertop_Overhang_Right_Back])
    return ctop
    
def create_cabinet(product):
    product.create_assembly()
    product.obj_bp.lm_basic_cabinets.is_cabinet = True
    product.obj_bp.lm_basic_cabinets.cabinet_shape = 'RECTANGLE'
    product.add_tab(name='Carcass Options',tab_type='VISIBLE')
    product.add_tab(name='Formulas',tab_type='HIDDEN')
    product.add_prompt(name="Material_Thickness",prompt_type='DISTANCE',value= unit.inch(.75),lock=True,tab_index=1)
    
def add_carcass_with_base_assembly(product,use_sink_carcass=False):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    
    Toe_Kick_Height = product.get_var('Toe Kick Height')  
    Toe_Kick_Setback = product.get_var('Toe Kick Setback')  
    Base_Inset_Front = product.get_var('Base Inset Front')  
    Base_Inset_Rear = product.get_var('Base Inset Rear')  
    Base_Inset_Left = product.get_var('Base Inset Left')  
    Base_Inset_Right = product.get_var('Base Inset Right')  
    
    carcass = product.add_assembly(SINK_CARCASS if use_sink_carcass else SIMPLE_CARCASS)
    carcass.x_loc(value = 0)
    carcass.y_loc(value = 0)
    carcass.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    carcass.x_rot(value = 0)
    carcass.y_rot(value = 0)
    carcass.z_rot(value = 0)
    carcass.x_dim('Product_Width',[Product_Width])
    carcass.y_dim('Product_Depth',[Product_Depth])
    carcass.z_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    carcass.set_material_pointers(EXPOSED_EXTERIOR_SURFACE,EXTERIOR)    
    carcass.set_material_pointers(EXPOSED_INTERIOR_SURFACE,INTERIOR)  
    carcass.set_material_pointers(CONCEALED_SURFACE,LEFT_EXTERIOR)  
    carcass.set_material_pointers(CONCEALED_SURFACE,RIGHT_EXTERIOR)  
    carcass.set_material_pointers(EXPOSED_EXTERIOR_EDGE,EDGES)  
    
    base_assembly = product.add_assembly(BASE_ASSEMBLY)
    base_assembly.x_loc('IF(Base_Inset_Left,Toe_Kick_Setback,0)',[Base_Inset_Left,Toe_Kick_Setback])
    base_assembly.y_loc('IF(Base_Inset_Rear,-Toe_Kick_Setback,0)',[Base_Inset_Rear,Toe_Kick_Setback])
    base_assembly.z_loc(value = 0)
    base_assembly.x_rot(value = 0)
    base_assembly.y_rot(value = 0)
    base_assembly.z_rot(value = 0)
    base_assembly.x_dim('Product_Width-IF(Base_Inset_Left,Toe_Kick_Setback,0)-IF(Base_Inset_Right,Toe_Kick_Setback,0)',[Product_Width,Base_Inset_Left,Base_Inset_Right,Toe_Kick_Setback])
    base_assembly.y_dim('Product_Depth+IF(Base_Inset_Front,Toe_Kick_Setback,0)+IF(Base_Inset_Rear,Toe_Kick_Setback,0)',[Product_Depth,Base_Inset_Front,Base_Inset_Rear,Toe_Kick_Setback])
    base_assembly.z_dim('Toe_Kick_Height',[Toe_Kick_Height])
    base_assembly.material("Exposed_Exterior_Surface")
    base_assembly.set_material_pointers(EXPOSED_EXTERIOR_SURFACE,EXTERIOR)
    base_assembly.set_material_pointers(CONCEALED_SURFACE,LEFT_EXTERIOR)
    base_assembly.set_material_pointers(CONCEALED_SURFACE,RIGHT_EXTERIOR)
    
def add_corner_carcass_with_base_assembly(product,cabinet_type="Base",pie_cut=True):
    product.add_prompt(name="Left Cabinet Depth",prompt_type='DISTANCE',value=unit.inch(24),tab_index=0)
    product.add_prompt(name="Right Cabinet Depth",prompt_type='DISTANCE',value=unit.inch(24),tab_index=0)
    product.add_prompt(name="Base Inset Rear Left",prompt_type='CHECKBOX',value= False,tab_index=0)
    product.add_prompt(name="Base Inset Rear Right",prompt_type='CHECKBOX',value= False,tab_index=0)
    
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    
    Toe_Kick_Height = product.get_var('Toe Kick Height')  
    Toe_Kick_Setback = product.get_var('Toe Kick Setback')  
    Base_Inset_Front = product.get_var('Base Inset Front')  
    Base_Inset_Left = product.get_var('Base Inset Left')  
    Base_Inset_Right = product.get_var('Base Inset Right')  
    Left_Cabinet_Depth = product.get_var('Left Cabinet Depth')  
    Right_Cabinet_Depth = product.get_var('Right Cabinet Depth')  
    Base_Inset_Rear_Left = product.get_var('Base Inset Rear Left')  
    Base_Inset_Rear_Right = product.get_var('Base Inset Rear Right')  
    
    carcass = product.add_assembly(PIE_CUT_CORNER_CARCASS if pie_cut else DIAGONAL_CORNER_CARCASS)
    carcass.x_loc(value = 0)
    carcass.y_loc(value = 0)
    if cabinet_type == "Base":
        carcass.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    if cabinet_type == "Upper":
        carcass.z_loc('Product_Height',[Product_Height])
    carcass.x_rot(value = 0)
    carcass.y_rot(value = 0)
    carcass.z_rot(value = 0)
    carcass.x_dim('Product_Width',[Product_Width])
    carcass.y_dim('Product_Depth',[Product_Depth])
    if cabinet_type == "Base":
        carcass.z_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    if cabinet_type == "Upper":
        carcass.z_dim('fabs(Product_Height)',[Product_Height])
    carcass.set_material_pointers(EXPOSED_EXTERIOR_SURFACE,EXTERIOR)
    carcass.set_material_pointers(EXPOSED_INTERIOR_SURFACE,INTERIOR)
    carcass.set_material_pointers(CONCEALED_SURFACE,LEFT_EXTERIOR)
    carcass.set_material_pointers(CONCEALED_SURFACE,RIGHT_EXTERIOR)
    carcass.set_material_pointers(EXPOSED_EXTERIOR_EDGE,EDGES)
    carcass.prompt('Left Depth','Left_Cabinet_Depth',[Left_Cabinet_Depth])
    carcass.prompt('Right Depth','Right_Cabinet_Depth',[Right_Cabinet_Depth])
    
    if cabinet_type == "Base":
        base_assembly = product.add_assembly(PIE_CUT_BASE_ASSEMBLY if pie_cut else DIAGONAL_BASE_ASSEMBLY)
        base_assembly.x_loc('IF(Base_Inset_Rear_Left,Toe_Kick_Setback,0)',[Base_Inset_Rear_Left,Toe_Kick_Setback])
        base_assembly.y_loc('IF(Base_Inset_Rear_Right,-Toe_Kick_Setback,0)',[Base_Inset_Rear_Right,Toe_Kick_Setback])
        base_assembly.z_loc(value = 0)
        base_assembly.x_rot(value = 0)
        base_assembly.y_rot(value = 0)
        base_assembly.z_rot(value = 0)
        base_assembly.x_dim('Product_Width-IF(Base_Inset_Rear_Left,Toe_Kick_Setback,0)-IF(Base_Inset_Right,Toe_Kick_Setback,0)',[Product_Width,Base_Inset_Rear_Left,Base_Inset_Right,Toe_Kick_Setback])
        base_assembly.y_dim('Product_Depth+IF(Base_Inset_Rear_Right,Toe_Kick_Setback,0)+IF(Base_Inset_Left,Toe_Kick_Setback,0)',[Product_Depth,Base_Inset_Rear_Right,Base_Inset_Left,Toe_Kick_Setback])
        base_assembly.z_dim('Toe_Kick_Height',[Toe_Kick_Height])
        base_assembly.material("Exposed_Exterior_Surface")
        base_assembly.set_material_pointers(EXPOSED_EXTERIOR_SURFACE,EXTERIOR)
        base_assembly.set_material_pointers(CONCEALED_SURFACE,LEFT_EXTERIOR)
        base_assembly.set_material_pointers(CONCEALED_SURFACE,RIGHT_EXTERIOR)
        base_assembly.prompt('Left Depth','Left_Cabinet_Depth-IF(Base_Inset_Front,Toe_Kick_Setback,0)-IF(Base_Inset_Rear_Left,Toe_Kick_Setback,0)',[Left_Cabinet_Depth,Base_Inset_Front,Base_Inset_Rear_Left,Toe_Kick_Setback])
        base_assembly.prompt('Right Depth','Right_Cabinet_Depth-IF(Base_Inset_Front,Toe_Kick_Setback,0)-IF(Base_Inset_Rear_Right,Toe_Kick_Setback,0)',[Right_Cabinet_Depth,Base_Inset_Front,Base_Inset_Rear_Right,Toe_Kick_Setback])
    
def add_upper_carcass(product):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    

    carcass = product.add_assembly(SIMPLE_CARCASS)
    carcass.x_loc(value = 0)
    carcass.y_loc(value = 0)
    carcass.z_loc('Product_Height',[Product_Height])
    carcass.x_rot(value = 0)
    carcass.y_rot(value = 0)
    carcass.z_rot(value = 0)
    carcass.x_dim('Product_Width',[Product_Width])
    carcass.y_dim('Product_Depth',[Product_Depth])
    carcass.z_dim('fabs(Product_Height)',[Product_Height])
    carcass.set_material_pointers(EXPOSED_EXTERIOR_SURFACE,EXTERIOR)    
    carcass.set_material_pointers(EXPOSED_INTERIOR_SURFACE,INTERIOR)  
    carcass.set_material_pointers(CONCEALED_SURFACE,LEFT_EXTERIOR)  
    carcass.set_material_pointers(CONCEALED_SURFACE,RIGHT_EXTERIOR)  
    carcass.set_material_pointers(EXPOSED_EXTERIOR_EDGE,EDGES)      
    
def add_fillers(product):
    product.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value= 0,tab_index=0,export=True)
    product.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value= 0,tab_index=0,export=True)
    
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    
    Toe_Kick_Height = product.get_var('Toe Kick Height')  
    Left_Side_Wall_Filler = product.get_var('Left Side Wall Filler')  
    Right_Side_Wall_Filler = product.get_var('Right Side Wall Filler') 
    
    left_filler = product.add_assembly(PART_WITH_EDGEBANDING)
    left_filler.set_name("Left Filler")
    left_filler.x_loc('-Left_Side_Wall_Filler',[Left_Side_Wall_Filler])
    left_filler.y_loc('Product_Depth',[Product_Depth])
    left_filler.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    left_filler.x_rot(value = 0)
    left_filler.y_rot(value = -90)
    left_filler.z_rot(value = -90)
    left_filler.x_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    left_filler.y_dim('Left_Side_Wall_Filler',[Left_Side_Wall_Filler])
    left_filler.z_dim(value = unit.inch(.75))
    left_filler.cutpart("Cabinet_Filler")
    left_filler.prompt('Hide','IF(Left_Side_Wall_Filler==0,True,False)',[Left_Side_Wall_Filler])
    
    right_filler = product.add_assembly(PART_WITH_EDGEBANDING)
    right_filler.set_name("Right Filler")
    right_filler.x_loc('Product_Width',[Product_Width])
    right_filler.y_loc('Product_Depth',[Product_Depth])
    right_filler.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    right_filler.x_rot(value = 0)
    right_filler.y_rot(value = -90)
    right_filler.z_rot(value = -90)
    right_filler.x_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    right_filler.y_dim('Right_Side_Wall_Filler',[Right_Side_Wall_Filler])
    right_filler.z_dim(value = unit.inch(.75))
    right_filler.cutpart("Cabinet_Filler")
    right_filler.prompt('Hide','IF(Right_Side_Wall_Filler==0,True,False)',[Right_Side_Wall_Filler])    
    
def add_corner_fillers(product):
    product.add_prompt(name="Left Side Wall Filler",prompt_type='DISTANCE',value= 0,tab_index=0,export=True)
    product.add_prompt(name="Right Side Wall Filler",prompt_type='DISTANCE',value= 0,tab_index=0,export=True)
    
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    
    Toe_Kick_Height = product.get_var('Toe Kick Height')  
    Left_Side_Wall_Filler = product.get_var('Left Side Wall Filler')  
    Right_Side_Wall_Filler = product.get_var('Right Side Wall Filler') 
    Left_Cabinet_Depth = product.get_var('Left Cabinet Depth')  
    Right_Cabinet_Depth = product.get_var('Right Cabinet Depth') 
    
    left_filler = product.add_assembly(PART_WITH_EDGEBANDING)
    left_filler.set_name("Left Filler")
    left_filler.x_loc('Left_Cabinet_Depth',[Left_Cabinet_Depth])
    left_filler.y_loc('Product_Depth-Left_Side_Wall_Filler',[Product_Depth,Left_Side_Wall_Filler])
    left_filler.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    left_filler.x_rot(value = 0)
    left_filler.y_rot(value = -90)
    left_filler.z_rot(value = 0)
    left_filler.x_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    left_filler.y_dim('Left_Side_Wall_Filler',[Left_Side_Wall_Filler])
    left_filler.z_dim(value = unit.inch(.75))
    left_filler.cutpart("Cabinet_Filler")
    left_filler.prompt('Hide','IF(Left_Side_Wall_Filler==0,True,False)',[Left_Side_Wall_Filler])
    
    right_filler = product.add_assembly(PART_WITH_EDGEBANDING)
    right_filler.set_name("Right Filler")
    right_filler.x_loc('Product_Width',[Product_Width])
    right_filler.y_loc('-Right_Cabinet_Depth',[Right_Cabinet_Depth])
    right_filler.z_loc('Toe_Kick_Height',[Toe_Kick_Height])
    right_filler.x_rot(value = 0)
    right_filler.y_rot(value = -90)
    right_filler.z_rot(value = -90)
    right_filler.x_dim('Product_Height-Toe_Kick_Height',[Product_Height,Toe_Kick_Height])
    right_filler.y_dim('Right_Side_Wall_Filler',[Right_Side_Wall_Filler])
    right_filler.z_dim(value = unit.inch(.75))
    right_filler.cutpart("Cabinet_Filler")
    right_filler.prompt('Hide','IF(Right_Side_Wall_Filler==0,True,False)',[Right_Side_Wall_Filler])       
    
def add_blind_panel(product,side="Left",cabinet_type="Base"):
    product.add_prompt(name="Blind Panel Width",prompt_type='DISTANCE',value=unit.inch(23),tab_index=1)
    product.add_prompt(name="Blind Panel Reveal",prompt_type='DISTANCE',value=unit.inch(3),tab_index=1)
    product.add_prompt(name="Blind Panel Thickness",prompt_type='DISTANCE',value=unit.inch(.75),tab_index=2)
    
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')    
    Toe_Kick_Height = product.get_var('Toe Kick Height')  
    Material_Thickness = product.get_var('Material_Thickness')
    Blind_Panel_Width = product.get_var('Blind Panel Width') 
    Blind_Panel_Reveal = product.get_var('Blind Panel Reveal') 
    
    blind_panel = product.add_assembly(PART_WITH_EDGEBANDING)
    blind_panel.set_name("Right Filler")
    if side == "Left":
        blind_panel.x_loc('Material_Thickness',[Material_Thickness])
    else:
        blind_panel.x_loc('Product_Width-Material_Thickness-Blind_Panel_Width-Blind_Panel_Reveal',
                          [Product_Width,Material_Thickness,Blind_Panel_Width,Blind_Panel_Reveal])
    blind_panel.y_loc('Product_Depth',[Product_Depth])
    if cabinet_type == "Base":
        blind_panel.z_loc('Toe_Kick_Height+Material_Thickness',[Toe_Kick_Height,Material_Thickness])
    if cabinet_type == "Upper":
        blind_panel.z_loc('Product_Height+Material_Thickness',[Product_Height,Material_Thickness])
    blind_panel.x_rot(value = 0)
    blind_panel.y_rot(value = -90)
    blind_panel.z_rot(value = -90)
    if cabinet_type == "Base":
        blind_panel.x_dim('Product_Height-Toe_Kick_Height-Material_Thickness*2',
                          [Product_Height,Toe_Kick_Height,Material_Thickness])
    if cabinet_type == "Upper":
        blind_panel.x_dim('fabs(Product_Height)-Material_Thickness*2',
                          [Product_Height,Material_Thickness])
    blind_panel.y_dim('Blind_Panel_Width+Blind_Panel_Reveal',[Blind_Panel_Width,Blind_Panel_Reveal])
    blind_panel.z_dim(value = unit.inch(.75))
    blind_panel.cutpart("Cabinet_Filler")
    
def add_fin_end_prompts(product):
    product.add_prompt(name="Left Fin End",prompt_type='CHECKBOX',value= False,tab_index=0,export=True)
    product.add_prompt(name="Right Fin End",prompt_type='CHECKBOX',value= False,tab_index=0,export=True)
    
def add_base_assembly_prompts(product):
    product.add_prompt(name="Toe Kick Height",prompt_type='DISTANCE',value= TOE_KICK_HEIGHT,tab_index=0,export=True)
    product.add_prompt(name="Toe Kick Setback",prompt_type='DISTANCE',value= TOE_KICK_SETBACK,tab_index=0,export=True)
    product.add_prompt(name="Base Inset Front",prompt_type='CHECKBOX',value= True,tab_index=0)
    product.add_prompt(name="Base Inset Rear",prompt_type='CHECKBOX',value= False,tab_index=0)
    product.add_prompt(name="Base Inset Left",prompt_type='CHECKBOX',value= False,tab_index=0)
    product.add_prompt(name="Base Inset Right",prompt_type='CHECKBOX',value= False,tab_index=0)
    
def add_exterior(product):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')
    Toe_Kick_Height = product.get_var('Toe Kick Height')
    Material_Thickness = product.get_var('Material_Thickness')
    
    product.exterior.draw()
    product.exterior.set_name("Exterior")
    product.exterior.obj_bp.parent = product.obj_bp
    product.exterior.x_loc('Material_Thickness',[Material_Thickness])
    product.exterior.y_loc('Product_Depth',[Product_Depth])
    product.exterior.z_loc('Toe_Kick_Height+Material_Thickness',[Toe_Kick_Height,Material_Thickness])
    product.exterior.x_rot(value = 0)
    product.exterior.y_rot(value = 0)
    product.exterior.z_rot(value = 0)
    product.exterior.x_dim('Product_Width-Material_Thickness*2',[Product_Width,Material_Thickness])
    product.exterior.y_dim('Product_Depth+Material_Thickness',[Product_Depth,Material_Thickness])
    product.exterior.z_dim('Product_Height-Toe_Kick_Height-Material_Thickness*2',[Product_Height,Toe_Kick_Height,Material_Thickness])
    
def add_upper_exterior(product):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')
    Material_Thickness = product.get_var('Material_Thickness')
    
    product.exterior.draw()
    product.exterior.set_name("Exterior")
    product.exterior.obj_bp.parent = product.obj_bp
    product.exterior.x_loc('Material_Thickness',[Material_Thickness])
    product.exterior.y_loc('Product_Depth',[Product_Depth])
    product.exterior.z_loc('Product_Height+Material_Thickness',[Product_Height,Material_Thickness])
    product.exterior.x_rot(value = 0)
    product.exterior.y_rot(value = 0)
    product.exterior.z_rot(value = 0)
    product.exterior.x_dim('Product_Width-Material_Thickness*2',[Product_Width,Material_Thickness])
    product.exterior.y_dim('Product_Depth+Material_Thickness',[Product_Depth,Material_Thickness])
    product.exterior.z_dim('fabs(Product_Height)-Material_Thickness*2',[Product_Height,Material_Thickness])

def add_blind_exterior(product,side="Left",cabinet_type="Base"):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')
    Material_Thickness = product.get_var('Material_Thickness')
    Blind_Panel_Width = product.get_var('Blind Panel Width') 
    Blind_Panel_Reveal = product.get_var('Blind Panel Reveal') 
    Toe_Kick_Height = product.get_var('Toe Kick Height')
    
    product.exterior.draw()
    product.exterior.set_name("Exterior")
    product.exterior.obj_bp.parent = product.obj_bp
    if side == "Left":
        product.exterior.x_loc('Material_Thickness+Blind_Panel_Width+Blind_Panel_Reveal',
                               [Material_Thickness,Blind_Panel_Width,Blind_Panel_Reveal])
    else:
        product.exterior.x_loc('Material_Thickness',[Material_Thickness])
    product.exterior.y_loc('Product_Depth',[Product_Depth])
    if cabinet_type == "Base":
        product.exterior.z_loc('Toe_Kick_Height+Material_Thickness',[Toe_Kick_Height,Material_Thickness])
    if cabinet_type == "Upper":
        product.exterior.z_loc('Product_Height+Material_Thickness',[Product_Height,Material_Thickness])
    product.exterior.x_rot(value = 0)
    product.exterior.y_rot(value = 0)
    product.exterior.z_rot(value = 0)
    product.exterior.x_dim('Product_Width-Blind_Panel_Width-Blind_Panel_Reveal-Material_Thickness*2',
                           [Product_Width,Blind_Panel_Width,Blind_Panel_Reveal,Material_Thickness])
    product.exterior.y_dim('Product_Depth+Material_Thickness',[Product_Depth,Material_Thickness])
    if cabinet_type == "Base":
        product.exterior.z_dim('Product_Height-Toe_Kick_Height-Material_Thickness*2',
                               [Product_Height,Toe_Kick_Height,Material_Thickness])
    if cabinet_type == "Upper":
        product.exterior.z_dim('fabs(Product_Height)-Material_Thickness*2',
                               [Product_Height,Toe_Kick_Height,Material_Thickness])
    
def add_inside_diagonal_exterior(product,carcass_type="Base"):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')
    Toe_Kick_Height = product.get_var('Toe Kick Height')
    Material_Thickness = product.get_var('Material_Thickness')
    Left_Cabinet_Depth = product.get_var('Left Cabinet Depth')  
    Right_Cabinet_Depth = product.get_var('Right Cabinet Depth') 
    
    product.exterior.draw()
    product.exterior.obj_bp.parent = product.obj_bp
    product.exterior.x_loc('Left_Cabinet_Depth',[Left_Cabinet_Depth])
    product.exterior.y_loc('Product_Depth',[Product_Depth])
    if carcass_type == "Base":
        product.exterior.z_loc('Toe_Kick_Height+Material_Thickness',[Toe_Kick_Height,Material_Thickness])
    if carcass_type == "Upper":
        product.exterior.z_loc('Product_Height+Material_Thickness',[Product_Height,Material_Thickness])
    product.exterior.x_rot(value = 0)
    product.exterior.y_rot(value = 0)

    product.exterior.z_rot('atan((fabs(Product_Depth)-Material_Thickness-Right_Cabinet_Depth)/(fabs(Product_Width)-Material_Thickness-Left_Cabinet_Depth))',
                           [Product_Depth,Material_Thickness,Right_Cabinet_Depth,Product_Width,Left_Cabinet_Depth])
#         product.exterior.x_dim('sqrt(((fabs(Product_Depth)-Material_Thickness-Right_Cabinet_Depth)**2)+((fabs(Product_Width)-Material_Thickness-Left_Cabinet_Depth)**2))',
#                                [Product_Depth,Material_Thickness,Right_Cabinet_Depth,Product_Width,Left_Cabinet_Depth])
    left_side = "(fabs(Product_Depth)-Right_Cabinet_Depth-Material_Thickness)**2"
    right_side = "(fabs(Product_Width)-Left_Cabinet_Depth-Material_Thickness)**2"
    product.exterior.x_dim('sqrt((' + left_side + ')+(' + right_side + '))',
                           [Product_Depth,Material_Thickness,Right_Cabinet_Depth,Product_Width,Left_Cabinet_Depth])
            
    product.exterior.y_dim('Product_Depth+Right_Cabinet_Depth+Material_Thickness',[Product_Depth,Right_Cabinet_Depth,Material_Thickness])
    if carcass_type == "Base":
        product.exterior.z_dim('fabs(Product_Height)-Toe_Kick_Height-(Material_Thickness*2)',[Product_Height,Toe_Kick_Height,Material_Thickness])
    if carcass_type == "Upper":
        product.exterior.z_dim('fabs(Product_Height)-(Material_Thickness*2)',[Product_Height,Material_Thickness])  
    
def add_inside_corner_exterior(product,carcass_type="Base"):
    Product_Width = product.get_var('dim_x','Product_Width')
    Product_Height = product.get_var('dim_z','Product_Height')
    Product_Depth = product.get_var('dim_y','Product_Depth')
    Toe_Kick_Height = product.get_var('Toe Kick Height')
    Material_Thickness = product.get_var('Material_Thickness')
    Left_Cabinet_Depth = product.get_var('Left Cabinet Depth')  
    Right_Cabinet_Depth = product.get_var('Right Cabinet Depth') 
    
    product.exterior.draw()
    product.exterior.obj_bp.parent = product.obj_bp
    product.exterior.x_loc('Left_Cabinet_Depth',[Left_Cabinet_Depth])
    product.exterior.y_loc('-Right_Cabinet_Depth',[Right_Cabinet_Depth])
    if carcass_type == "Base":
        product.exterior.z_loc('Toe_Kick_Height+Material_Thickness',[Toe_Kick_Height,Material_Thickness])
    if carcass_type == "Upper":
        product.exterior.z_loc('Product_Height+Material_Thickness',[Product_Height,Material_Thickness])
    product.exterior.x_rot(value = 0)
    product.exterior.y_rot(value = 0)
    product.exterior.z_rot(value = 0)    
    product.exterior.x_dim('Product_Width-Left_Cabinet_Depth-Material_Thickness',[Product_Width,Left_Cabinet_Depth,Material_Thickness])
    product.exterior.y_dim('Product_Depth+Right_Cabinet_Depth+Material_Thickness',[Product_Depth,Right_Cabinet_Depth,Material_Thickness])
    if carcass_type == "Base":
        product.exterior.z_dim('fabs(Product_Height)-Toe_Kick_Height-(Material_Thickness*2)',[Product_Height,Toe_Kick_Height,Material_Thickness])
    if carcass_type == "Upper":
        product.exterior.z_dim('fabs(Product_Height)-(Material_Thickness*2)',[Product_Height,Material_Thickness])  
    
class Base_Standard(fd_types.Assembly):
    """ Base Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    
    exterior = None
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.base_cabinet_height
        self.depth = g.base_cabinet_depth
        self.width = g.width_1_door    
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Base"
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_carcass_with_base_assembly(self)
        add_fillers(self)
        add_countertop(self)
        if self.exterior:
            add_exterior(self)
        
class Sink_Standard(fd_types.Assembly):
    """ Sink Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    
    exterior = None
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.base_cabinet_height
        self.depth = g.base_cabinet_depth
        self.width = g.width_1_door    
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Base"
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_carcass_with_base_assembly(self,use_sink_carcass=True)
        add_fillers(self)
        add_countertop(self)
        if self.exterior:
            add_exterior(self)        
        
class Tall_Standard(fd_types.Assembly):
    """ Tall Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    
    exterior = None
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.tall_cabinet_height
        self.depth = g.tall_cabinet_depth
        self.width = g.width_1_door    
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Tall"
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_carcass_with_base_assembly(self)
        add_fillers(self)
        if self.exterior:
            add_exterior(self)
        
class Upper_Standard(fd_types.Assembly):
    """ Upper Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    mirror_z = True
    
    exterior = None
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.upper_cabinet_height
        self.depth = g.upper_cabinet_depth
        self.width = g.width_1_door
        self.height_above_floor = g.height_above_floor    
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Upper"
        add_fin_end_prompts(self)
        add_upper_carcass(self)
        add_fillers(self)
        if self.exterior:
            add_upper_exterior(self)
        
class Base_Blind(fd_types.Assembly):
    """ Base Blind Cabinet
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    
    exterior = None
    
    blind_side = "Left"
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.base_cabinet_height
        self.depth = g.base_cabinet_depth
        self.width = g.base_width_blind
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Base"
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_carcass_with_base_assembly(self)
        add_blind_panel(self,self.blind_side)
        add_fillers(self)
        add_countertop(self)
        if self.exterior:
            add_blind_exterior(self,self.blind_side)
        
class Tall_Blind(fd_types.Assembly):
    """ Tall Blind Cabinet
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    
    exterior = None
    
    blind_side = "Left"
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.tall_cabinet_height
        self.depth = g.tall_cabinet_depth
        self.width = g.tall_width_blind    
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Tall"
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_carcass_with_base_assembly(self)
        add_blind_panel(self,self.blind_side)
        add_fillers(self)
        if self.exterior:
            add_blind_exterior(self,self.blind_side)        
        
class Upper_Blind(fd_types.Assembly):
    """ Upper Blind Cabinet
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    mirror_z = True
    
    exterior = None
    
    blind_side = "Left"
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.upper_cabinet_height
        self.depth = g.upper_cabinet_depth
        self.width = g.upper_width_blind    
        self.height_above_floor = g.height_above_floor
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Upper"
        add_fin_end_prompts(self)
        add_upper_carcass(self)
        add_blind_panel(self,self.blind_side,"Upper")
        add_fillers(self)
        if self.exterior:
            add_blind_exterior(self,self.blind_side,"Upper")             
        
class Base_Inside_Corner(fd_types.Assembly):
    """ Base Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    placement_type = "Corner"
    
    exterior = None
    
    pie_cut = True
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.base_cabinet_height
        self.depth = g.base_inside_corner_size
        self.width = g.base_inside_corner_size
        self.prompts = {'Left Cabinet Depth':g.base_cabinet_depth,
                        'Right Cabinet Depth':g.base_cabinet_depth}
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Base"
        self.obj_bp.lm_basic_cabinets.cabinet_shape = 'INSIDE_NOTCH' if self.pie_cut else 'INSIDE_DIAGONAL'
        add_fin_end_prompts(self)
        add_base_assembly_prompts(self)
        add_corner_carcass_with_base_assembly(self,"Base",self.pie_cut)
        add_corner_fillers(self)
        add_corner_countertop(self,self.pie_cut)
        if self.exterior:
            if self.pie_cut:
                add_inside_corner_exterior(self,"Base")
            else:
                add_inside_diagonal_exterior(self,"Base")
        
class Upper_Inside_Corner(fd_types.Assembly):
    """ Base Cabinet Standard
    """
    
    property_id = "cabinets.basic_cabinet_prompts"
    plan_id = "framelss_standard.draw_plan"
    update_id = "cabinet.update"
    type_assembly = "PRODUCT"
    mirror_y = True
    mirror_z = True
    placement_type = "Corner"
    
    exterior = None
    
    pie_cut = True
    
    def __init__(self):
        g = bpy.context.scene.lm_basic_cabinets.size_defaults
        self.height = g.upper_cabinet_height
        self.depth = g.upper_inside_corner_size
        self.width = g.upper_inside_corner_size
        self.height_above_floor = g.height_above_floor
        self.prompts = {'Left Cabinet Depth':g.upper_cabinet_depth,
                        'Right Cabinet Depth':g.upper_cabinet_depth}
    
    def draw(self):
        create_cabinet(self)
        self.obj_bp.lm_basic_cabinets.cabinet_type = "Upper"
        self.obj_bp.lm_basic_cabinets.cabinet_shape = 'INSIDE_NOTCH' if self.pie_cut else 'INSIDE_DIAGONAL'
        add_fin_end_prompts(self)
        add_corner_carcass_with_base_assembly(self,"Upper",self.pie_cut)
        add_corner_fillers(self)
        if self.exterior:
            add_inside_corner_exterior(self,"Upper")        
        
class PROMPTS_Basic_Cabinet_Prompts(fd_types.Prompts_Interface):
    bl_idname = "cabinets.basic_cabinet_prompts"
    bl_label = "Basic Cabinet Prompts"
    bl_options = {'UNDO'}
    
    object_name = bpy.props.StringProperty(name="Object Name",description="Stores the Base Point Object Name so the object can be retrieved from the database.")
    
    width = bpy.props.FloatProperty(name="Width",unit='LENGTH',precision=4)
    height = bpy.props.FloatProperty(name="Height",unit='LENGTH',precision=4)
    depth = bpy.props.FloatProperty(name="Depth",unit='LENGTH',precision=4)    
    
    product = None
    
    prompts = {}

    def check(self, context):
        self.update_product_size()
        update_product_materials(self.product)
        return True

    def execute(self, context):
        self.update_product_size()
        return {'FINISHED'}

    def add_prompt(self,prompt_name):
        prompt = self.product.get_prompt(prompt_name)
        if prompt:
            self.prompts[prompt_name] = prompt

    def invoke(self,context,event):
        self.product = self.get_product()
        self.add_prompt("Left Fin End")
        self.add_prompt("Right Fin End")
        self.add_prompt("Base Inset Front")
        self.add_prompt("Base Inset Rear")
        self.add_prompt("Base Inset Left")
        self.add_prompt("Base Inset Right")
        self.add_prompt("Left Side Wall Filler")
        self.add_prompt("Right Side Wall Filler")
        self.add_prompt("Toe Kick Height")
        self.add_prompt("Toe Kick Setback")
        self.add_prompt("Add Backsplash")
        self.add_prompt("Add Left Backsplash")
        self.add_prompt("Add Right Backsplash")
        self.add_prompt("Side Splash Setback")
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=utils.get_prop_dialog_width(500))
        
    def draw(self, context):
        layout = self.layout
        layout.label(self.product.obj_bp.mv.name_object)
        self.draw_product_size(layout)
        col = layout.column(align=True)
        
        box = col.box()
        row = box.row()
        row.label("Finished Ends:")
        if "Left Fin End" in self.prompts:
            prompt = self.prompts["Left Fin End"]
            row.prop(prompt,prompt.prompt_type,text=prompt.name)
            
        if "Right Fin End" in self.prompts:
            prompt = self.prompts["Right Fin End"]
            row.prop(prompt,prompt.prompt_type,text=prompt.name)
        
        box = col.box()
        row = box.row()
        row.label("Fillers:")
        if "Left Side Wall Filler" in self.prompts:
            prompt = self.prompts["Left Side Wall Filler"]
            row.prop(prompt,prompt.prompt_type,text="Left")
            
        if "Right Side Wall Filler" in self.prompts:
            prompt = self.prompts["Right Side Wall Filler"]
            row.prop(prompt,prompt.prompt_type,text="Right")
        
        box = col.box()
        row = box.row()
        row.label("Countertop:")
        if "Add Backsplash" in self.prompts:
            prompt = self.prompts["Add Backsplash"]
            row.prop(prompt,prompt.prompt_type,text="Back")
        if "Add Left Backsplash" in self.prompts:
            prompt = self.prompts["Add Left Backsplash"]
            row.prop(prompt,prompt.prompt_type,text="Left")        
        if "Add Right Backsplash" in self.prompts:
            prompt = self.prompts["Add Right Backsplash"]
            row.prop(prompt,prompt.prompt_type,text="Right") 
        if "Side Splash Setback" in self.prompts:
            prompt = self.prompts["Side Splash Setback"]
            row.prop(prompt,prompt.prompt_type,text="Setback")
        
        box = col.box()
        row = box.row()
        row.label("Base Assembly:")
        if "Base Inset Front" in self.prompts:
            prompt = self.prompts["Base Inset Front"]
            row.prop(prompt,prompt.prompt_type,text="Front")     
        
        if "Base Inset Rear" in self.prompts:
            prompt = self.prompts["Base Inset Rear"]
            row.prop(prompt,prompt.prompt_type,text="Rear")   
            
        if "Base Inset Left" in self.prompts:
            prompt = self.prompts["Base Inset Left"]
            row.prop(prompt,prompt.prompt_type,text="Left")   
            
        if "Base Inset Right" in self.prompts:
            prompt = self.prompts["Base Inset Right"]
            row.prop(prompt,prompt.prompt_type,text="Right")      

        row = box.row()
        row.label(" ")
        if "Toe Kick Height" in self.prompts:
            prompt = self.prompts["Toe Kick Height"]
            row.prop(prompt,prompt.prompt_type,text=prompt.name)   
            
        if "Toe Kick Setback" in self.prompts:
            prompt = self.prompts["Toe Kick Setback"]
            row.prop(prompt,prompt.prompt_type,text=prompt.name)               

bpy.utils.register_class(PROMPTS_Basic_Cabinet_Prompts)
