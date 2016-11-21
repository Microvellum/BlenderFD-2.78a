import bpy
import math
from mv import fd_types, unit, utils

class PANEL_Basic_Cabinet_Options(bpy.types.Panel):
    """Panel to Store all of the Cabinet Options"""
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Basic Cabinet Options"
    bl_category = "Fluid Designer"

    props = None

    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='BLANK1')

    def draw_exterior_defaults(self,layout):
        col = layout.column(align=True)
        
        box = col.box()
        box.label("Door & Drawer Defaults:")
        
        row = box.row(align=True)
        row.prop(self.props.exterior_defaults,"inset_door")
        row.prop(self.props.exterior_defaults,"no_pulls")
        
        if not self.props.exterior_defaults.no_pulls:
            box = col.box()
            box.label("Pull Placement:")
            
            row = box.row(align=True)
            row.label("Base Doors:")
            row.prop(self.props.exterior_defaults,"base_pull_location",text="From Top of Door")
            
            row = box.row(align=True)
            row.label("Tall Doors:")
            row.prop(self.props.exterior_defaults,"tall_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Upper Doors:")
            row.prop(self.props.exterior_defaults,"upper_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Distance From Edge:")
            row.prop(self.props.exterior_defaults,"pull_from_edge",text="")
            
            row = box.row(align=True)
            row.prop(self.props.exterior_defaults,"center_pulls_on_drawers")
    
            if not self.props.exterior_defaults.center_pulls_on_drawers:
                row.prop(self.props.exterior_defaults,"drawer_pull_from_top",text="Distance From Top")
        
        box = col.box()
        box.label("Door & Drawer Reveals:")
        
        if self.props.exterior_defaults.inset_door:
            row = box.row(align=True)
            row.label("Inset Reveals:")
            row.prop(self.props.exterior_defaults,"inset_reveal",text="")
        else:
            row = box.row(align=True)
            row.label("Standard Reveals:")
            row.prop(self.props.exterior_defaults,"left_reveal",text="Left")
            row.prop(self.props.exterior_defaults,"right_reveal",text="Right")
            
            row = box.row(align=True)
            row.label("Base Door Reveals:")
            row.prop(self.props.exterior_defaults,"base_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"base_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Tall Door Reveals:")
            row.prop(self.props.exterior_defaults,"tall_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"tall_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Upper Door Reveals:")
            row.prop(self.props.exterior_defaults,"upper_top_reveal",text="Top")
            row.prop(self.props.exterior_defaults,"upper_bottom_reveal",text="Bottom")
            
        row = box.row(align=True)
        row.label("Vertical Gap:")
        row.prop(self.props.exterior_defaults,"vertical_gap",text="")
    
        row = box.row(align=True)
        row.label("Door To Cabinet Gap:")
        row.prop(self.props.exterior_defaults,"door_to_cabinet_gap",text="")
    
    def draw_cabinet_sizes(self,layout):

        col = layout.column(align=True)

        box = col.box()
        box.label("Standard Frameless Cabinet Sizes:")
        
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self.props.size_defaults,"base_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"base_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Tall:")
        row.prop(self.props.size_defaults,"tall_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"tall_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self.props.size_defaults,"upper_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"upper_cabinet_depth",text="Depth")

        row = box.row(align=True)
        row.label("Sink:")
        row.prop(self.props.size_defaults,"sink_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"sink_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Suspended:")
        row.prop(self.props.size_defaults,"suspended_cabinet_height",text="Height")
        row.prop(self.props.size_defaults,"suspended_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("1 Door Wide:")
        row.prop(self.props.size_defaults,"width_1_door",text="Width")
        
        row = box.row(align=True)
        row.label("2 Door Wide:")
        row.prop(self.props.size_defaults,"width_2_door",text="Width")
        
        row = box.row(align=True)
        row.label("Drawer Stack Width:")
        row.prop(self.props.size_defaults,"width_drawer",text="Width")
        
        box = col.box()
        box.label("Blind Cabinet Widths:")
        
        row = box.row(align=True)
        row.label('Base:')
        row.prop(self.props.size_defaults,"base_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Tall:')
        row.prop(self.props.size_defaults,"tall_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Upper:')
        row.prop(self.props.size_defaults,"upper_width_blind",text="Width")
        
        box = col.box()
        box.label("Inside Corner Cabinet Sizes:")
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self.props.size_defaults,"base_inside_corner_size",text="")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self.props.size_defaults,"upper_inside_corner_size",text="")
        
        box = col.box()
        box.label("Placement:")
        row = box.row(align=True)
        row.label("Height Above Floor:")
        row.prop(self.props.size_defaults,"height_above_floor",text="")
        
        box = col.box()
        box.label("Drawer Heights:")
        row = box.row(align=True)
        row.prop(self.props.size_defaults,"equal_drawer_stack_heights")
        if not self.props.size_defaults.equal_drawer_stack_heights:
            row.prop(self.props.size_defaults,"top_drawer_front_height")
    
    def draw(self, context):
        self.props = context.scene.lm_basic_cabinets
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.prop(self.props,'defaults_tabs',expand=True)
        
        if self.props.defaults_tabs == 'SIZES':
            self.draw_cabinet_sizes(box)
        
        if self.props.defaults_tabs == 'EXTERIOR':
            self.draw_exterior_defaults(box)

bpy.utils.register_class(PANEL_Basic_Cabinet_Options)
    