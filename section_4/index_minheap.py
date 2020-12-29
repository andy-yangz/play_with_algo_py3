import random

def print_tree(arr):
    n = len(arr)
    i = 1
    while i < n:
        print(arr[i:i*2])
        i = i*2 

class MinHeap:
    def __init__(self, capacity, arr=None):
        if arr is None:
            self.data = [None] * (capacity+1)
            self.capacity = capacity
            self.count = 0
        else:
            self.data = [None] + arr
            self.count = capacity
            #heapify
            for i in range((self.count-1)//2, 0, -1):
                self.shift_down(i)

    def shift_up(self, k):
        item = self.data[k]
        while k > 1 and item < self.data[k//2]:
            self.data[k] = self.data[k//2]
            k = k//2
        self.data[k] = item
    
    def shift_down(self, k):
        item = self.data[k]
        while 2*k <= self.count:
            j = 2*k
            if j+1<=self.count and self.data[j] > self.data[j+1]:
                j += 1
            
            if item <= self.data[j]: break
            self.data[k] = self.data[j]
            k = j
        self.data[k] = item


    def is_empty(self):
        return self.count==0
    
    def size(self):
        return self.count

    def insert(self, ele):
        assert self.count<=self.capacity
        
        self.data[self.count+1] = ele
        self.count += 1
        self.shift_up(self.count)
    
    def extract_min(self):
        assert not self.is_empty()

        res = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.shift_down(1)
        return res

if __name__ == "__main__":
    minheap = MinHeap(100)
    # print(minheap.data, minheap.capacity, minheap.count)
    for i in range(20):
        minheap.insert(random.randint(0, 100))
    print_tree(minheap.data)
    while (not minheap.is_empty()):
        print(minheap.extract_min())
    # print(maxheap.size())
    # print(maxheap.data)