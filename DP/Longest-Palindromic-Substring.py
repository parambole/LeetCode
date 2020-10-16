class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        maxVal = 0
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                
                if s[i] == s[j] and ( j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    
                if dp[i][j] and j - i + 1 > maxVal:
                    maxVal = j - i + 1
                    start = i
                    
                
        return s[start: start + maxVal]
