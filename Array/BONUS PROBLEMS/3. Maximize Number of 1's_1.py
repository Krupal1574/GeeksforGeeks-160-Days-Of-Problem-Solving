class Solution:
    def maxOnes(self, arr, k):
        max_len = 0
        left = 0
        zero_count = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1

            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len