from read_graph import read_graph
from sparse_graph import SparseGraph
from index_minheap import IndexMinHeap

class BellmanFord:
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.distto = [0 for _ in range(self.graph.V())]
        self.come = [None for _ in range(self.graph.V())]
        self.has_neg_cycle = False

        #Bellman Ford
        for _ in range(self.graph.V()-1): #V-1 pass
            for i in range(self.graph.V()):
                for edge in self.graph.get_adj(i):
                    w = edge.other(i)
                    if (self.come[w] is None) or (self.distto[i]+edge.weight < self.distto[w]):
                        self.distto[w] = self.distto[i]+edge.weight
                        self.come[w] = i

        self.has_neg_cycle = self.detect_neg_cycle()
    
    def detect_neg_cycle(self):
        for i in range(self.graph.V()):
            for edge in self.graph.get_adj(i):
                w = edge.other(i)
                if (self.come[w] is None) or (self.distto[i]+edge.weight < self.distto[w]):
                    return True
        return False

    def shortest_path_to(self, w):
        return self.distto[w]
    
    def has_path_to(self, w):
        return bool(self.distto[w])
    
    def shortest_path(self, w):
        assert not self.has_neg_cycle
        path = [w]
        cur = w
        while self.come[cur] is not None:
            path.append(self.come[cur])
            cur = self.come[cur]
        return path[::-1]

    def show_path(self, w):
        path = self.shortest_path(w)
        print(" -> ".join([str(n) for n in path]))
    
    def negative_cycle(self):
        return self.has_neg_cycle

if __name__ == "__main__":
    g = SparseGraph(5, True)
    read_graph(g, 'testG2.txt')

    print("Test BellmanFord:")
    bellford = BellmanFord(g, 0)
    if bellford.negative_cycle():
        print("The graph contain negative cycle.")
    else:
        for i in range(1, 5):
            print(f"Shortest Path to {i} : {bellford.shortest_path_to(i)}")
            bellford.show_path(i)
            print("------------------")