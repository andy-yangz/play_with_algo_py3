import sys
import os
from .selection_sort import selection_sort
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort, generate_nearly_odered

def insertion_sort(array):
    """Insertion Sort array inplace."""
    n = len(array)
    for i in range(1, n):
        cur = array[i]
        for j in range(i, -1, -1):
            if cur < array[j-1] and j>0:
                array[j] = array[j-1]
            else:
                break
        array[j] = cur

def insertion_sort_lr(array, l, r):
    """Insertion Sort at the range [l, r] of array."""
    for i in range(l, r+1):
        cur = array[i]
        for j in range(i, l-1, -1):
            if cur < array[j-1] and j>l:
                array[j] = array[j-1]
            else:
                break
        array[j] = cur

if __name__ == "__main__":
    n = 10000
    # test_arr = generate_random_Intlist(n, 0, 100)
    test_arr = generate_nearly_odered(n, 100)
    # print_list(test_arr)
    # selection_sort(test)
    test_sort("Insertion Sort", insertion_sort, test_arr)
    test_sort("Selection Sort", selection_sort, test_arr)

    # print("After Sort:") 
    # print_list(test_arr)