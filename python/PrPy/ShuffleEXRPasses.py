# Script Name: Shuffle EXR Passes
# Version: 1.0
# Purpose: Shuffle EXR passes (layers except rgba) from read node(s).
# Created For: Pr_Suite v1.0
# Created On: 1/8/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (1/8/2015)
#		   Checks for empty selection and available read nodes in selection and raises warning accordingly.
#		   Stores all available passes (layers) names except rgba from selected read nodes.
#		   Creates shuffle nodes for all available passes, labels them accordingly and sets input to selected read nodes.


import nuke

def ShuffleEXRPasses():
	if nuke.selectedNodes() != []:
		selected = nuke.selectedNodes("Read")
		if selected:
			for read in selected:
				channelCollect = read.channels()
				store = []
				for channel in channelCollect:
					cut = channel.split(".")
					ind = cut[0]
					store.append(ind)
				channelSet = list(set(store))
				channelSet.remove("rgba")
				
				for separation in channelSet:
					shuffle = nuke.nodes.Shuffle(label = separation)
					shuffle.knob("in").setValue(separation)
					shuffle.setInput(0, read)
		else:
			nuke.message("Read node(s) not found in selection")
	else:
		nuke.message("No nodes selected")