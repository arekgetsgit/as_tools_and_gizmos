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

def sandwichColorspace():
    # create top colorspace node
    cstop=nuke.createNode('Colorspace',inpanel=False)
    cstopin=cstop.knob('colorspace_in')
    cstopin.setValue('7')
    cstop.knob('label').setValue('set values here')
    cstopout=cstop.knob('colorspace_out')
    cstopout.setValue('19')

    # get name of the top colorspace node
    ctname=cstop.knob('name').getValue()

    # create bottom colorspace node
    csbottom=nuke.createNode('Colorspace',inpanel=False)
    csbottom.knob('colorspace_in').setExpression("parent."+ctname+".colorspace_out")
    csbottom.knob('colorspace_out').setExpression("parent."+ctname+".colorspace_in")

# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_Colorspace", "sandwich_colorspace.sandwichColorspace()")