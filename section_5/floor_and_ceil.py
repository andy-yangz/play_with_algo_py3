# Floor 找到 Target 最左端
# Ceil 找到 Target 最右端


def bs_floor(arr, target):
    n = len(arr)
    l, r = 0, n-1
    while l<=r:
        m = l + (r-l)//2
        if arr[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l if arr[l]==target else l-1


def bs_ceil(arr, target):
    # 最好基于基础的二分搜索改，改动越少越好，合并一下就行
    n = len(arr)
    l, r = 0, n-1
    while l<=r:
        m = l + (r-l)//2
        if arr[m] <= target:
            l = m + 1
        else:
            r = m - 1
    return r if arr[r]==target else r+1


if __name__ == "__main__":
    arr = [1, 3, 4, 4, 6, 6, 6, 6, 7, 10, 11, 11, 20]
    floor = bs_floor(arr, 5)
    print(floor)
    print(arr[floor])
    ceil = bs_ceil(arr, 5)
    print(ceil)
    print(arr[ceil])
