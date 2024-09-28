# --------------------------------------------------------------
#  sandwich_colorspace.py
#  Version: 1.0.0
#  Last Updated: 03.01.2024
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#   creates sandwich of colorspace nodes
#
# --------------------------------------------------------------

import nuke

def sandwichOCIOColorspace():
    # create top colorspace node
    cstop=nuke.createNode('OCIOColorSpace',inpanel=False)
    cstopin=cstop.knob('in_colorspace')
    cstopin.setValue('7')
    cstop.knob('label').setValue('set values here')
    cstopout=cstop.knob('out_colorspace')
    cstopout.setValue('19')

    # get name of the top colorspace node
    ctname=cstop.knob('name').getValue()

    # create bottom colorspace node
    csbottom=nuke.createNode('OCIOColorSpace',inpanel=False)
    csbottom.knob('in_colorspace').setExpression("parent."+ctname+".out_colorspace")
    csbottom.knob('out_colorspace').setExpression("parent."+ctname+".in_colorspace")
    csbottom.setYpos(csbottom.ypos()+100)

# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Colorspace", "sandwich_colorspace.sandwichColorspace()")