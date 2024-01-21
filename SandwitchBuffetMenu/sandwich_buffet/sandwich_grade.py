# --------------------------------------------------------------
#  sandwich_grade.py
#  Version: 1.0.0
#  Last Updated: 03.01.2024
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#   creates sandwich of grade nodes
#
# --------------------------------------------------------------

import nuke 

def sandwichGrade():
    # create top grade node
    gradetop=nuke.createNode('Grade',inpanel=False)
    gradetop.knob('gamma').setValue(1.8)
    gradetop.knob('reverse').setValue(True)
    gradetop.knob('label').setValue('set values here')

    # create bottom grade node
    gradebottom=nuke.createNode('Grade',inpanel=False)

    # get names of created grade nodes
    gtname=gradetop.knob('name').getValue()
    gbname=gradebottom.knob('name').getValue()

    # set expression 
    gradebottom.knob('gamma').setExpression("parent."+gtname+".gamma")
    gradebottom.knob('channels').setExpression("parent."+gtname+".channels")
    
# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Grade", "sandwich_grade.sandwichGrade()")