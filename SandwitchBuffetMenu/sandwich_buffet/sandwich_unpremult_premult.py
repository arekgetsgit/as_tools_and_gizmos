# --------------------------------------------------------------
#  sandwich_unpremult_premult.py
#  Version: 1.0.0
#  Last Updated: 03.01.2024
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#   creates sandwich of unpremult and premult nodes
#
# --------------------------------------------------------------

import nuke 

def sandwichUnpremultPremult():
    #create unpremult
    unpremult=nuke.createNode("Unpremult",inpanel=False)

    #create premult
    premult=nuke.createNode("Premult",inpanel=False)


# Add menu items to the SandwichBuffet nodes menu
nuke.menu('Nodes').addCommand("SandwichBuffet/sandwich_UnpremultPremult", "sandwich_unpremult_premult.sandwichUnpremultPremult()")