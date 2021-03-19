class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        
        for i, c in enumerate(cost):
            if i < 2:
                dp[i] = c
                
            dp[i] = min(dp[i-1], dp[i-2]) + c
            
        return min(dp[n - 1], dp[n - 2])
