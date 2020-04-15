class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in range(0, len(shift)-1):
            if shift[i][0] == shift[i+1][0]:
                shift[i+1][1] = shift[i+1][1] + shift[i][1]
            else:
                if shift[i][1] > shift[i+1][1]:
                    shift[i+1][1] = shift[i][1] - shift[i+1][1]
                    shift[i+1][0] = shift[i][0]
                elif shift[i][1] < shift[i+1][1]:
                    shift[i+1][1] = shift[i+1][1] - shift[i][1]
                elif shift[i][1] == shift[i+1][1]:
                    shift[i+1][1] = 0
        if(shift[-1][1] > len(shift)):
            shift[-1][1] = shift[-1][1]%len(shift)
        
        if(shift[-1][0] == 0):
            return self.leftShift(s, shift[-1][1])
        else:
            return self.rightShift(s, shift[-1][1])
                    
    def leftShift(self, s: str, count: int):
        return s[count:] + s[:count]
        
    
    def rightShift(self, s: str, count: int):
        return s[len(s) - count:] + s[:len(s) - count]
        
                
                    
