# Script Name: Multi Knob Values
# Version: 1.0
# Purpose: Get knob names and values from user and apply these values to selected nodes.
# Created For: Pr_Suite v1.0
# Created On: 15/7/2015
# Author: Parimal Desai
# Website: www.parimalvfx.com
# History: v1.0 (15/7/2015)
#		   Python panel with five string knobs for knob names and five array knobs for values.
#		   Setting values to selected nodes and checking for NameError and TypeError.


import nuke
import nukescripts
import os
import webbrowser

def MultiKnobValues():
	# checking if any nodes are selected if not raise warning
	selected = nuke.selectedNodes()
	if selected != []:
		# creating knob values panel
		class KnobValuesPanel( nukescripts.PythonPanel ):
			def __init__( self, node ):
				nukescripts.PythonPanel.__init__(self, "Multi Knob Values")
				self.setMinimumSize(370, 250)
				self.note = nuke.Text_Knob("note", "", "Enter knob calling Name and Value")
				self.blank1 = nuke.Text_Knob("blank1", "", " ")
				self.knob1 = nuke.String_Knob("konb1", "Knob 1")
				self.value1 = nuke.Array_Knob("value1", " = Value 1")
				self.value1.clearFlag( nuke.STARTLINE )
				self.knob2 = nuke.String_Knob("knob2", "Knob 2")
				self.value2 = nuke.Array_Knob("value2", " = Value 2")
				self.value2.clearFlag( nuke.STARTLINE )
				self.knob3 = nuke.String_Knob("knob3", "Knob 3")
				self.value3 = nuke.Array_Knob("value3", " = Value 3")
				self.value3.clearFlag( nuke.STARTLINE )
				self.knob4 = nuke.String_Knob("knob4", "Knob 4")
				self.value4 = nuke.Array_Knob("value4", " = Value 4")
				self.value4.clearFlag ( nuke.STARTLINE )
				self.knob5 = nuke.String_Knob("knob5", "Knob 5")
				self.value5 = nuke.Array_Knob("value5", " = Value 5")
				self.value5.clearFlag( nuke.STARTLINE )
				self.blank2 = nuke.Text_Knob("blank2", "", " ")
				self.help = nuke.PyScript_Knob("help", "Help", """class HelpPanel( nukescripts.PythonPanel ):
	def __init__( pan, node ):
		nukescripts.PythonPanel.__init__(pan, "Multi Knob Values Help")
		pan.setMinimumSize(830, 455)
		pan.h1 = nuke.Text_Knob("h1", "", "<font color = 'grey' size = '5'><b>Multi Knob Values</b></font><font color = 'grey' size = '3'> v1.0</font>")
		pan.h2 = nuke.Text_Knob("h2", "", "<font color = 'white'><b>Change multiple knob values of selected nodes.</font>")
		pan.gp1 = nuke.Text_Knob("gp1", "", " ")
		pan.h3 = nuke.Text_Knob("h3", "", "<font color = 'grey' size = '5'><b>Step</b>By<b>Step</b>")
		pan.h4 = nuke.Text_Knob("h4", "", "<font color = 'lightgreen'><p><b>#Step 1:</b> Select nodes to change knob values.</p><p><b>#Step 2:</b> Run 'Multi Knob Values'</p><p><b>#Step 3:</b> Enter knob calling name of your desired knob in any of the Knob inputs.</p><p><b>#Step 4:</b> Enter desired value for that knob in Value input.<p></p>")
		pan.h5 = nuke.Text_Knob("h5", "", "<font color = 'grey' size = '5'><b>Caution</font>")
		pan.h6 = nuke.Text_Knob("h6", "", "<font color = 'red'><b><p>#Make sure the value of knob which you are wanting to change, that knob is available in all selected nodes.</p><p>#Currently only numerical and boolean values are supported for Value input.</p><p>#If you try to set knob values other than numericals and boolean, no value will get applied to that knob.</p><p>#If you write only knob calling name and don't assign any value to it then 0 value will get applied to that knob.</p><p></p>")
		pan.support = nuke.Text_Knob("support", "<b>Support</b>")
		pan.documentation = nuke.PyScript_Knob("documentation", "Documentation", '''for search in nuke.pluginPath():
	path = os.path.dirname(search) + "/documentation/MultiKnobValuesv10.html"
	if os.path.exists(path):
		webbrowser.open("file:///" + path)
		break
	else:
		if nuke.ask("Pr_Suite documentation not found in expected installation directory. Click 'Yes' to access online Pr_Suite documentation."):
			webbrowser.open("http://www.parimalvfx.com/rnd/pr_suite/documentation/")
		break''')
		pan.documentation.clearFlag( nuke.STARTLINE )
		pan.report_bug = nuke.PyScript_Knob("report_bug", "Report Bug", "webbrowser.open('http://www.parimalvfx.com/rnd/pr_suite/report-bug/')")
		pan.report_bug.clearFlag( nuke.STARTLINE )
		pan.check_updates = nuke.PyScript_Knob("check_updates", "Check for Updates", "webbrowser.open('http://www.parimalvfx.com/rnd/pr_suite/python-scripts/')")
		pan.gp2 = nuke.Text_Knob("gp2", "       ", "")
		pan.gp3 = nuke.Text_Knob("gp3", "", " ")
		
		for insert in ( pan.h1, pan.h2, pan.gp1, pan.h3, pan.h4, pan.h5, pan.h6, pan.support, pan.documentation, pan.report_bug, pan.check_updates, pan.gp2, pan.gp3 ):
			pan.addKnob( insert )

show = HelpPanel( "node" )
show.showModal()""")
				
				for add in ( self.note, self.blank1, self.knob1, self.value1, self.knob2, self.value2, self.knob3, self.value3, self.knob4, self.value4, self.knob5, self.value5, self.blank2, self.help ):
					self.addKnob( add )

			# defining knob changed function
			def knobChanged( self, knob ):
				if knob.name() == "OK":
					# storing knob values
					k1 = self.knob1.value()
					v1 = self.value1.value()
					k2 = self.knob2.value() 
					v2 = self.value2.value()
					k3 = self.knob3.value()
					v3 = self.value3.value()
					k4 = self.knob4.value()
					v4 = self.value4.value()
					k5 = self.knob5.value()
					v5 = self.value5.value()
					print 'Your values are: ', k1, v1, k2, v2, k3, v3, k4, v4, k5, v5
					
					# setting knob values to selected nodes, checking for errors and raising warning
					selected = nuke.selectedNodes()
					a = 0
					
					# setting knob 1
					try:
						for i in selected:
							kne1 = ""
							i[k1].setValue(v1)
					except NameError:
						kne1 = " Knob 1"
						a = 1
					except TypeError:
						pass
					else:
						pass
					
					# setting knob 2
					try:
						for i in selected:
							kne2 = ""
							i[k2].setValue(v2)
					except NameError:
						kne2 = " Knob 2"
						a = 1
					except TypeError:
						pass
					else:
						pass
					
					# setting knob 3
					try:
						for i in selected:
							kne3 = ""
							i[k3].setValue(v3)
					except NameError:
						kne3 = " Knob 3"
						a = 1
					except TypeError:
						pass
					else:
						pass
					
					# setting knob 4
					try:
						for i in selected:
							kne4 = ""
							i[k4].setValue(v4)
					except NameError:
						kne4 = " Knob 4"
						a = 1
					except TypeError:
						pass
					else:
						pass
					
					# setting knob 5
					try:
						for i in selected:
							kne5 = ""
							i[k5].setValue(v5)
					except NameError:
						kne5 = " Knob 5"
						a = 1
					except TypeError:
						pass
					else:
						pass
					
					# raising error if knob name is wrong
					if a == 1:
						er = "Knob calling name in these knobs are not correct: "
						nuke.message( er + kne1 + kne2 + kne3 + kne4 + kne5 )
				
				else:
					pass

		# showing panel
		view = KnobValuesPanel( "node" )
		view.showModalDialog()

	else:
		print nuke.message("No nodes selected")