import matplotlib.pyplot as plt
import pylab as p

def display_raw(g, show=True):
	fig = p.figure()
	
	for node in g.n_pid.values():
		if len(node.roads) == 0:
			p.plot(node.xpos,node.ypos, 'bo', color='blue')
		elif len(node.roads) == 1:
			p.plot(node.xpos,node.ypos, 'bo', color='black')
		elif len(node.roads) == 2:
			p.plot(node.xpos,node.ypos, 'bo', color='green')
		elif len(node.roads) == 3:
			p.plot(node.xpos,node.ypos, 'bo', color='red')
		else:
			p.plot(node.xpos,node.ypos, 'bo', color='orange')
		for road in node.roads:
			p.plot([node.xpos, road.dest.xpos], [node.ypos, road.dest.ypos], color='blue')
	
	if show: p.show()
