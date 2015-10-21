# Script Name: Delete Thumbs Tmp
# Version: 1.0
# Purpose: Delete read nodes which are reading Thumbs.db and .tmp.
# Created For: Pr_Suite v1.0
# Created On: 28/7/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (28/7/2015)
#		   Search and delete read nodes with Thumbs.db as name and .tmp as extension.


import nuke

def DeleteThumbsTmp():
	all = nuke.allNodes("Read")
	if all:
		for read in all:
			file = read["file"].value()
			last = file.split('/')[-1]
			if last == "Thumbs.db" or last[-4:] == ".tmp":
				nuke.delete(read)
	else:
		nuke.message("No read nodes found")