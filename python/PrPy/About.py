# Script Name: About
# Version: 1.0
# Purpose: Pr_Suite About
# Created For: Pr_Suite v1.0
# Created On: 1/10/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (1/10/2015)
#		   Pr_Suite About


import nuke
import nukescripts
import webbrowser

def About():
	class AboutPanel(nukescripts.PythonPanel):
		def __init__(self, about):
			nukescripts.PythonPanel.__init__(self, "About Pr_Suite")
			self.setMinimumSize(311, 311)
			self.logo = nuke.PyScript_Knob("about_pr_suite", "<img src='About_Pr_Suite.png'>", "webbrowser.open('http://www.parimalvfx.com/rnd/pr_suite/')")
			self.addKnob(self.logo)

	show = AboutPanel( "about" )
	show.showModal()