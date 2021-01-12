import random

def print_indexheap_tree(idxheap):
    n = len(idxheap.indexs)
    i = 1
    while i < n:
        res = []
        for j in idxheap.indexs[i:i*2]:
            if j:
                res.append(str(idxheap.data[j]))
        print(" ".join(res))
        i = i*2 

class IndexMinHeap:
    def __init__(self, capacity, arr=None):
        if arr is None:
            self.data = [None] * (capacity+1)
            self.capacity = capacity
            self.count = 0
            self.indexs = [None] * (capacity+1) #Index 列表
            self.reverse = [0] * (capacity+1) # 反向列表
        else:
            self.data = [None] + arr
            self.count = capacity
            #heapify
            for i in range((self.count-1)//2, 0, -1):
                self.shift_down(i)

    def shift_up(self, k):
        item = self.data[self.indexs[k]]
        idx = self.indexs[k]
        while k > 1 and item < self.data[self.indexs[k//2]]:
            self.indexs[k] = self.indexs[k//2]
            self.reverse[self.indexs[k]] = k
            k = k//2
        self.indexs[k] = idx
        self.reverse[idx] = k
    
    def shift_down(self, k):
        item = self.data[self.indexs[k]]
        idx = self.indexs[k]
        while 2*k <= self.count:
            j = 2*k
            if j+1<=self.count and self.data[self.indexs[j]] > self.data[self.indexs[j+1]]:
                j += 1
            
            if item <= self.data[self.indexs[j]]: break
            self.indexs[k] = self.indexs[j]
            self.reverse[self.indexs[k]] = k
            k = j
        self.indexs[k] = idx
        self.reverse[idx] = k


    def is_empty(self):
        return self.count==0
    
    def size(self):
        return self.count

    # For user i is from 0, but in heap from 1
    def insert(self, i, ele):
        assert self.count<=self.capacity
        assert i+1>=1 and i+1<=self.capacity

        i += 1
        self.data[i] = ele
        self.indexs[self.count+1] = i
        self.reverse[i] = self.count+1
        self.count += 1
        self.shift_up(self.count)
    
    def extract_min(self):
        assert not self.is_empty()

        res = self.data[self.indexs[1]]
        self.indexs[1], self.indexs[self.count] = self.indexs[self.count], self.indexs[1]
        self.reverse[self.indexs[1]] = 1
        self.reverse[self.indexs[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return res
    
    def extract_min_index(self):
        assert not self.is_empty()

        res = self.indexs[1]-1
        self.indexs[1], self.indexs[self.count] = self.indexs[self.count], self.indexs[1]
        self.reverse[self.indexs[1]] = 1
        self.reverse[self.indexs[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return res
    
    def contain(self, i):
        return self.reverse[i+1] != 0
    
    def get_item(self, i):
        assert self.contain(i), print("Not Contain this idx")
        return self.data[i+1]

    def change(self, i, ele):
        assert self.contain(i), print("Not Contain this idx")
        i += 1
        self.data[i] = ele
        j = self.reverse[i]
        self.shift_up(j)
        self.shift_down(j)

if __name__ == "__main__":
    iminheap = IndexMinHeap(30)
    # print(minheap.data, minheap.capacity, minheap.count)
    # for i in range(20):
    #     iminheap.insert(i, random.randint(0, 100))
    # print_indexheap_tree(iminheap)

    nums = []
    for i in range(10):
        ele = random.randint(0, 100)
        iminheap.insert(i, ele)
        nums.append(ele)
    print(nums)
    print(iminheap.data[iminheap.indexs[1]])
    # iminheap = IndexMinHeap(30, nums)
    # print("Data: ", nums)
    # print_tree(imaxheap.data)
    # print_indexheap_tree(iminheap)
    # while (not iminheap.is_empty()):
    #     index = iminheap.extract_min_index()
    #     print("Index: ", index)
    #     print(nums[index])

    # print(iminheap.extract_min())
    # print(iminheap.indexs)
    # print(iminheap.reverse)
    # print(iminheap.data)
    # iminheap.change(3, 2)
    # print(iminheap.indexs)
    # print(iminheap.reverse)
    # print(iminheap.data)
    # while (not minheap.is_empty()):
    #     print(minheap.extract_min())
    # print(maxheap.size())
    # print(maxheap.data)