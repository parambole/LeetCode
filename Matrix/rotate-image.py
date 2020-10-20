# Best link to do it https://www.youtube.com/watch?v=SA867FvqHrM or study

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                
                top = matrix[i][j]
                
                # move left to top
                matrix[i][j] = matrix[n - 1 - j][i]
                
                # moving bottom to left
                matrix[n - 1 - j][i] = matrix[n - i - 1][n - 1 - j] 
                
                # moving bottom to right to bottom
                matrix[n - i - 1][n - 1 - j] = matrix[j][n - i - 1]
                
                #move top to right
                matrix[j][n - i - 1] = top
