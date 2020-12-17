import sys
import os
from selection_sort import selection_sort
from insertion_sort import insertion_sort

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort, generate_nearly_odered

def shell_sort(array):
    """Insertion Sort sort array inplace."""
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            cur = array[i]
            for j in range(i, -1, -gap):
                if cur < array[j-gap] and j>0:
                    array[j] = array[j-gap]
                else:
                    break
            array[j] = cur
        gap //= 2

if __name__ == "__main__":
    n = 10000
    test_arr = generate_random_Intlist(n, 0, 1000)
    # test_arr = generate_nearly_odered(n, 100)
    # print_list(test_arr)
    # selection_sort(test)
    # test_arr1, test_arr2 = test_arr.copy(), test_arr.copy()
    # test_sort("Insertion Sort", insertion_sort, test_arr)
    # test_sort("Selection Sort", selection_sort, test_arr1)
    test_sort("Shell Sort", shell_sort, test_arr)

    # print("After Sort:") 
    # print_list(test_arr)
