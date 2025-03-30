class Solution:
    def findLargest(self, arr):
        arr = sorted(map(str, arr), key=lambda x: x * 10, reverse=True)
        if arr[0] == "0":
            return "0"
        return ''.join(arr)