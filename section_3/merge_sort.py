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
    """Insertion Sort sort array inplace."""
    n = len(array)
    __merge_sort(array, 0, n-1)

if __name__ == "__main__":
    n = 100000
    test_arr = generate_random_Intlist(n, 0, 1000)
    # test_arr = generate_nearly_odered(n, 10)
    # cp_arr = test_arr.copy()
    # print_list(test_arr)
    # selection_sort(test)
    # test_sort("Insertion Sort", insertion_sort, cp_arr)
    test_sort("Merge Sort", merge_sort, test_arr)
    # test_sort("Selection Sort", selection_sort, test_arr)

    # print("After Sort:") 
    # print_list(test_arr)