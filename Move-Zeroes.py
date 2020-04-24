class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 count += 1
#         if count == len(nums):
#             return nums;
        
#         for i in range(count):
#             for j in range(len(nums) - 1):
#                 if(nums[j] == 0):
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#         return nums
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        while(count < len(nums)):
                nums[count] = 0
                count += 1
            
