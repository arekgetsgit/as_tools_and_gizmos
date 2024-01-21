# --------------------------------------------------------------
#  sandwich_reformatscale.py
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

def sandwichReformatScale():
    # create top reformat node
    reftop=nuke.createNode('Reformat',inpanel=False)
    reftop.knob('type').setValue('2')
    reftop.knob('label').setValue('set values here')

    # create bottom reformat node
    refbottom=nuke.createNode('Reformat',inpanel=False)
    refbottom.knob('type').setValue('2')

    # get names of created reformat nodes
    rtname=reftop.knob('name').getValue()
    rbname=refbottom.knob('name').getValue()

    # set expression 
    refbottom.knob('scale').setExpression("1/parent."+rtname+".scale")
    refbottom.knob('resize').setExpression("parent."+rtname+".resize")
    refbottom.knob('filter').setExpression("parent."+rtname+".filter")
    
# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Reformat_Scale", "sandwich_reformatscale.sandwichReformatScale()") 