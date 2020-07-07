class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        n = len(grid)
        if n == 0:
            return self.count
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.dfs(grid,n,m,i,j)
                    break
        return self.count
    
    def dfs(self,grid,n,m,r,c):
        if r < 0 or c < 0 or r >= n or c >=m or grid[r][c] != 1:
            return
        
        grid[r][c] = 2
        
        if r == 0 or grid[r-1][c] == 0: 
            self.count += 1
        if r == n-1 or grid[r+1][c] == 0:
            self.count += 1
        if c == 0 or grid[r][c-1] == 0:
            self.count += 1
        if c == m-1 or grid[r][c+1] == 0:
            self.count += 1
            
        self.dfs(grid,n,m,r-1,c)
        self.dfs(grid,n,m,r+1,c)
        self.dfs(grid,n,m,r,c-1)
        self.dfs(grid,n,m,r,c+1)
