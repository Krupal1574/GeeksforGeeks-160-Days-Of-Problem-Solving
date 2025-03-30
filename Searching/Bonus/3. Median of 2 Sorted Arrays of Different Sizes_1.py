class Solution:
    def medianOf2(self, a, b):
        if len(a) > len(b):
            return self.medianOf2(b, a)
        
        n, m = len(a), len(b)
        lo, hi = 0, n

        while lo <= hi:
            mid1 = lo + (hi - lo) // 2
            mid2 = (n + m + 1) // 2 - mid1

            l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
            r1 = float('inf') if mid1 == n else a[mid1]
            l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
            r2 = float('inf') if mid2 == m else b[mid2]

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1

        return 0.0