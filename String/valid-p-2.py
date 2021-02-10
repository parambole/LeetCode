class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        i = 0
        j = len(s) - 1
        
        def isPalin(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1
            return True
            
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalin(s, i + 1, j) or isPalin(s, i, j - 1)
                
        
        return True
