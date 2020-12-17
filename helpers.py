import random
import time

def generate_random_Intlist(n, range_L, range_R):
    result = []
    for _ in range(n):
        result.append(random.randint(range_L, range_R))
    return result

def generate_nearly_odered(n, swap_time):
    array = list(range(n))
    for _ in range(swap_time):
        x, y = random.randint(0, n-1), random.randint(0, n-1)
        array[x], array[y] = array[y], array[x]
    return array
    
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def test_sort(name, sort_func, arr):
    start = time.time()
    sort_func(arr)
    cost_time = time.time() - start

    assert is_sorted(arr), print(arr)
    print(f"{name}: {cost_time} s")

def print_list(array):
    print(" ".join([str(ele) for ele in array]))