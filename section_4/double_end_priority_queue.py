# Aka min max priority queue
import random

class MinMaxPriorityQueue:
    def __init__(self, capacity):
        self.data = [None] * (capacity+1)
        self.maxidx = [None] * (capacity+1)
        self.minidx = [None] * (capacity+1)
        self.maxrev = [0] * (capacity+1)
        self.minrev = [0] * (capacity+1)
        self.count = 0
        self.capacity = capacity

    def shift_up_max(self, k):
        if k > self.count: return
        item = self.data[self.maxidx[k]]
        idx = self.maxidx[k]
        while k>1 and item > self.data[self.maxidx[k//2]]:
            self.maxidx[k] = self.maxidx[k//2]
            self.maxrev[self.maxidx[k]] = k
            k = k//2
        self.maxidx[k] = idx
        self.maxrev[idx] =k
    
    def shift_up_min(self, k):
        if k > self.count: return #if k is invalid, return directly
        item = self.data[self.minidx[k]]
        idx = self.minidx[k]
        while k>1 and item < self.data[self.minidx[k//2]]:
            self.minidx[k] = self.minidx[k//2]
            self.minrev[self.minidx[k]] = k
            k = k//2
        self.minidx[k] = idx
        self.minrev[idx] =k
    
    def shift_down_max(self, k):
        item = self.data[self.maxidx[k]]
        idx = self.maxidx[k]
        while 2*k <= self.count:
            j = 2*k 
            if 2*k+1 <= self.count and self.data[self.maxidx[j]] < self.data[self.maxidx[j+1]]:
                j += 1
            if item >= self.data[self.maxidx[j]]: break
            self.maxidx[k] = self.maxidx[j]
            self.maxrev[self.maxidx[k]] = k
            k = j
        self.maxidx[k] = idx
        self.maxrev[idx] = k 
    
    def shift_down_min(self, k):
        item = self.data[self.minidx[k]]
        idx = self.minidx[k]
        while 2*k <= self.count:
            j = 2*k 
            if 2*k+1 <= self.count and self.data[self.minidx[j]] > self.data[self.minidx[j+1]]:
                j += 1
            if item <= self.data[self.minidx[j]]: break
            self.minidx[k] = self.minidx[j]
            self.minrev[self.minidx[k]] = k
            k = j
        self.minidx[k] = idx
        self.minrev[idx] = k 
    
    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
    def get_min(self):
        return self.data[self.minidx[1]]

    def get_max(self):
        return self.data[self.maxidx[1]]

    def put(self, ele):
        assert self.count<self.capacity
        for i in range(1, self.capacity+1):
            if self.data[i] is None:
                self.data[i] = ele
                self.maxidx[self.count+1] = i
                self.minidx[self.count+1] = i
                self.maxrev[i] = self.count+1
                self.minrev[i] = self.count+1
                self.count += 1
                self.shift_up_max(self.count)
                self.shift_up_min(self.count)
                break

    def remove_max(self):
        assert not self.is_empty()
        idx = self.minrev[self.maxidx[1]]
        res = self.data[self.maxidx[1]]
        self.data[self.maxidx[1]] = None

        self.maxidx[1], self.maxidx[self.count] = self.maxidx[self.count], self.maxidx[1]
        self.maxrev[self.maxidx[1]] = 1
        self.maxrev[self.maxidx[self.count]] = 0

        #delete max element from min heap
        self.minidx[idx], self.minidx[self.count] = self.minidx[self.count], self.minidx[idx]
        self.minrev[self.minidx[idx]] = idx
        self.minrev[self.minidx[self.count]] = 0

        self.count -= 1

        self.shift_up_min(idx)
        self.shift_down_max(1)
        return res

    def remove_min(self):
        assert not self.is_empty()
        idx = self.maxrev[self.minidx[1]]
        res = self.data[self.minidx[1]]
        self.data[self.minidx[1]] = None

        self.minidx[1], self.minidx[self.count] = self.minidx[self.count], self.minidx[1]
        self.minrev[self.minidx[1]] = 1
        self.minrev[self.minidx[self.count]] = 0

        #delete max element from min heap
        self.maxidx[idx], self.maxidx[self.count] = self.maxidx[self.count], self.maxidx[idx]
        self.maxrev[self.maxidx[idx]] = idx
        self.maxrev[self.maxidx[self.count]] = 0

        self.count -= 1

        self.shift_up_max(idx)
        self.shift_down_min(1)
        return res

# def print_left(heap):
#     for i in range(1, heap.capacity+1):
#         if heap.minrev[]

if __name__ == "__main__":
    minmaxheap = MinMaxPriorityQueue(30)

    nums = []
    for i in range(7):
        ele = random.randint(0, 100)
        minmaxheap.put(ele)
        nums.append(ele)
    print(nums)
    # print(minmaxheap.get_max())
    # print(minmaxheap.get_min())

    print(minmaxheap.remove_max())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_min())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_min())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_max())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_max())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_min())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_max())
    print(minmaxheap.count)
    print(minmaxheap.data)
    print(minmaxheap.remove_min())
    print(minmaxheap.count)
    print(minmaxheap.data)
    