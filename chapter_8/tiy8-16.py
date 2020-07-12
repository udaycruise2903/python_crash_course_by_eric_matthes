# try it yourself exercise 8-16
# Importing module
import icecream_menu


icecream_menu.make_icecream_menu('vanilla', 'chocolate', 'butterscotch')

# importing module with function name.
from icecream_menu import make_icecream_menu


make_icecream_menu('pineapple', 'candy bar')

# importing function name as fn
from icecream_menu import make_icecream_menu as mim


mim('chocolate flavour', 'vanilla flavour')

# import module name as mn
import icecream_menu as im


im.make_icecream_menu('choco bar')

from icecream_menu import*

make_icecream_menu('pineapple')



