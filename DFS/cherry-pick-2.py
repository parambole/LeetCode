class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        num_row, num_col = len(grid), len(grid[0])    
        
        @lru_cache(None)
        def helper(row, col1, col2):
            
            cherries = 0
            cherries += grid[row][col1]
            
            if col1 != col2:
                cherries += grid[row][col2]
                
            
            if row == num_row - 1:
                return cherries
            
            temp = 0
            for m1 in (col1, col1 - 1, col1 + 1):
                for m2 in (col2, col2 - 1, col2 + 1):
                    if m1 >= 0 and m2 >= 0 and m1 < num_col and m2 < num_col:
                        temp = max(temp, helper(row + 1, m1, m2))
                        
            return cherries + temp                    
        return helper(0,0,num_col-1)
