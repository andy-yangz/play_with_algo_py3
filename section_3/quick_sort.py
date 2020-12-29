import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_Intlist, print_list, is_sorted
from section_2.insertion_sort import insertion_sort, insertion_sort_lr
import random, time

def __partition1(arr, l, r):
    # 对 arr[l:r+1] 部分进行 partition 操作
    # 使得返回的位置p,arr在p左边的<arr[p],arr在p右边的>arr[p]
    # 随机选择一个位置作为 pivot，并且和开头交换
    idx = random.randint(l, r)
    arr[l], arr[idx] = arr[idx], arr[l]

    pivot = arr[l]
    j = l
    # arr[l+1..j] < pivot, arr[j+1..i] > pivot
    for i in range(l+1, r+1):
        if arr[i] < pivot:
            arr[j+1], arr[i] = arr[i], arr[j+1]
            j += 1
    arr[l], arr[j] = arr[j], arr[l]
    return j


def __partition2(arr, l, r):
    # 对 arr[l:r+1] 部分进行 partition 操作
    # 双路排序
    idx = random.randint(l, r)
    arr[l], arr[idx] = arr[idx], arr[l]

    pivot = arr[l]
    i, j = l+1, r
    # arr[l+1..i] < pivot, arr[j..r] > pivot
    while True:
        while i<=r and arr[i] < pivot:
            i += 1
        while j>=l+1 and arr[j] > pivot:
            j -= 1
        if i > j: break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[l], arr[j] = arr[j], arr[l]
    return j

def __partition3(arr, l, r):
    # 对 arr[l,r]闭区间进行三路排序
    # 返回两个分界点
    # 减少了对重复元素的排序
    idx = random.randint(l, r)
    arr[l], arr[idx] = arr[idx], arr[l]

    pivot = arr[l]
    #保证 [l+1,lt]<v, [lt+1, i-1]==v, [gt, r]>v
    lt, gt, i = l, r+1, l+1
    while i < gt:
        if arr[i] < pivot:
            arr[i], arr[lt+1] = arr[lt+1], arr[i]
            i += 1
            lt += 1
        elif arr[i] == pivot:
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            gt -= 1
    arr[l], arr[lt] = arr[lt], arr[l]
    return lt-1, gt

def __quick_sort(arr, l, r, method="one"):
    if l >= r: return
    # if r-l<=10:
    #     insertion_sort_lr(arr, l, r)
    #     return
    if method == "one": #单路排序
        q = __partition1(arr, l, r)
        __quick_sort(arr, l, q-1, method=method)
        __quick_sort(arr, q+1, r, method=method)
    elif method == "two": #双路排序
        q = __partition2(arr, l, r)
        __quick_sort(arr, l, q-1, method=method)
        __quick_sort(arr, q+1, r, method=method)
    elif method == "three": #三路排序
        lt, gt = __partition3(arr, l, r)
        __quick_sort(arr, l, lt, method=method)
        __quick_sort(arr, gt, r, method=method)
    else:
        raise Exception("Please select method between {one, two, three}")

def quick_sort(array, method):
    """Selection Sort sort array inplace."""
    n = len(array)
    __quick_sort(array, 0, n-1, method=method)

def test_sort(name, sort_func, arr, method="one"):
    start = time.time()
    sort_func(arr, method=method)
    cost_time = time.time() - start

    assert is_sorted(arr), print(arr)
    print(f"{name}: {cost_time} s")

if __name__ == "__main__":
    n = 100000
    test_arr = generate_random_Intlist(n, 0, 1000)
    arr_cp1 = test_arr.copy()
    arr_cp2 = test_arr.copy()
    # print_list(test_arr)
    # selection_sort(test)
    test_sort("Quick Sort One", quick_sort, test_arr, "one")
    test_sort("Quick Sort Two", quick_sort, arr_cp1, "two")
    test_sort("Quick Sort Three", quick_sort, arr_cp2, "three")
    # print("After Sort:")
    # print_list(test_arr)