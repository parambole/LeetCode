class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = n - 2
        
        """
        j = 1
        nums[1] = 1
        nums[2] = 1
        """
        
        while j >= 0 and nums[j] >= nums[j + 1]:
            j -= 1
                        
        if j != -1:
            """
            [1,3,2]
            j = 0
            i = 2
            """
            i = n -  1

            while i > j and nums[i] <= nums[j]:
                i -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[j + 1: n] = nums[j + 1: n][::-1]
                        
            
        
