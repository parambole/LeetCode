class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # BEatuciful method for BS
        
        if num == 1:
            return True
        
        left = 2
        right = num // 2
        
        while left <= right:
            
            mid = (left + right) // 2
            
            sq = mid ** 2
            
            if sq == num:
                return True
            
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1
            
        return False
        
