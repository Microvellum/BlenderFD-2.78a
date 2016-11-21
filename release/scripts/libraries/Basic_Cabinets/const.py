from os import path

""" Folder Name of Libraries"""
DOOR_FOLDER_NAME = "Door Panels"
PULL_FOLDER_NAME = "Cabinet Pulls"
MATERIAL_LIBRARY_NAME = "Cabinet Materials"
COLUMN_FOLDER_NAME = "Columns"
SINK_FOLDER_NAME = "Sinks"
COOKTOP_FOLDER_NAME = "Cooktops"
FAUCET_FOLDER_NAME = "Faucets"
CROWN_MOLDING_FOLDER_NAME = "Crown Molding Profiles"
BASE_MOLDING_FOLDER_NAME = "Base Molding Profiles"
CORE_CATEGORY_NAME = "Wood Core"

""" Library Names"""
FACEFRAME_LIBRARY_NAME = "Cabinets - Face Frame"
FRAMELESS_LIBRARY_NAME = "Cabinets - Frameless"
BASE_CATEGORY_NAME = "Base Cabinets"
TALL_CATEGORY_NAME = "Tall Cabinets"
UPPER_CATEGORY_NAME = "Upper Cabinets"
OUTSIDE_CORNER_CATEGORY_NAME = "Outside Corner Cabinets"
INSIDE_CORNER_CATEGORY_NAME = "Inside Corner Cabinets"
TRANSITION_CATEGORY_NAME = "Transition Cabinets"
STARTER_CATEGORY_NAME = "Starter Cabinets"
DRAWER_CATEGORY_NAME = "Drawer Cabinets"
BLIND_CORNER_CATEGORY_NAME = "Blind Corner Cabinets"

""" Common Directory Names """
ROOT_DIR = path.dirname(__file__)
CARCASS_DIR = path.join(ROOT_DIR,"Cabinet Assemblies","Basic Carcasses")
CUTPARTS_DIR = path.join(ROOT_DIR,"Cabinet Assemblies","Cut Parts")
COUNTERTOP_PARTS_DIR = path.join(ROOT_DIR,"Cabinet Assemblies","Countertop Parts")
COLUMN_PARTS_DIR = path.join(ROOT_DIR,"Columns")

""" Assembly Paths """
SIMPLE_CARCASS = path.join(CARCASS_DIR,"Simple Carcass.blend")
BASE_ASSEMBLY = path.join(CARCASS_DIR,"Base Assembly.blend")

NOTCHED_SIDE = path.join(CUTPARTS_DIR,"Notched Side.blend")
PART_WITH_FRONT_EDGEBANDING = path.join(CUTPARTS_DIR,"Part with Front Edgebanding.blend")
PART_WITH_NO_EDGEBANDING = path.join(CUTPARTS_DIR,"Part with No Edgebanding.blend")
PART_WITH_FRONT_AND_BOTTOM_EDGEBANDING = path.join(CUTPARTS_DIR,"Part with Front and Bottom Edgebanding.blend")
PART_WITH_EDGEBANDING = path.join(CUTPARTS_DIR,"Part with Edgebanding.blend")
CHAMFERED_PART = path.join(CUTPARTS_DIR,"Chamfered Part.blend")
CORNER_NOTCH_PART = path.join(CUTPARTS_DIR,"Corner Notch Part.blend")
TRANSITION_PART = path.join(CUTPARTS_DIR,"Transition Part with Front Edgebanding.blend")
BENDING_PART = path.join(CUTPARTS_DIR,"Cut Parts","Bending Part.blend")
RADIUS_CORNER_PART_WITH_EDGEBANDING = path.join(CUTPARTS_DIR,"Radius Corner Part with Edgebanding.blend")
DIVISION = path.join(CUTPARTS_DIR,"Part with Edgebanding.blend")
BLIND_PANEL = path.join(CUTPARTS_DIR,"Part with Edgebanding.blend")
MID_RAIL = path.join(CUTPARTS_DIR,"Part with Edgebanding.blend")

BACKSPLASH_PART = path.join(COUNTERTOP_PARTS_DIR,"Backsplash.blend")
CTOP = path.join(COUNTERTOP_PARTS_DIR,"Straight Countertop Square.blend")
NOTCHED_CTOP = path.join(COUNTERTOP_PARTS_DIR,"Corner Notched Countertop Square.blend")
DIAGONAL_CTOP = path.join(COUNTERTOP_PARTS_DIR,"Corner Diagonal Countertop Square.blend")

DRAWER_SLIDE = path.join(ROOT_DIR,"Cabinet Assemblies","Hardware","Drawer Slide.blend")
LEG_LEVELERS = path.join(ROOT_DIR,"Cabinet Assemblies","Hardware","Leg Levelers.blend")
SPACER = path.join(ROOT_DIR,"Cabinet Assemblies","Hardware","Spacer.blend")

ADJ_MACHINING = path.join(ROOT_DIR,"Cabinet Assemblies","Machining","Adjustable Shelf Holes.blend")

DRAWER_BOX = path.join(ROOT_DIR,"Cabinet Assemblies","Drawer Boxes","Wood Drawer Box.blend")

MICROWAVE = path.join(ROOT_DIR,"Appliances","Conventional Microwave.blend")
VENT = path.join(ROOT_DIR,"Appliances","Wall Mounted Range Hood 01.blend")
REFRIGERATOR = path.join(ROOT_DIR,"Appliances","Professional Refrigerator Generic.blend")
SINK = path.join(ROOT_DIR,"Sinks","Double Basin Sink.blend")

HARDWOOD = path.join(ROOT_DIR,"Cabinet Assemblies","Face Frames","Hardwood.blend")
FACE_FRAME = path.join(ROOT_DIR,"Cabinet Assemblies","Face Frames","Face Frame.blend")
PIE_CUT_FACE_FRAME = path.join(ROOT_DIR,"Cabinet Assemblies","Face Frames","Pie Cut Face Frame.blend")

""" Default Materials """
EXPOSED_CABINET_MATERIAL = ("Plastics","Melamine","White Melamine")
UNEXPOSED_CABINET_MATERIAL = ("Wood","Wood Core","PB")
SEMI_EXPOSED_CABINET_MATERIAL = ("Plastics","Melamine","White Melamine")
DOOR_BOX_MATERIAL = ("Plastics","Melamine","White Melamine")
DOOR_MATERIAL = ("Plastics","Melamine","White Melamine")
GLASS_MATERIAL = ("Glass","Glass","Glass")
METAL = ("Metals","Metals","Stainless Steel")
DRAWER_BOX_MATERIAL = ("Plastics","Melamine","White Melamine")
COUNTER_TOP_MATERIAL = ("Stone","Stone","Basalt Slate")
