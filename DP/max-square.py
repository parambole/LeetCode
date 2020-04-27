class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        
        r = len(matrix)
        
        if r == 0:
            return 0
        c = len(matrix[0])
        
        dp = [ [0] * c for i in range(r)]
        
        maxSquare = 0

        for i in range(r):
            if matrix[i][0] == "1":
                
                dp[i][0] = 1
                maxSquare = max(maxSquare, dp[i][0])
        for j in range(c):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                maxSquare = max(maxSquare, dp[0][j])
                
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == "1":
                    if dp[i][j-1] != 0 and dp[i-1][j] != 0 and dp[i-1][j-1] != 0:
                        
                        
                        # So since these three elements influence at any point you need the min because you can only make a square + 1
                        
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    else:  
                        dp[i][j] = 1
                maxSquare = max(dp[i][j], maxSquare)
        return maxSquare * maxSquare
                    
                    
