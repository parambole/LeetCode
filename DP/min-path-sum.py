class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        dp = [ [0]*m for i in range(n)]
        

        
        
        dp[0][0] = grid[0][0]
        
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1,m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
            
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n-1][m-1]
        
        
        
                


            
            
            
# DFS IS NOT RIGHT THINK WHY
        
#         self.minPath = sys.maxsize
#         if len(grid) == 0:
#             return self.minPath
        
#         n = len(grid)
#         m = len(grid[0])
        
#         self.dfs(0,0,n,m,grid,0)
                
#         return self.minPath
    
#     def dfs(self, r, c, n , m, grid, val):
        
#         if r < 0 or r >= n or c < 0 or c >= m:
#             return
        
#         temp = grid[r][c]
        
        
#         val += temp
        
#         if r == n-1 and c == m-1:
#             self.minPath = min(self.minPath, val)
        
#         self.dfs(r , c + 1 , n, m, grid, val)
#         self.dfs(r + 1, c , n, m, grid, val)
        
        
        
                
                
            
