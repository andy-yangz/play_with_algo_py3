def reverse_pairs(nums):
    # O(n^2) 的解法
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count += 1
    return count

def __merge(nums, l, mid, r):
    array = nums[l:r+1].copy()
    count = 0
    i, j = 0, mid-l+1
    for k in range(l, r+1):
        if i > mid-l:
            nums[k] = array[j]
            j+= 1
        elif j > r-l:
            nums[k] = array[i]
            i += 1
        elif array[i] > array[j]:
            nums[k] = array[j]
            j += 1
            count += mid-l-i+1
        else:
            nums[k] = array[i]
            i += 1
    return count

def __merge_count(nums, l, r):
    if l>=r: return
    mid = l + (r-l)//2
    lc = __merge_count(nums, l, mid)
    rc = __merge_count(nums, mid+1, r)
    if nums[mid] > nums[mid+1]:
        cc = __merge(nums, l, mid, r)
    return lc + rc + cc


def reverse_pairs(nums):
    # 计算出数字序列中逆序对的数量
    n = len(nums)
    count = __merge_count(nums, 0, n-1)
    return count
    

