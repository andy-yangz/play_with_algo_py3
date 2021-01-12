#Path compression
class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(1)
    
    def find(self, p):
        assert 0<= p <self.count, "{p} is out of range."
        # while p!=self.parent[p]:
        #     self.parent[p] = self.parent[self.parent[p]]
        #     p = self.parent[p]
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot:
            return
        if self.rank[proot] < self.rank[qroot]:
            self.parent[proot] = qroot
        elif self.rank[qroot] < self.rank[proot]:
            self.parent[qroot] = proot
        else:
            self.parent[proot] = qroot
            self.rank[qroot] += 1

if __name__ == "__main__":
    uf = UnionFind(100)