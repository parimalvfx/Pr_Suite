# Script Name: Master Disable
# Version: 1.0
# Purpose: Disable multiple nodes from a single node.
# Created For: Pr_Suite v1.0
# Created On: 12/9/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (12/9/2015)
#		   Disable multiple nodes by linking them to a disable knob in NoOp node.


import nuke

def MasterDisable():
	selected = nuke.selectedNodes()
	if selected != []:
		master = nuke.nodes.NoOp()
		k1 = nuke.Tab_Knob("MasterDisable")
		k2 = nuke.Boolean_Knob("disable", "disable")
		k2.setTooltip("Pass default input through this node without any processing.")
		master.addKnob(k1)
		master.addKnob(k2)
		master["hide_input"].setValue(True)
		master["label"].setValue("Master Disable - [value disable]")
		name = master.knob("name").value()
		set = "parent." + name + ".disable"
		for d in selected:
			d["disable"].setExpression(set)
	else:
		nuke.message("No nodes selected")