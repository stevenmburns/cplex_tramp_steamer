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
        
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser( description="Generate .lp file from text file with 4 fields per line: u, v, alpha, epsilon")

    parser.add_argument( "-n", "--block_name", type=str, required=True)  
    parser.add_argument( "-ifn", "--input_file_name", type=str, required=True)  

    args = parser.parse_args()

    p = re.compile( "^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$")

    # u v d e
    # t(u) + d - e p <= t(v)
    # t(u) - t(v) - e p <= -d
    # t(v) - t(u) + e p >=  d

    mgr = NodeMgr()

    lst = []
    with open( args.input_file_name, "rt") as fp:
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

    with open( args.block_name + ".lp", "wt") as fp:
        print( "Minimize", file=fp)
        print( " obj: p", file=fp)
        print( "Subject To", file=fp)
        for (i,tup) in enumerate(lst):
            print( " c%d: x%d - x%d + %d p >= %g" % (i,tup[1],tup[0],tup[3],tup[2]), file=fp)
        print( "Bounds", file=fp)
        print( " 0 <= p", file=fp)
        print( "End", file=fp)
