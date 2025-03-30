class Solution:
    def kokoEat(self, arr, k):
        l, h = 1, max(arr)
        while l < h:
            mid = l + (h - l) // 2
            sum_parts = sum((p + mid - 1) // mid for p in arr)
            if sum_parts <= k:
                h = mid
            else:
                l = mid + 1
        return l