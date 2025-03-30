class Solution:
    def singleDigit(self, n):
        return 0 if n == 0 else (9 if n % 9 == 0 else n % 9)