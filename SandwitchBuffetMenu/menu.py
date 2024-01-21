
# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

#import sandwich buffet scripts
import sandwich_unpremult_premult
import sandwich_colorspace
import sandwich_grade
import sandwich_lin2log
import sandwich_gamma
import sandwich_reformatscale


# --------------------------------------------------------------
#  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

#create sandwich buffet menu
sandwichBuffetMenu = nuke.menu('Nodes').addMenu('SandwichBuffet', icon="sandwichbuffeticon.png")