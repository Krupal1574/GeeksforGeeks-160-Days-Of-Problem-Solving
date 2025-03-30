class Solution:
    def convertToWords(self, n: int) -> str:
        belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        belowHundred = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def convertWords(num):
            if num == 0:
                return ""
            if num < 10:
                return belowTen[num]
            if num < 20:
                return belowTwenty[num - 10]
            if num < 100:
                return belowHundred[num // 10] + ("" if num % 10 == 0 else " " + convertWords(num % 10))
            if num < 1000:
                return convertWords(num // 100) + " Hundred" + ("" if num % 100 == 0 else " " + convertWords(num % 100))
            if num < 1000000:
                return convertWords(num // 1000) + " Thousand" + ("" if num % 1000 == 0 else " " + convertWords(num % 1000))
            if num < 1000000000:
                return convertWords(num // 1000000) + " Million" + ("" if num % 1000000 == 0 else " " + convertWords(num % 1000000))
            return convertWords(num // 1000000000) + " Billion" + ("" if num % 1000000000 == 0 else " " + convertWords(num % 1000000000))

        if n == 0:
            return "Zero"
        return convertWords(n)