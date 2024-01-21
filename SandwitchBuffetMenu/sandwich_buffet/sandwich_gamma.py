# --------------------------------------------------------------
#  sandwich_gamma.py
#  Version: 1.0.0
#  Last Updated: 03.01.2024
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#   creates sandwich of lin2log nodes
#
# --------------------------------------------------------------

import nuke 

def sandwichGamma():
    # create top gamma node
    gamtop=nuke.createNode('Gamma',inpanel=False)

    # create bottom gamma node
    gambottom=nuke.createNode('Gamma',inpanel=False)
    gambottom.knob('value').setValue(1.8)
    gambottom.knob('label').setValue('set values here')

    # get names of created gamma nodes
    gtname=gamtop.knob('name').getValue()
    gbname=gambottom.knob('name').getValue()

    # set expression 
    gamtop.knob('value').setExpression("1/parent."+gbname+".value")
    gamtop.knob('channels').setExpression("parent."+gbname+".channels")
    
# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Gamma", "sandwich_gamma.sandwichGamma()") 