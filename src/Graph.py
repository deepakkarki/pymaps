#Graph class for holding the road network
from xml.etree import ElementTree

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
		
	def add_node(self, Node):
		'''
		add a node to the given graph
		'''
		pass

	def get_node(self,pid=None, pos=None, name=None):
		'''
		gets the reqd node from the graph given, 
		pid or pos or name of the Node
		'''
		pass

	def connect(self, src_id, dest_id, rid, wt=0.0, info={},type='oneway'):
		'''
		connect the nodes with src, dest id with road rid.
		'''
		pass

	def display(self):
		'''
		Display the graph
		'''
		pass

	def delete_node(self,pid):
		'''
		delete the node with specific pid.
		also automatically delete all roads to and from it.
		'''
		pass

	def delete_road(self, rid):
		'''
		Remove the road with the given rid
		'''

	def update_node_info(self, pid, **info):
		'''
		Update the node with pid = pid with info
		'''
		#if the other side wants to write a dict, 
		#it should unpack by **param while passing
		pass

	def update_road_info(self, rid, **info):
		'''
		Update the road with rid = rid with info
		'''
		pass
		
