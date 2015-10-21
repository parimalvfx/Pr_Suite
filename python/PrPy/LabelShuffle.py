# Script Name: Label Shuffle
# Version: 1.0
# Purpose: Label shuffle node with name of shuffled layer.
# Created For: Pr_Suite v1.0
# Created On: 12/9/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (12/9/2015)
#		   Labels selected shuffle nodes with the layer name they have shuffled.


import nuke

def LabelShuffle():
	if nuke.selectedNodes() != []:
		selected = nuke.selectedNodes("Shuffle")
		if selected != []:
			for r in selected:
				inv = r.knob("in").value()
				r.knob("label").setValue(inv)
		else:
			nuke.message("Shuffle node(s) not found in selection")
	else:
		nuke.message("No nodes selected")