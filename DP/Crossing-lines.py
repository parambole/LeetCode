class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        l1 = len(A) + 1
        l2 = len(B) + 1
        
        dp = [[0]*l2 for i in range(l1)]
        
        
        for i in range(1, l1):
            for j in range(1, l2):
                if A[i-1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1-1][l2-1]
