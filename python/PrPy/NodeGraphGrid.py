# Script Name: Node Graph Grid
# Version: 1.0
# Purpose: Enable/Disable show grid and snap to grid.
# Created For: Pr_Suite v1.0
# Created On: 28/7/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (28/7/2015)
#		   Enable/Disable show grid and snap to grid.


import nuke

def NodeGraphGrid():
	show_value = nuke.toNode("preferences").knob("show_grid").value()
	show = nuke.toNode("preferences").knob("show_grid")
	snap_value = nuke.toNode("preferences").knob("SnapToGrid").value()
	snap = nuke.toNode("preferences").knob("SnapToGrid")

	if show_value == 1 & snap_value == 1:
		show.setValue(0)
		snap.setValue(0)
	else:
		show.setValue(1)
		snap.setValue(1)