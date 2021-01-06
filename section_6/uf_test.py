from union_find1 import UnionFind as UnionFind1
from union_find2 import UnionFind as UnionFind2
from union_find3 import UnionFind as UnionFind3
from union_find4 import UnionFind as UnionFind4
from union_find5 import UnionFind as UnionFind5
import random, time

def testuf(n, UnionFind):
    uf = UnionFind(n)
    start = time.time()
    for i in range(n):
        a, b = random.randint(0, n-1), random.randint(0,n-1)
        uf.union(a, b)
    
    for i in range(n):
        a, b = random.randint(0, n-1), random.randint(0,n-1)
        uf.is_connected(a, b)
    print(f"{2*n} ops, {time.time()-start} secs.")

# print("UF1:")
# testuf(10000, UnionFind1)
# print("UF2:")
# testuf(50000, UnionFind2)
# print("UF3:")
# testuf(100000, UnionFind3)
print("UF4:")
testuf(100000, UnionFind4)
print("UF5:")
testuf(100000, UnionFind5)

# testuf1(100000)
