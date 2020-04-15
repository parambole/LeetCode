class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         R = [1] * n
#         L = [1] * n
        
#         for i in range(n-2, -1, -1):
#             R[i] = R[i+1] * nums[i+1]
#         for i in range(1,n):
#             L[i] = L[i-1] * nums[i-1]
#         for i in range(n):
#             R[i] = R[i] * L[i]
#         return R
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n
        R = 1
        for i in range(1,n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(len(nums) - 1, -1, -1):
            L[i] *= R
            R *= nums[i]
        return L
