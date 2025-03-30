class Solution:
    def longestPrefixSuffix(self, s: str) -> int:
        n = len(s)
        lps = [0] * n  

        len_ = 0  
        i = 1 

        while i < n:
            if s[i] == s[len_]:
                len_ += 1
                lps[i] = len_  
                i += 1
            else:
                if len_ != 0:
                    len_ = lps[len_ - 1]  
                else:
                    lps[i] = 0  
                    i += 1

        return lps[n - 1]