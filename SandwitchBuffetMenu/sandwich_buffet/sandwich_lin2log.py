# --------------------------------------------------------------
#  sandwich_lin2log.py
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

def sandwichLin2Log():
    #create top log2lin
    lin2logtop=nuke.createNode("Log2Lin",inpanel=False)
    lin2logtop.knob('operation').setValue('1')
    lin2logtop.knob('label').setValue('set values here')

    #create bottom log2lin
    lin2logbottom=nuke.createNode("Log2Lin",inpanel=False)

    # get names of created log2lin nodes
    ltname=lin2logtop.knob('name').getValue()
    lbname=lin2logbottom.knob('name').getValue()

    # set expression
    lin2logbottom.knob('black').setExpression("parent."+ltname+".black")
    lin2logbottom.knob('white').setExpression("parent."+ltname+".white") 
    lin2logbottom.knob('gamma').setExpression("parent."+ltname+".gamma")
    
# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Lin2Log", "sandwich_lin2log.sandwichLin2Log()") 