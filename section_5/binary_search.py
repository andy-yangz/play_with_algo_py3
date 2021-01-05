import random

def binary_search_iter(arr, target):
    # 循环版本
    n = len(arr)
    #在[0, n-1]两边闭合区间查找
    l, r = 0, n-1
    while l<=r:
        m = l + (r-l)//2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m-1
        else:
            l = m+1
    return -1

def binary_search_recur(arr, target):
    # 递归版本
    if not arr: return -1
    n = len(arr)
    #在[0, n-1]两边闭合区间查找
    l, r = 0, n-1
    m = l + (r-l)//2
    if arr[m] == target:
        return m
    elif arr[m] < target:
        search = binary_search_recur(arr[m+1:], target)
        if search == -1:
            return -1
        else:
            return m + search + 1
    else:
        search = binary_search_recur(arr[:m], target)
        return search

if __name__ == "__main__":
    # arr = list(range(1,300))
    arr = sorted([random.randint(1, 100) for i in range(100)])
    print(arr)
    result = binary_search_iter(arr, 99)
    print(result)
    result = binary_search_recur(arr, 99)
    print(result)