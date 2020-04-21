# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        
        if n == 0 or m == 0:
            return -1
        
        minCol = sys.maxsize
        
        
        r = 0
        c = m - 1
        
        while r < n  and c >= 0:
            
            if binaryMatrix.get(r,c) == 0:
                r = r + 1
            elif binaryMatrix.get(r,c) == 1:
                minCol = c
                c = c - 1
        
        return minCol if minCol != sys.maxsize else -1
        
