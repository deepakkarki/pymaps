#Graph class for holding the road network
from xml.etree import ElementTree
import copy

class Graph(object):

	def __init__(self, src_file=None):
		'''
		constructor, creates a graph object. 
		initialized with file data, if src_file is provided.
		src_file (str) : The location of data source. file or url.
		'''
		self.n_pid = {}
		#Node pid to node ref. mapping

		self.n_pos = {}
		#Node pos to node ref. mapping

		self.n_name = {}
		#Node name to node ref. mapping

		self.r_tag = {}
		#rid to road info mapping. values are also dicts.

		self.dimention = {'minlat':None,'minlon':None,'maxlat':None,'maxlon':None}
		#dimention of the nodes

	def get_graph(self, src):
		'''
		populates the graph as per file/url data
		'''
		pass
		
	def add_node(self, node):
		'''
		add a node to the given graph
		'''
		if node.pid not in self.n_pid:
			self.n_pid[node.pid] = node
			pos = (node.xpos, node.ypos)
			self.n_pos[pos] = node
			if 'name' in node.get_info():
				self.n_name[node.get_info(info='name')] = node

	def get_node(self,pid=None, pos=None, name=None):
		'''
		gets the reqd node from the graph given, 
		pid or pos or name of the Node
		'''
		if pid: 
			return self.n_pid[pid]  
        if position:
        	return self.n_pos[position]
        if name : 
        	return self.n_name[name]
        return None

	def connect(self, src_id, dest_id, rid, wt=None, info={},way='twoway'):
		'''
		connect the nodes with src, dest id with road rid.
		'''
		if src_id not in self.n_pid or dest_id not in self.n_pid:
			pass

		else:
			s_node = self.n_pid[src_id] 
			d_node = self.n_pid[dest_id]

			if not wt:
				wt = (s_node.xpos - d_node.xpos)**2 + (s_node.ypos - d_node.ypos)**2

			if 'angle' not in info:
				info['angle'] = get_angle(self.get_node(pid=src_id), self.get_node(pid=dest_id))

			rd = Road(rid, d_node, wt, **info)
			if dest_id not in self.n_pid[src_id].get_children_id():
				self.n_pid[src_id].add_road(rd)

			if way == 'twoway':
				info = copy.deepcopy(info)
				info['angle'] = (angle+180)%360
				rd = Road(rid, d_node, wt, **info)
				if src_id not in self.n_pid[dest_id].get_children_id():
				self.n_pid[dest_id].add_road(rd)


	def display(self):
		'''
		Display the graph
		'''
		for node in self.n_pid:
            #prints all the children nodes for every node in the graph.
            print 'Tag ID: ',node,'(x= ', self.n_pid[node].xpos,', y= ', self.n_pid[node].ypos, ') -> ',self.n_pid[node].get_children_id()

	def delete_node(self,pid):
		'''
		delete the node with specific pid.
		also automatically delete all roads to and from it.
		'''
		links = self.n_pid[pid].get_children_id()

        for id in links:
            self.delete_road(pid, id)

        node = self.n_pid.pop(pid)
        #delete from n_pid dict
        self.n_name.pop(node.get_info(info='name'), None)
        #delete from n_name dict
        return self.n_pos.pop((node.xpos, node.ypos))
        #delete from n_pos dict, and return the Node object

#This should be delete link, delete road should delete the whole road
	def delete_road(self, pid1, pid2):
		'''
		Remove the road with the given rid
		'''
		node = self.n_pid[pid1]

        for road in node.roads:
            if road.get_dest_pid() == pid2:
                node.roads.remove(road)

        node = self.n_pid[pid2]

        for road in node.roads:
            if road.get_dest_pid() == pid1:
                node.roads.remove(road)

	def update_node_info(self, pid, **info):
		'''
		Update the node with pid = pid with info
		'''
		#if the other side wants to write a dict, 
		#it should unpack by **param while passing
		node = self.n_pid[pid]
        node.update_info(**info)

	def update_road_info(self, rid, **info):
		'''
		Update the road with rid = rid with info
		'''
		if rid in self.road_tags:
            self.r_tag[rid].update(info)
        else:
            self.road_tags[rid] = dict_of_info

def get_angle(node1, node2):
    from math import degrees, atan
    x1 = node1.xpos
    y1 = node1.ypos
    x2 = node2.xpos
    y2 = node2.ypos
    if x1 == x2:
        return 90
    return degrees(atan((y2-y1)/(x2-x1)))