class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0:
            i += 1
            
        l = i - 1
        h = i 
        
        res = []
        
        while l >= 0 or h < n:
            
            """
            
            This is a better way of merging two lists
            
            But need to understand why didn't we put a condition on l
            
            """
            if h >= n or abs(nums[l]) < abs(nums[h]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[h] ** 2)
                h += 1
                
        return res
