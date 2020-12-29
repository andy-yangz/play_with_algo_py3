import random

class IndexMaxHeap:
    """
    Index Max Heap data structure.
    """
    def __init__(self, capacity, arr=None):
        if arr is None:
            self.data = [None] * (capacity+1)
            self.indexs = [None] * (capacity+1) #index列表
            self.reverse = [0] * (capacity+1) #反向列表
            self.count = 0
            self.capacity = capacity
        else:
            self.data = [None] + arr
            self.count = len(arr)
            self.capacity = capacity
            #Heapify
            for i in range(self.count//2, 0, -1):
                self.shift_down(i)
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count==0

    def shift_up(self, k):
        while k > 1 and (self.data[self.indexs[k]] > self.data[self.indexs[k//2]]):
            self.indexs[k], self.indexs[k//2] = self.indexs[k//2], self.indexs[k]
            self.reverse[self.indexs[k]] = k
            self.reverse[self.indexs[k//2]] = k//2
            k = k//2

    def shift_down(self, k):
        while 2*k <= self.count:
            j = 2*k #left child position
            if j+1 <= self.count and self.data[self.indexs[j]] < self.data[self.indexs[j+1]]:
                j += 1
            
            if self.data[self.indexs[j]] <= self.data[self.indexs[k]]:
                break
            self.indexs[j], self.indexs[k] = self.indexs[k], self.indexs[j]
            self.reverse[self.indexs[j]] = j
            self.reverse[self.indexs[k]] = k
            k = j

    # For user i from 0, so we need add 1 inside
    def insert(self, i, ele):
        assert(self.count+1 <= self.capacity)
        assert(i+1>=1 and i+1<=self.capacity)

        i += 1
        self.data[i] = ele
        self.indexs[self.count+1] = i
        self.reverse[i] = self.count+1
        self.count += 1
        self.shift_up(self.count)

    def extract_max(self):
        assert self.count>0
        res = self.data[self.indexs[1]]
        self.indexs[1], self.indexs[self.count] = self.indexs[self.count], self.indexs[1]
        self.reverse[self.indexs[1]] = 1
        self.reverse[self.indexs[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return res
    
    def extract_max_index(self):
        assert self.count>0
        res = self.indexs[1] - 1
        self.indexs[1], self.indexs[self.count] = self.indexs[self.count], self.indexs[1]
        self.reverse[self.indexs[1]] = 1
        self.reverse[self.indexs[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return res

    def contain(self, i):
        #是否数据包含当前idx
        return self.reverse[i+1] != 0

    def get_item(self, i):
        assert self.contain(i), print("Not Contain this idx")
        return self.data[i+1]
    
    def change(self, i, ele):
        assert self.contain(i)
        i += 1
        self.data[i] = ele

        # for j in range(self.count):
        #     if self.indexs[j] == i:
        #         self.shift_up(j)
        #         self.shift_down(j)
        j = self.reverse[i]
        self.shift_up(j)
        self.shift_down(j)


if __name__ == "__main__":
    imaxheap = IndexMaxHeap(50)
    nums = []
    for i in range(30):
        ele = random.randint(0, 100)
        imaxheap.insert(i, ele)
        nums.append(ele)
    # print("Data: ", nums)
    # print_tree(maxheap.data)
    # while (not imaxheap.is_empty()):
    #     print(imaxheap.extract_max())
    print(imaxheap.extract_max())
    print(imaxheap.extract_max())
    print(imaxheap.indexs)
    print(imaxheap.reverse)
    imaxheap.change(3, 101)
    print(imaxheap.indexs)
    print(imaxheap.reverse)
    # print(imaxheap.data)
    # print(imaxheap.count)