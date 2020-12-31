from index_maxheap import IndexMaxHeap
import random

def print_indexheap_tree(idxheap):
    n = len(idxheap.indexs)
    indexs = idxheap.indexs[:idxheap.count+1]
    i = 1
    while i < n:
        res = []
        for j in indexs[i:i*2]:
            if j:
                res.append(str(idxheap.data[j]))
        print(" ".join(res))
        i = i*2 

class PriorityQueue:
    def __init__(self, size=10):
        self.heap = IndexMaxHeap(size)

    def insert(self, p):
        self.heap.insert_ele(p)

    def extract_max(self):
        return self.heap.extract_max()

    def remove(self, i):
        self.heap.remove(i)

    def get_max(self):
        return self.heap.data[self.heap.indexs[1]]

    def changePriority(self, i, p):
        self.heap.change(i, p)

if __name__ == "__main__":
    # imaxheap = IndexMaxHeap(50)
    prior_queue = PriorityQueue()
    prior_queue.insert(45)
    prior_queue.insert(20)
    prior_queue.insert(14)
    prior_queue.insert(12)
    prior_queue.insert(31)
    prior_queue.insert(7)
    prior_queue.insert(11)
    prior_queue.insert(13)
    prior_queue.insert(7)

    print("PriorityQueue: ")
    print_indexheap_tree(prior_queue.heap)

    print("Node with maximum priority: ", prior_queue.extract_max())

    print("PriorityQueue After Extract Maximum: ")
    print_indexheap_tree(prior_queue.heap)

    prior_queue.changePriority(2, 49)
    print("PriorityQueue After Change: ")
    print_indexheap_tree(prior_queue.heap)

    prior_queue.remove(3)
    print("PriorityQueue After Remove:")
    print_indexheap_tree(prior_queue.heap)
    # nums = []
    # for i in range(30):
    #     ele = random.randint(0, 100)
    #     # imaxheap.insert(i, ele)
    #     nums.append(ele)
    # imaxheap = IndexMaxHeap(30, nums)
    # print("Data: ", nums)
    # print_tree(imaxheap.data)
    # while (not imaxheap.is_empty()):
    #     index = imaxheap.extract_max_index()
    #     print("Index: ", index)
    #     print(nums[index])
    # print(imaxheap.extract_max())
    # print(imaxheap.extract_max())
    # print(imaxheap.indexs)
    # print(imaxheap.reverse)
    # imaxheap.change(3, 101)
    # print(imaxheap.indexs)
    # print(imaxheap.reverse)
    # print(imaxheap.data)