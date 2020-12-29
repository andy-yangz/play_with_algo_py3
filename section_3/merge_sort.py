import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort, generate_nearly_odered
from section_2.insertion_sort import insertion_sort, insertion_sort_lr

def __merge(arr, l, r, mid):
    # 一定要注意边界条件
    temp = arr[l:r+1].copy()
    i, j = l-l, mid+1-l
    for idx in range(l, r+1):
        if i > mid-l:
            arr[idx] = temp[j]
            j += 1
        elif j>r-l:
            arr[idx] = temp[i]
            i += 1
        elif temp[i] < temp[j]:
            arr[idx] = temp[i]
            i += 1
        else:
            arr[idx] = temp[j]
            j += 1
        idx += 1

def __merge_sort(arr, l, r):
    # if l >=r: return
    if r - l <= 10:
        insertion_sort_lr(arr, l, r)
        return
    mid = l + (r-l)//2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid+1, r)
    # __merge(arr, l, r, mid)
    if arr[mid] > arr[mid+1]:
        __merge(arr, l, r, mid)

def merge_sort(array):
    """Merge Sort sort array inplace."""
    n = len(array)
    __merge_sort(array, 0, n-1)

def merge_sort_BU(array):
    """Merge Sort sort array inplace from bottom up."""
    n = len(array)
    size = 1
    while size <= n:
        i = 0
        while i+size < n:
            if array[i+size-1] > array[i+size]: #We can use insertion sort to sort short list, however the speed will slower
                __merge(array, i, min(i+size+size-1, n-1), i+size-1)
            i += 2*size
        size += size

if __name__ == "__main__":
    n = 10000
    test_arr = generate_random_Intlist(n, 0, 1000)
    # test_arr = generate_nearly_odered(n, 10)
    cp_arr = test_arr.copy()
    # print_list(test_arr)
    # selection_sort(test)
    # test_sort("Insertion Sort", insertion_sort, cp_arr)
    test_sort("Merge Sort", merge_sort, test_arr)
    test_sort("Merge Sort BU", merge_sort_BU, cp_arr)
    # test_sort("Selection Sort", selection_sort, test_arr)

    # print("After Sort:") 
    # print_list(test_arr)
    # print_list(cp_arr)