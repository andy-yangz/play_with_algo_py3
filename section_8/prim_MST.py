from index_minheap import IndexMinHeap
from sparse_graph import SparseGraph
from read_graph import read_graph

class PrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.ipq = IndexMinHeap(graph.E())
        self.marked = [False for _ in range(graph.V())]
        self.edge_to = [None for _ in range(graph.V())]
        self.mst = [] #Min Span Tree
        self.mst_weight = 0

        self.visit(0)
        while not self.ipq.is_empty():
            v = self.ipq.extract_min_index()
            assert self.edge_to[v]
            self.mst.append(self.edge_to[v])
            self.visit(v)

        self.mst_weight = sum([edge.weight for edge in self.mst])
                
    def visit(self, v):
        assert not self.marked[v]
        self.marked[v] = True
        for e in self.graph.get_adj(v):
            w = e.other(v)
            if not self.marked[w]:
                if not self.edge_to[w]:
                    self.ipq.insert(w, e.wt())
                    self.edge_to[w] = e
                elif e.wt() < self.edge_to[w].wt():
                    self.ipq.change(w, e.wt())
                    self.edge_to[w] = e

    def mst_edges(self):
        return self.mst

    def result(self):
        return self.mst_weight


if __name__ == "__main__":
    g = SparseGraph(8)
    read_graph(g, "testG1.txt")

    print("Test Prim MST:")
    lazyPrimMST = PrimMST(g)
    mst = lazyPrimMST.mst_edges()
    for edge in mst:
        print(edge)
    print("The MST weight is: ", lazyPrimMST.result())
