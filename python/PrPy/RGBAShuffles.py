# Script Name: RGBA Shuffles
# Version: 1.0
# Purpose: Create a new shuffle node with pre-shuffled rgba channels.
# Created For: Pr_Suite v1.0
# Created On: 11/8/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (11/8/2015)
#		   Creates a new shuffle node with pre-shuffled rgba channels, tile color and sets node input to selected node, if any.


import nuke

def RedShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		red = nuke.nodes.Shuffle(tile_color="0xff0000ff", red="red", green="red", blue="red", alpha="red")
		try:
			red.setInput(0, connect)
		except ValueError:
			pass

def GreenShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		green = nuke.nodes.Shuffle(tile_color="0xff00ff", red="green", green="green", blue="green", alpha="green")
		try:
			green.setInput(0, connect)
		except ValueError:
			pass

def BlueShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		blue = nuke.nodes.Shuffle(tile_color="0xffff", red="blue", green="blue", blue="blue", alpha="blue")
		try:
			blue.setInput(0, connect)
		except ValueError:
			pass

def AlphaShuffle():
	selected = nuke.selectedNodes()
	for connect in selected:
		alpha = nuke.nodes.Shuffle(tile_color="0xffffffff", red="alpha", green="alpha", blue="alpha", alpha="alpha")
		try:
			alpha.setInput(0, connect)
		except ValueError:
			pass