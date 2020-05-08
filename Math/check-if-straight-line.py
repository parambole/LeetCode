class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n < 2:
            return False
        # y = mx + c
        
        # when ever there is division check if its not zer0
        if (coordinates[0][0] - coordinates[1][0]) == 0:
            return False
        
        m = ((coordinates[0][1] - coordinates[1][1]) // (coordinates[0][0] - coordinates[1][0]))
        
        c = coordinates[0][1] - m * coordinates[0][0]
        
        for i in range(1, n):
            if (coordinates[i][1] - m * coordinates[i][0]) != c:
                return False
        return True
            
