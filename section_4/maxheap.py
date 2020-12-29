import random

def print_tree(arr):
    n = len(arr)
    i = 1
    while i < n:
        print(arr[i:i*2])
        i = i*2 

class MaxHeap:
    """
    Max Heap data structure.
    """
    def __init__(self, capacity, arr=None):
        if arr is None:
            self.data = [None] * (capacity+1)
            self.count = 0
            self.capacity = capacity
        else:
            self.data = [None] + arr
            self.count = len(arr)
            self.capacity = capacity
            
            for i in range(self.count//2, 0, -1):
                self.shift_down(i)
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count==0

    def shift_up(self, k):
        ''' Swap Version
        while k > 1 and (self.data[k] > self.data[k//2]):
            self.data[k], self.data[k//2] = self.data[k//2], self.data[k] # Swap 操作
            k = k//2
        '''
        # 赋值版
        item = self.data[k]
        while k>1 and item > self.data[k//2]:
            self.data[k] = self.data[k//2]
            k = k // 2
        self.data[k] = item

    def shift_down(self, k):
        ''' Swap Version
        while 2*k <= self.count:
            j = 2*k #left child position
            if j+1 <= self.count and self.data[j] < self.data[j+1]:
                j += 1
            
            if self.data[j] <= self.data[k]:
                break
            self.data[j], self.data[k] = self.data[k], self.data[j]
            k = j
        ''' 
        item = self.data[k]
        while 2*k <= self.count:
            j = 2*k
            if j+1 <= self.count and self.data[j] < self.data[j+1]:
                j += 1
            if item >= self.data[j]:
                break
            self.data[k] = self.data[j]
            k = j
        self.data[k] = item

    def insert(self, ele):
        # assert(self.count+1 <= self.capacity) #Judge not overflow
        if self.count+1 > self.capacity:
            self.resize(2 * self.capacity)

        self.data[self.count+1] = ele
        self.count +=1
        self.shift_up(self.count)

    def extract_max(self):
        assert self.count>0
        res = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.shift_down(1)
        
        if self.count == self.capacity//4:
            self.resize(self.capacity//2)
        return res

    def resize(self, size):
        # Resize Capacity
        self.capacity = size
        temp = [None] * (size+1) # C++ style
        for i in range(self.count+1):
            temp[i] = self.data[i]
        self.data = temp


if __name__ == "__main__":
    maxheap = MaxHeap(10)
    for i in range(20):
        maxheap.insert(random.randint(0, 30))
    # print_tree(maxheap.data)
    while (not maxheap.is_empty()):
        print(maxheap.extract_max())
    # print(maxheap.size())
    # print(maxheap.data)