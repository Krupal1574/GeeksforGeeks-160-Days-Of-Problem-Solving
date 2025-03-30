class Solution:
    
    def findSplit(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target = total_sum // 3
        current_sum = 0
        first_split = -1
        second_split = -1
        
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum == target:
                first_split = i
                break
        
        if first_split == -1:
            return [-1, -1]
        
        current_sum = 0
        
        for i in range(first_split + 1, len(arr)):
            current_sum += arr[i]
            if current_sum == target:
                second_split = i
                break
        
        if second_split != -1:
            return [first_split, second_split]
        return [-1, -1]