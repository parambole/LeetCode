class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day = set(days)
        dp = [ 0  for i in range(days[-1]+1)]
        
        for i in range(days[-1]+1):
            if i in day:
                dp[i] = min( dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2],   dp[max(0, i-1)] + costs[0])
            else:
                dp[i] = dp[i-1]
                
        return dp[-1]
