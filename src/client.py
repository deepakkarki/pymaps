from Graph import *
from renderer import *
from display_raw import *

g = Graph('sample.osm')
display_raw(g)
render(g)

print "done!!"