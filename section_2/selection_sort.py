import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort

def selection_sort(array):
    """Selection Sort sort array inplace."""
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

if __name__ == "__main__":
    n = 10000
    test_arr = generate_random_Intlist(n, 0, 10000)
    # print_list(test_arr)
    # selection_sort(test)
    test_sort("Selection Sort", selection_sort, test_arr)
    # print("After Sort:")
    # print_list(test)