import re
from collections import OrderedDict

class NodeMgr:
    def __init__( self):
        self.idx = 0
        self.nodes = OrderedDict()

    def add( self, n):
        if n not in self.nodes:
            self.nodes[n] = self.idx
            self.idx += 1

        assert len(self.nodes) == self.idx

        return self.nodes[n]
        
if __name__ == "__main__":
    p = re.compile( "^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$")

    # u v d e
    # t(u) + d - e p <= t(v)
    # t(u) - t(v) -e p <= -d
    # t(v) - t(u) +e p >=  d


    mgr = NodeMgr()

    lst = []
    with open( "__ers", "rt") as fp:
        for line in fp:
            line = line.rstrip('\n')
            m = p.match( line)
            if m:
                tup = m.groups()
                n0 = mgr.add( tup[0])
                n1 = mgr.add( tup[1])
                lst.append( (n0,n1,float(tup[2]),int(tup[3])))
            else:
                assert False

    print( "Maximize")
    print( " obj: p")
    print( "Subject To")
    for (i,tup) in enumerate(lst):
        print( " c%d: x%d - x%d + %d p >= %g" % (i,tup[1],tup[0],tup[3],tup[2]))
    print( "Bounds")
    print( " 0 <= p")
