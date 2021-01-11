from sparse_graph import SparseGraph
from dense_graph import DenseGraph
from read_graph import read_graph

class Component:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False for _ in range(graph.V())]
        self.ids = [-1 for _ in range(graph.V())]
        self.ccount = 0

        for i in range(graph.V()):
            if not self.visited[i]:
                self.dfs(i)
                self.ccount += 1
            
    def dfs(self, v):
        self.visited[v] = True
        self.ids[v] = self.ccount
        for w in self.graph.get_adj(v):
            if not self.visited[w]:
                self.dfs(w)

    def count(self):
        return self.ccount

    def is_connected(self, v, w):
        assert 0 <= v < self.graph.V()
        assert 0 <= w < self.graph.V()

        return self.ids[v] == self.ids[w]


if __name__ == "__main__":
    g1 = SparseGraph(13)
    read_graph(g1, "testG1.txt")
    component1 = Component(g1)
    print(f"TestG1.txt, Component Count: ", component1.count())
    
    g2 = SparseGraph(6)
    read_graph(g2, "testG2.txt")
    component2 = Component(g2)
    print(f"TestG2.txt, Component Count: ", component2.count())