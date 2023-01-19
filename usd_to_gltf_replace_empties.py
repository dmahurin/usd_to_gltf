# script to convert from usd to gltf and replace empties with boxes
# depends on empties_to_boxes add-on

# Usage: blender -b -P usd2gltf_replace_empties.py -- input.usda output.gltf
# if file is usdz, then first do: unzip input.usdz

import bpy
import sys

import empties_to_boxes

args_start = sys.argv[1:].index('--')
args = sys.argv[args_start+2:]
infile=args[0]
outfile=args[1]

bpy.ops.wm.usd_import(filepath=infile, relative_path=True,
    read_mesh_colors=True,import_usd_preview=True)

context = bpy.context
scene = context.scene
viewlayer = context.view_layer

empties_to_boxes.empties_to_boxes(bpy.context.selected_objects)

bpy.ops.object.select_by_type(extend=False, type='MESH') 
bpy.ops.export_scene.gltf( filepath=outfile, export_yup=True,
    check_existing=False, export_format="GLTF_EMBEDDED")
