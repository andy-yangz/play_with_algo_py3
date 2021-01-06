class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)
    
    def find(self, p):
        assert 0<= p <self.count, "{p} is out of range."
        while p!=self.parent[p]:
            p = self.parent[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot:
            return
        self.parent[proot] = qroot

if __name__ == "__main__":
    uf = UnionFind(100)