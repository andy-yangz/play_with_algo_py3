import random

#稀疏图的实现

class SparseGraph:
    def __init__(self, n, directed=False):
        self.n = n #顶点
        self.m = 0 #边
        self.directed = directed
        self.g = [[] for _ in range(self.n)]
    
    def V(self):
        return self.n
    
    def E(self):
        return self.m
    
    def add_edge(self, v, w):
        assert (0<= v <self.n)
        assert (0<= w <self.n)
        
        self.g[v].append(w)
        if v!=w and (not self.directed):
            self.g[w].append(v)
        self.m += 1
    
    def has_edge(self, v, w):
        assert (0<= v <self.n)
        assert (0<= w <self.n)
        for node in self.g[v]:
            if node == w:
                return True
        return False
    #O(E)
    def get_adj(self, v):
        return iter(self.g[v])

    def show(self):
        for i in range(self.n):
            nodes_print = '\t'.join([str(v) for v in self.g[i]])
            print(f"Vertex {i}: {nodes_print}")

if __name__ == "__main__":
    n, m = 20, 100
    graph = SparseGraph(n, False)
    for i in range(m):
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)
        graph.add_edge(a, b)
    graph.show()
    # for v in range(n):
    #     print(f'{v}: ', end="")
    #     vadj = graph.get_adj(v)
    #     for n in vadj:
    #         print(f"{n} ", end="")
    #     print()