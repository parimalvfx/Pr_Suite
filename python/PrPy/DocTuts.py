# Script Name: Doc Tuts
# Version: 1.0
# Purpose: Documentation and Tutorial links for Pr_Suite.
# Created For: Pr_Suite v1.0
# Created On: 5/9/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (5/9/2015)
#		   Pr_Suite documentation launching.
#		   Pr_Suite tutorials launching.


import nuke
import os
import webbrowser

def Documentation():
	for search in nuke.pluginPath():
		path = os.path.dirname(search) + "/documentation/Pr_Suite v1.0 Documentation.html"
		if os.path.exists(path):
			webbrowser.open("file:///" + path)
			break
		else:
			if nuke.ask("Pr_Suite documentation not found in expected installation directory. Click 'Yes' to access online Pr_Suite documentation."):
				webbrowser.open("http://www.parimalvfx.com/rnd/pr_suite/documentation/")
			break

def Tutorials():
	webbrowser.open("https://www.youtube.com/playlist?list=PLGLKN8PppBfiYBDWa_Bk3KVveFcD_BJ3S")