

# Try this again
class Solution:
        def minimumEffortPath(self, heights: List[List[int]]) -> int:
            m = len(heights)
            n = len(heights[0])
            self.dir = [[-1,0],[0,-1],[1,0],[0,1]]

            def is_possible(i,j,max_effort):
                if i == m-1 and j == n-1:
                    return True

                visited[i][j] = True
                for x,y in self.dir:
                    new_i = i + x
                    new_j = j + y
                    if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j] and abs(heights[new_i][new_j] - heights[i][j]) <= mid:
                        if is_possible(new_i, new_j, max(max_effort, abs(heights[new_i][new_j] - heights[i][j]))):
                            return True

            lo = 0
            hi = 10000000
            ans = -1
            while lo <= hi:
                mid = (lo+hi)//2
                visited = [[False] * n for i in range(m)]
                if is_possible(0,0,0):
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:  
        
        
#         def dfs(i, j, path_cost, max_diff):
#             if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
#                 return False
            
            
#             visited[i][j] = True
                        
#             max_diff = max(max_diff, abs(heights[i][j] - path_cost))
            
#             if max_diff > max_effort:
#                 return False  
            
#             if i == n - 1 and j == m - 1:
#                 return True
            
                        
#             dir = [(-1,0), (0,-1), (1,0),(0,1)]
#             for x, y in dir:
#                 if dfs(i + x, j + y, heights[i][j], max_diff):
#                     return True            
            
        
#         low = 0
#         high = 10000000
#         ans = -1 
#         n = len(heights)
#         m = len(heights[0])
        
#         while low <= high:
#             max_effort = ( low + high ) // 2
#             visited = [[False] * m for _ in range(n)]
#             if dfs(0,0, heights[0][0], 0):
#                 ans = max_effort
#                 high = max_effort - 1
#             else:
#                 low = max_effort + 1
#         return ans 
        
        
        
        # This is a TLE solution BUT own code
        
        
#         def dfs(i, j, path_cost, max_diff):

#             if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] == -1:
#                 return
            
#             temp = heights[i][j]
            
#             max_diff = max(max_diff, abs(temp - path_cost))
            
#             heights[i][j] = -1
            
#             if i == len(heights) - 1 and j == len(heights[0]) - 1:
#                 self.min_value = min(self.min_value, max_diff)
                
            
#             dir = [(-1,0), (0,-1), (1,0),(0,1)]
#             for x, y in dir:
#                 dfs(i + x, j + y, temp, max_diff)
            
            
#             # Check if this is at the right location
#             heights[i][j] = temp
            
#         self.min_value = sys.maxsize
#         dfs(0,0, heights[0][0], 0)
#         return self.min_value



