class Solution:

    def findMaximum(self, arr):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo]