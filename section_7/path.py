from sparse_graph import SparseGraph
from read_graph import read_graph
from component import Component

class Path:
    def __init__(self, graph, s):
        assert 0<= s <graph.V()

        self.graph = graph
        self.visited = [False for _ in range(graph.V())]
        self.come = [-1 for _ in range(graph.V())] #Come From
        
        self.s = s

        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.graph.get_adj(v):
            if not self.visited[w]:
                self.come[w] = v
                self.dfs(w)

    def has_path(self, w):
        assert 0 <= w < self.graph.V()
        return self.visited[w]

    def path(self, w):
        path = []
        cur = w
        while cur != -1:
            path.append(cur)
            cur = self.come[cur]
        return path[::-1]

    def show_path(self, w):
        path = self.path(w)
        for i,p in enumerate(path):
            if i == len(path)-1:
                break
            print(f"{p} -> ", end="")
        print(p)

if __name__ == "__main__":
    g = SparseGraph(6)
    read_graph(g, "testG2.txt")
    g.show()

    dfs = Path(g, 0)
    print("DFS: ")
    dfs.show_path(4)