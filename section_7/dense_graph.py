import random
#稠密图的实现

class DenseGraph:
    def __init__(self, n, directed=False):
        self.n = n #顶点
        self.m = 0 #边
        self.directed = directed
        self.g = [[False for _ in range(self.n)] for _ in range(self.n)]
    
    def V(self):
        return self.n
    
    def E(self):
        return self.m
    
    def add_edge(self, v, w):
        assert (0<= v <self.n)
        assert (0<= w <self.n)

        if self.has_edge(v, w): return 

        self.g[v][w] = True
        if not self.directed:
            self.g[w][v] = True
        self.m += 1
    
    def has_edge(self, v, w):
        assert (0<= v <self.n)
        assert (0<= w <self.n)
        return self.g[v][w]
    #O(V)
    def get_adj(self, v):
        return (i for i,e in enumerate(self.g[v]) if e)
    
    def show(self):
        for i in range(self.n):
            print("\t".join(['1' if link else '0' for link in self.g[i]]))

if __name__ == "__main__":
    n, m = 20, 100
    graph = DenseGraph(n, False)
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
