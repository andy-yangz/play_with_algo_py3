from minheap import MinHeap
from sparse_graph import SparseGraph
from read_graph import read_graph

class LazyPrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.pq = MinHeap(graph.E())
        self.marked = [False for _ in range(graph.V())]
        self.mst = [] #Min Span Tree
        self.mst_weight = 0

        self.visit(0)
        while not self.pq.is_empty():
            min_edge = self.pq.extract_min()
            if self.marked[min_edge.v()] == self.marked[min_edge.w()]:
                continue #如果边两个节点都在红色直接跳过
            self.mst.append(min_edge)
            if self.marked[min_edge.v()]:
                self.visit(min_edge.w())
            else:
                self.visit(min_edge.v())
        self.mst_weight = sum([edge.weight for edge in self.mst])
                
    def visit(self, v):
        assert not self.marked[v]
        self.marked[v] = True
        for e in self.graph.get_adj(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def mst_edges(self):
        return self.mst

    def result(self):
        return self.mst_weight


if __name__ == "__main__":
    g = SparseGraph(8)
    read_graph(g, "testG1.txt")

    print("Test Lazy Prim MST:")
    lazyPrimMST = LazyPrimMST(g)
    mst = lazyPrimMST.mst_edges()
    for edge in mst:
        print(edge)
    print("The MST weight is: ", lazyPrimMST.result())
