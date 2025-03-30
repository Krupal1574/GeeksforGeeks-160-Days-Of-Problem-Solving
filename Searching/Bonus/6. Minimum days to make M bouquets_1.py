class Solution:
    def minDaysBloom(self, m, k, arr):
        if m * k > len(arr): return -1

        low, high = 1, max(arr)
        while low < high:
            mid = (low + high) // 2
            cnt = parts = 0
            for n in arr:
                cnt = cnt + 1 if n <= mid else 0
                if cnt == k:
                    parts += 1
                    cnt = 0
            if parts < m: low = mid + 1
            else: high = mid
        return low