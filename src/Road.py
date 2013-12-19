class Road(object):

    def __init__(self, dest, wt, rid='', angle = 0.0):
        '''
        Initializes Road object -
        dest (Node) : Reference to the dest Node object.
        wt (float) : Weight/cost of travelling thru this Road.
        rid (str) : A unique road id.
        angle (float) : angle road makes with the X-axis
        '''
        self.dest = dest
        self.wt = wt
        self.rid = rid
        self.angle = angle
        
    

    def __str__(self):
        '''
        returns the pid of the Node which is the dest
        '''
        return self.dest.pid
        #self -> road obj.
        #dest -> reference to node object
        #dest.pid -> point id of the Node referenced by dest
