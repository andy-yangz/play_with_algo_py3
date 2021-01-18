from read_graph import read_graph
from sparse_graph import SparseGraph
from index_minheap import IndexMinHeap

class Dijkstra:
    def __init__(self, graph, s):
        self.graph = graph
        self.distto = [0 for _ in range(self.graph.V())]
        self.marked= [False for _ in range(self.graph.V())]
        self.come = [None for _ in range(self.graph.V())]

        self.ipq = IndexMinHeap(self.graph.V())

        self.distto[s] = 0
        self.marked[s] = True
        self.ipq.insert(s, self.distto[s])
        while not self.ipq.is_empty():
            v = self.ipq.extract_min_index()
            self.marked[v] = True
            for edge in self.graph.get_adj(v):
                w = edge.other(v)
                if not self.marked[w]:
                    if (self.come[w] is None) or (self.distto[v]+edge.wt()<self.distto[w]):
                        self.distto[w] = self.distto[v]+edge.wt()
                        self.come[w] = v
                        if self.ipq.contain(w):
                            self.ipq.change(w, self.distto[w])
                        else:
                            self.ipq.insert(w, self.distto[w])

    
    def shortest_path_to(self, w):
        return self.distto[w]

    def has_path_to(self, w):
        return self.marked[w]

    def shortest_path(self, w):
        path = [w]
        cur = w
        while self.come[cur] is not None:
            path.append(self.come[cur])
            cur = self.come[cur]
        return path[::-1]

    def show_path(self, w):
        path = self.shortest_path(w)
        print(" -> ".join([str(n) for n in path]))

if __name__ == "__main__":
    g = SparseGraph(5, True)
    read_graph(g, 'testG1.txt')

    print("Test Dijkstra:")
    dij = Dijkstra(g, 0)
    for i in range(1, 5):
        print(f"Shortest Path to {i} : {dij.shortest_path_to(i)}")
        dij.show_path(i)
        print("------------------")