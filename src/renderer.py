import matplotlib.pyplot as plt
import pylab as p
from pylab import *

def render(g):
	fig = p.figure()

	minX = float(g.dimention['minlon'])
	maxX = float(g.dimention['maxlon'])
	minY = float(g.dimention['minlat'])
	maxY = float(g.dimention['maxlat'])
	ax = fig.add_subplot(111,autoscale_on=False,xlim=(minX,maxX),ylim=(minY,maxY))

	for road in g.r_tag:
		#road is the "rid", viz key in roadTags dictionary
		road_ref = g.r_tag[road]
		#road_ref is the refrence to the value dictionary of the key rid in g.roadTags
		node_list = road_ref['nodes']
		#get all the nodes that fall into this road as a list
		x = []
		y = []
		for pid in node_list:
			ref = g.get_node(pid=pid)
			x.append(ref.ypos)
			y.append(ref.xpos)
		thisRendering = road_ref['render']
		p.plot(x, y,
				marker          = '',
				linestyle       = thisRendering['linestyle'],
				linewidth       = thisRendering['linewidth'],
				color           = thisRendering['color'],
				solid_capstyle  = 'round',
				solid_joinstyle = 'round',
				zorder          = thisRendering['zorder'],
			   )
		
	p.show()
