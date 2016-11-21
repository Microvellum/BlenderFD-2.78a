"""
Microvellum 
Interiors
Stores the logic and insert defs for all interior components for cabinets and closets.
Shelves, Dividers, Divisions, Rollouts, Wire Baskets, Hanging Rods
"""

import bpy
from mv import utils, unit, fd_types
from os import path

ROOT_PATH = path.join(path.dirname(__file__),"Cabinet Assemblies")

SHELF = path.join(ROOT_PATH,"Cut Parts","Part with Edgebanding.blend")

SHELF_SETBACK = unit.inch(.25)

#---------ASSEMBLY INSTRUCTIONS
    
class Simple_Shelves(fd_types.Assembly):
    
    library_name = "Cabinet Interiors"
    type_assembly = "INSERT"
    placement_type = "INTERIOR"
    property_id = "interiors.shelf_prompt" #TODO: Create Prompts Page
    mirror_y = False
    
    carcass_type = "" # {Base, Tall, Upper, Sink, Suspended}
    open_name = ""
    shelf_qty = 1
    add_adjustable_shelves = True
    add_fixed_shelves = False
    
    def add_common_prompts(self):
        self.add_tab(name='Interior Options',tab_type='VISIBLE')
        self.add_tab(name='Formulas',tab_type='HIDDEN')

        self.add_prompt(name="Edgebanding Thickness",
                        prompt_type='DISTANCE',
                        value=unit.inch(.75),
                        tab_index=1)
    
        sgi = self.get_var('cabinetlib.spec_group_index','sgi')
    
        self.prompt('Edgebanding Thickness','EDGE_THICKNESS(sgi,"Cabinet_Interior_Edges' + self.open_name + '")',[sgi])
    
    def add_adj_prompts(self):
        self.add_prompt(name="Shelf Qty",
                        prompt_type='QUANTITY',
                        value=self.shelf_qty,
                        tab_index=0)
        
        self.add_prompt(name="Shelf Setback",
                        prompt_type='DISTANCE',
                        value=SHELF_SETBACK,
                        tab_index=0)

        sgi = self.get_var('cabinetlib.spec_group_index','sgi')

        self.prompt('Adjustable Shelf Thickness','THICKNESS(sgi,"Cabinet_Shelf' + self.open_name + '")',[sgi])

    def add_shelves(self):
        Width = self.get_var('dim_x','Width')
        Height = self.get_var('dim_z','Height')
        Depth = self.get_var('dim_y','Depth')
        Shelf_Qty = self.get_var("Shelf Qty")
        Shelf_Setback = self.get_var("Shelf Setback")
        Adjustable_Shelf_Thickness = self.get_var("Adjustable Shelf Thickness")

        adj_shelf = self.add_assembly(SHELF)
        adj_shelf.set_name("Adjustable Shelf")
        adj_shelf.x_loc(value=0)
        adj_shelf.y_loc('Depth',[Depth])
        adj_shelf.z_loc('((Height-(Adjustable_Shelf_Thickness*Shelf_Qty))/(Shelf_Qty+1))',[Height,Adjustable_Shelf_Thickness,Shelf_Qty])
        adj_shelf.x_rot(value = 0)
        adj_shelf.y_rot(value = 0)
        adj_shelf.z_rot(value = 0)
        adj_shelf.x_dim('Width',[Width])
        adj_shelf.y_dim('-Depth+Shelf_Setback',[Depth,Shelf_Setback])
        adj_shelf.z_dim('Adjustable_Shelf_Thickness',[Adjustable_Shelf_Thickness])
        adj_shelf.prompt('Hide','IF(Shelf_Qty==0,True,False)',[Shelf_Qty])
        adj_shelf.cutpart("Cabinet_Shelf")
        adj_shelf.edgebanding('Cabinet_Interior_Edges',l1 = True, w1 = True, l2 = True, w2 = True)

    def draw(self):
        self.create_assembly()
        
        self.add_common_prompts()
        self.add_adj_prompts()
        self.add_adjustable_shelves()

        self.update()    
