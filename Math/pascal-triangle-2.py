# First time did try run with nikitas help thank you so much :)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 1
        prev = 1
        result = [prev]        
        while i <= rowIndex:
            temp = int(prev * (rowIndex-i+1)/i)
            result.append(temp)
            prev = temp
            i += 1
        
        return result
