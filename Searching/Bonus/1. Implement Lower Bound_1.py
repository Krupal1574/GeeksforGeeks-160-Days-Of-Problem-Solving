class Solution:
    def lowerBound(self, arr, target):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo