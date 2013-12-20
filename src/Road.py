class Road(object):

    def __init__(self, rid, dest, wt=0.0, info={}):
        '''
        Initializes Road object -
        rid (str) : A unique road id.
        dest (Node) : Reference to the dest Node object.
        wt (float) : Weight/cost of travelling thru this Road.
        info (dict) : extra attribute storage
        '''
        self.dest = dest
        self.wt = wt
        self.rid = rid
        self.angle = angle
        self.info = info
        

    def set_rid(self, rid):
        '''
        set road id
        '''
        self.rid = rid

    def get_rid(self):
        '''
        returns road id
        '''
        return self.rid

    def set_dest(self, dest):
        '''
        set destination Node reference
        '''
        self.dest = dest

    def get_dest(self):
        '''
        returns the destination Node reference
        '''
        return self.dest

    def set_wt(self,wt):
        '''
        set road Weight/cost
        '''
        self.wt = wt

    def get_wt(self):
        '''
        returns road Weight
        '''
        return self.wt

    def update_info(self, **info):
        '''
        set extra info in terms of kw args
        '''
        self.info.update(inf)

    def get_info(self, info=None):
        '''
        Get the required info of the Node, if info is None, return all
        info (str) : is name of data reqd.
        '''
        if not info:
            return self.info
        return self.info[info]

    def get_dest_pid(self):
        '''
        returns the pid of the Node which is the dest
        '''
        return self.dest.get_pid()
        #self -> road obj.
        #dest -> reference to node object
        #dest.pid -> point id of the Node referenced by dest

    def __str__(self):
        '''
        returns the pid of the Node which is the dest
        '''
        return self.dest.get_pid()

