import random

class Solution:
    def __quick_sort(self, arr, l, r):
        idx = random.randint(l, r)
        arr[l], arr[idx] = arr[idx], arr[l]

        pivot = arr[l]
        i, j =  l+1, r
        while True:
            while i<=r and arr[i] < pivot:
                i += 1
            while j>=l+1 and arr[j] > pivot:
                j -= 1
            if i>j: break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        arr[l], arr[j] = arr[j], arr[l]
        return j

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if not arr: return []
        if not k: return []
        if k>=len(arr): return arr
        l, r = 0, len(arr)-1
        j = -1
        while j != k:
            j = self.__quick_sort(arr, l, r)
            if j > k:
                r = j - 1
            elif j < k:
                l = j + 1
        return arr[:j]