class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        d = [[-1,0],[0,-1],[1,0],[0,1]]
        
        longest_path = 0
        starting = [[0]*(n) for i in range(m)]
        
        def dfs(i,j):            
            if starting[i][j] != 0:
                return starting[i][j]
            
            for dir in d:
                newx, newy = i + dir[0], j + dir[1]
                if newx >= 0 and newx < m and newy >= 0 and newy < n and matrix[newx][newy] > matrix[i][j]:
                    starting[i][j] = max(starting[i][j], dfs(newx, newy))
            starting[i][j] += 1
            return starting[i][j]
        
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i,j))

        return longest_path
