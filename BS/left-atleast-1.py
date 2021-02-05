# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        min_col = col
        for r in range(row):
            low = 0
            high = col - 1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                if binaryMatrix.get(r, mid) == 1:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
                    
            
            if ans != -1:
                min_col = min(min_col, ans)
                
        return -1 if min_col == col else min_col
