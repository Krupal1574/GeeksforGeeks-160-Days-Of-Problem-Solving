class Solution:
    def canAttend(self, arr):
        arr.sort(key=lambda x: x[0])  
        for i in range(len(arr) - 1):
            if arr[i][1] > arr[i + 1][0]:  
                return False
        return True