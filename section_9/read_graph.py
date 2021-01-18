from dense_graph import DenseGraph
from sparse_graph import SparseGraph

def read_graph(graph, path):
    f = open(path, 'r')
    V, E = next(f).split(" ")
    V, E = int(V), int(E)

    assert V == graph.V()

    for line in f:
        line = line.strip()
        if not line: continue
        a, b, w = line.split(" ")
        a, b, w= int(a), int(b), float(w)
        graph.add_edge(a, b, w)

if __name__ == "__main__":
    g1 = DenseGraph(8)
    g2 = SparseGraph(8)

    read_graph(g1, "testG1.txt")
    read_graph(g2, "testG1.txt")

    g1.show()
    g2.show()
