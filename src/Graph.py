#Graph class for holding the road network
from xml.etree import ElementTree
from Node import Node
from Road import Road
from rendering_rules import renderingRules
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

		if src_file:
			self.get_graph(src_file)

	def get_graph(self, src):
		'''
		populates the graph as per file/url data
		'''
		document = ElementTree.parse( src )
		dimention = document.find( 'bounds' ).attrib
		for stat in dimention:
			dimention[stat] = float(dimention[stat])
		self.dimention = dimention

		for user in document.findall( 'node' ):
			prop = user.attrib
			#find all tags tagged node
			id = prop.pop('id')
			#get the id of the Node
			lon = prop.pop('lon')
			#get the id of the Node
			lat = prop.pop('lat')
			#get the id of the Node
			node = Node(id, float(lat), float(lon), **prop)
			self.add_node(node)

		for way in document.findall( 'way' ):
			#we have created the nodes in the previous loop, now link them all.
			id = way.attrib[ 'id' ] 
			#save the current road_id to id
			xyz=[]
			#the list of all the node id that appear on the road.
			info = {}
			#info about this particular road.
			
			for i in way.getchildren():

				if i.tag == 'nd': #if the child is a node
					#add the node id to the list xyz, later after all children have been exhausted, 
					#link the nodes which belong to the road.
					if i.attrib['ref'] in self.n_pid:
						xyz.append(i.attrib['ref'])
					
				if i.tag == 'tag': #if the child is a tag containing info about the road
					#then add the info_name as a key in the dict info, the corresponding value being the info_value
					#should i add start_node and end_node as a key-value in info?? if so how?
					info[i.attrib['k']] = i.attrib['v']
					
			if 'highway' in info.keys():
				info['nodes'] = xyz
				
				if info['highway'] in renderingRules.keys():
					info['render'] = renderingRules[info['highway']] #info[render] itself holds a dictionary
				else:
					info['render'] = renderingRules['default']

				self.update_r_tag_data(id, **info)
				
				route = 'twoway'
				if 'oneway' in info:
					route = 'oneway'

				for i in range(0,len(xyz)-1):
					#now that all children of the selected 'way' (see prev loop) have been exhausted, 
					#link the nodes which belong to the road.
					self.connect(xyz[i],xyz[i+1], rid = id,way=route)

		
	def add_node(self, node):
		'''
		add a node to the given graph
		node (Node) : the node we wish to add
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

	def connect(self, src_id, dest_id, rid, wt=None,way='twoway', **info):
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
				info['angle'] = (info['angle']+180)%360
				rd = Road(rid, d_node, wt, **info)
				if src_id not in self.n_pid[dest_id].get_children_id():
					self.n_pid[dest_id].add_road(rd)


#TODO : This should also remove the node from list in r_tag dict.
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

#TODO : This should be delete link, delete road should delete the whole road
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

#TODO : should probably rename road to link.
	def update_r_tag_data(self, rid, **info):
		'''
		Update the road dict of the graph
		#not individual road object
		'''
		if rid in self.r_tag:
			self.r_tag[rid].update(info)
		else:
			self.r_tag[rid] = info

#TODO : complete this function. lot of thinking here. 
	def save(self, d_file):
		'''
		saves the current graph into a XML file, can be used to save custom layers.
		d_file (str) : fiel name to store the file as  d_file.xml
		'''
		pass

	def display(self):
		'''
		Display the graph
		'''
		for node in self.n_pid:
			#prints all the children nodes for every node in the graph.
			print 'Tag ID: ',node,'(x= ', self.n_pid[node].xpos,', y= ', self.n_pid[node].ypos, ') -> ',self.n_pid[node].get_children_id()


def get_angle(node1, node2):
	from math import degrees, atan
	x1 = node1.xpos
	y1 = node1.ypos
	x2 = node2.xpos
	y2 = node2.ypos
	if x1 == x2:
		return 90
	return degrees(atan((y2-y1)/(x2-x1)))
