# Quick Find

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = []
        for i in range(n):
            self.id.append(i)
    
    def find(self, p):
        assert 0<= p <self.count, "{p} is out of range."
        return self.id[p]
    
    def is_connected(self, p, q):
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        if pid == qid:
            return

        for i in range(self.count):
            if self.id[i] == pid:
                self.id[i] = qid

if __name__ == "__main__":
    uf = UnionFind(100)