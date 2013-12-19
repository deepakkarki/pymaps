#Node class, used to represent a point on the map

class Node(object):

	def __init__(self, pid, xpos=0.0, ypos=0.0, info={}):
		'''
		Initializes a Node object -
		pid (str): The point id, unique for a Node.
		xpos,ypos (float): latitude - logitude resp.
		info (dict) : extra attribute storage
		'''
		self.pid = pid
		self.xpos = xpos
		self.ypos = ypos
		self.roads = []
		self.info = info

	def get_pid(self):
		'''
		returns pid of the Node
		'''
		return self.pid

	def set_pid(self, pid):
		'''
		set the pid of the Node
		pid (str) : unique identifier of the Node
		'''
		self.pid = pid

	def set_pos(self,pos):
		'''
		sets x and y pos of the Node
		pos (tuple of two floats) : holds (x,y) pos to be set
		'''
		self.xpos,self.ypos = pos

	def get_pos(self):
		'''
		returns position of Node
		'''
		return self.xpos, self.ypos

	def set_info(self, **info):
		'''
		set/update the Node info
		info is a key-word args param
		'''
		self.info.update(info)

	def get_info(self, info=None):
		'''
		Get the required info of the Node, if info is None, return all
		info (str) : is name of data reqd.
		'''
		if not info:
			return self.info
		return self.info[info]

	def add_road(self,road):
		'''
		Add a road with this node as starting point
		road (Road) : The road object with this Node as src
		'''
		self.roads.append(road)

	def get_children_id(self):
		'''
		returns a list of children id. 
		(ie) the set of dest Nodes present in the roads list
		'''
		id_list = []
        for road in self.roads:
            id_list.append(road.get_dest_pid())
        return id_list

    def get_children(self):
    	'''
		returns a list of children references. 
		(ie) the set of dest Nodes present in the roads list
		'''
		ref_list = []
        for road in self.roads:
            ref_list.append(road.dest)
        return ref_list
