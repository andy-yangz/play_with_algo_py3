from union_find5 import UnionFind
from minheap import MinHeap
from sparse_graph import SparseGraph
from read_graph import read_graph

class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        self.pq = MinHeap(graph.E())
        self.mst = []
        self.mstweight = 0
        for i in range(self.graph.V()):
            for edge in self.graph.get_adj(i):
                if edge.v() < edge.w():
                    self.pq.insert(edge)

        #一个个取出来，检验是不是有环
        uf = UnionFind(self.graph.V())
        while (not self.pq.is_empty()) and (len(self.mst)<=graph.V()):
            edge = self.pq.extract_min()
            if not uf.is_connected(edge.v(), edge.w()):
                self.mst.append(edge)
                uf.union(edge.v(), edge.w())
        
        self.mstweight = sum([e.wt() for e in self.mst])
    
    def mst_edges(self):
        return self.mst
    
    def result(self):
        return self.mstweight

if __name__ == "__main__":
    g = SparseGraph(8)
    read_graph(g, "testG1.txt")

    print("Test Kruskal MST:")
    kruskal = KruskalMST(g)
    mst = kruskal.mst_edges()
    for edge in mst:
        print(edge)
    print("The MST weight is: ", kruskal.result())
