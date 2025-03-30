class Solution:
    def fizzBuzz(self, n: int):
        result = []
        
        for i in range(1, n + 1):
            current = []
            
            if i % 3 == 0:
                current.append("Fizz")
            if i % 5 == 0:
                current.append("Buzz")
            
            if not current:
                current.append(str(i))
            
            result.append("".join(current))
        
        return result