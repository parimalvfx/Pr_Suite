# Script Name: menu
# Version: 1.0
# Purpose: Menus for Pr_Suite.
# Created For: Pr_Suite v1.0
# Created On: 5/10/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (5/10/2015)
#		   Pr_Suite Menu in Nodes for gizmos.
#		   Pr_Suite Menu in Nuke for python scripts.


import nuke
import nukescripts
import os
import webbrowser
import PrPy

nodes = nuke.menu( "Nodes" )
g = nodes.addMenu( "Pr_Suite", icon="Pr_Suite_v01.png" )
g.addCommand( "Pr_ShuffleMatte", lambda: nuke.createNode("Pr_ShuffleMatte"), "", icon="Pr_ShuffleMatte_v01.png" )
g.addCommand( "Pr_LBGrain", lambda: nuke.createNode("Pr_LBGrain"), "", icon="Pr_LBGrain_v01.png" )
g.addCommand( "Pr_RGBLuma", lambda: nuke.createNode("Pr_RGBLuma"), "", icon="Pr_RGBLuma_v01.png" )
g.addCommand( "Pr_RGBShadow", lambda: nuke.createNode("Pr_RGBShadow"), "", icon="Pr_RGBShadow_v01.png" )
g.addCommand( "Pr_Contrast", lambda: nuke.createNode("Pr_Contrast"), "", icon="Pr_Contrast_v01.png" )
g.addCommand( "Pr_Palette", lambda: nuke.createNode("Pr_Palette"), "", icon="Pr_Palette_v01.png" )
g.addCommand( "Pr_CameraAim", lambda: nuke.createNode("Pr_CameraAim"), "", icon="Pr_CameraAim_v01.png" )
g.addCommand( "Pr_LightAim", lambda: nuke.createNode("Pr_LightAim"), "", icon="Pr_LightAim_v01.png" )
g.addCommand( "Pr_Timecode", lambda: nuke.createNode("Pr_Timecode"), "", icon="Pr_Timecode_v01.png" )
g.addCommand( "Pr_InfoText", lambda: nuke.createNode("Pr_InfoText"), "", icon="Pr_InfoText_v01.png" )

top = nuke.menu( "Nuke" )
p = top.addMenu( "Pr_Suite", icon="Pr_Suite_v01.png" )
p.addCommand( "Node Graph Grid", "PrPy.NodeGraphGrid.NodeGraphGrid()", "H", icon="Node_Graph_Grid_v01.png" )
p.addCommand( "Master Disable", "PrPy.MasterDisable.MasterDisable()", "Shift+H", icon="Master_Disable_v01.png" )
p.addCommand( "Delete Thumbs.db and .tmp", "PrPy.DeleteThumbsTmp.DeleteThumbsTmp()", "Ctrl+Shift+H", icon="Delete_Thumbs_tmp_v01.png" )
p.addCommand( "Multi Knob Values", "PrPy.MultiKnobValues.MultiKnobValues()", "V", icon="Multi_Knob_Values_v01.png" )
p.addCommand( "Shuffle EXR Passes", "PrPy.ShuffleEXRPasses.ShuffleEXRPasses()", "E", icon="Shuffle_EXR_Passes_v01.png" )
s = p.addMenu( "RGBA Shuffles", icon="RGBA_Shuffles_v01.png" )
s.addCommand( "Red Shuffle", "PrPy.RGBAShuffles.RedShuffle()", "Ctrl+E", icon="RGBA_Shuffles_Red_v01.png" )
s.addCommand( "Green Shuffle", "PrPy.RGBAShuffles.GreenShuffle()", "Shift+E", icon="RGBA_Shuffles_Green_v01.png" )
s.addCommand( "Blue Shuffle", "PrPy.RGBAShuffles.BlueShuffle()", "Ctrl+Shift+E", icon="RGBA_Shuffles_Blue_v01.png" )
s.addCommand( "Alpha Shuffle", "PrPy.RGBAShuffles.AlphaShuffle()", "Ctrl+Alt+E", icon="RGBA_Shuffles_Alpha_v01.png" )
p.addCommand( "Label Shuffle", "PrPy.LabelShuffle.LabelShuffle()", "Ctrl+L", icon="Label_Shuffle_v01.png" )
p.addSeparator()
p.addCommand( "Documentation", "PrPy.DocTuts.Documentation()", "", icon="Doc.png" )
p.addCommand( "Tutorials", "PrPy.DocTuts.Tutorials()", "", icon="Tutorials.png" )
p.addSeparator()
p.addCommand( "License", "PrPy.License.License()", "", icon="Pr_Suite_v01.png" )
p.addCommand( "About Pr_Suite", "PrPy.About.About()", "", icon="Pr_Suite_v01.png" )