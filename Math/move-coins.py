class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        # This question is very mathematical
        
        # One thing we need to know is 0dd - even = odd
        # Even - even = even
        
        # so all of them can be moved to one position and then from there just take the min one
        
        even_count = 0
        odd_count = 0
        for n in position:
            if n % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            
        return min(even_count, odd_count)
