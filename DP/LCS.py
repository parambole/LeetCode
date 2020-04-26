class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # This we are initialling the empty
        dp = [ [0]* (m+1) for i in range(n+1)]
        
        for i in range(1, n +1):
            for j in range(1, m + 1):
                if text2[j - 1] == text1[i - 1]:
                    
                    # This is because when they are the same we say reduce the subproblem to move the pointer for both
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # move one character each and check because we want to maximexe our changes
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
                    
        return dp[n][m]
                
    
