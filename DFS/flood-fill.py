class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(image, r, c, newColor, initColor):
            
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initColor:
                return
            
            image[r][c] = newColor
            
            dfs(image, r + 1 , c , newColor, initColor)
            dfs(image, r, c + 1 , newColor, initColor)
            dfs(image, r - 1 , c , newColor, initColor)
            dfs(image, r , c - 1 , newColor, initColor)
            
        
        if len(image) == 0:
            return image
        
        
        # Very very imp to realise that we need to always mark the visiting node and if it's the same then oops there is an error 
        if image[sr][sc] == newColor:
            return image
        
        dfs(image, sr, sc, newColor, image[sr][sc])
        
        return image
