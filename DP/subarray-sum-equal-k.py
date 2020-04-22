class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         return 1
#         n = len(nums)
#         count = 0
#         curr = 0
                
#         for i in range(n):
#             curr = 0
#             for j in range(i, n):
#                 curr += nums[j]
#                 if curr == k:
#                     count += 1
#         return count
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {}
        
        dic[0] = 1
        
        s = 0
        total = 0
        
        for num in nums:
            s += num
            
            if (s - k) in dic:
                total += dic[s-k]
            
            if s in dic:
                dic[s] = dic[s] + 1
            else:
                dic[s] = 1
            
        return total
                
        
