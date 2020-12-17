import sys
import os
from selection_sort import selection_sort
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, test_sort, generate_nearly_odered

def bubble_sort(array):
    """Insertion Sort sort array inplace."""
    n = len(array)
    flag = True
    while flag:
        flag = False
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True

if __name__ == "__main__":
    n = 100
    test_arr = generate_random_Intlist(n, 0, 100)
    # test_arr = generate_nearly_odered(n, 100)
    print_list(test_arr)
    # selection_sort(test)
    test_sort("Insertion Sort", bubble_sort, test_arr)
    # test_sort("Selection Sort", selection_sort, test_arr)

    print("After Sort:") 
    print_list(test_arr)