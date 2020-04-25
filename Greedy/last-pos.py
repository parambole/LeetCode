class Solution:
#     def canJump(self, nums: List[int]) -> bool:
        
#         n = len(nums)
#         dp = [False] * n
        
#         dp[0] = True
        
#         tracker = set()
                
#         for j in range(1, nums[0] + 1):
#             tracker.add( 0 + j )
        
#         for i in range(1, n):
#             if i in tracker:
#                 dp[i] = True
#                 for j in range(1, nums[i] + 1):
#                     tracker.add( i + j )
#             else:
#                 dp[i] = False
#         return dp[-1]

    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        lastpos = n-1 
        
        for i in range(n-1, -1, -1):
            
            # Can I take a bigger num in this range. This is a smarter way of doing it
            if i + nums[i] >= lastpos:
                lastpos = i
            
        return lastpos == 0
