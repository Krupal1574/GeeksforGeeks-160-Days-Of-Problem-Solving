class Solution:
    
    def camelCase(self, arr, pat):
        res = []
        for word in arr:
            j = 0
            for i in range(len(word)):
                if word[i].isupper():
                    if j < len(pat) and word[i] == pat[j]:
                        j += 1
                    elif j < len(pat):
                        break
            if j == len(pat):
                res.append(word)
        return res