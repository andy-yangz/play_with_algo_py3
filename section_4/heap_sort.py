import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort, generate_nearly_odered
from maxheap import MaxHeap

def heap_sort1(arr):
    n = len(arr)
    maxheap = MaxHeap(n)
    for i in range(n):
        maxheap.insert(arr[i])
    for i in range(n-1, -1, -1):
        arr[i] = maxheap.extract_max()

def heap_sort2(arr):
    n = len(arr)
    maxheap = MaxHeap(n, arr)
    for i in range(n-1, -1, -1):
        arr[i] = maxheap.extract_max()

def __shift_down(arr, n, k):
    while 2*k+1 < n:
        j = 2*k+1 #left child position
        if j+1 < n and arr[j] < arr[j+1]:
            j += 1
        
        if arr[j] <= arr[k]:
            break
        arr[j], arr[k] = arr[k], arr[j]
        k = j

#原地堆排序
def heap_sort(arr):
    n = len(arr)
    #heapify
    for i in range((n-1-1)//2, -1, -1):
        __shift_down(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __shift_down(arr, i, 0)

if __name__ == "__main__":
    n = 1000000
    test_arr = generate_random_Intlist(n, 0, 1000)
    # test_arr = generate_nearly_odered(n, 10)
    # cp_arr = test_arr.copy()
    # cp_arr2 = test_arr.copy()
    # print_list(test_arr)
    # selection_sort(test)
    # test_sort("Insertion Sort", insertion_sort, cp_arr)
    test_sort("Heap Sort1: ", heap_sort1, test_arr)
    # test_sort("Heap Sort2: ", heap_sort2, cp_arr)
    # test_sort("Heap Sort3: ", heap_sort, cp_arr2)

    # print(test_arr)
    # test_sort("Merge Sort BU", merge_sort_BU, cp_arr)