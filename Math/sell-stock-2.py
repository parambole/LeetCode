class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     min = sys.maxsize
    #     max = - ( sys.maxsize + 1 )
    #     for i in range(len(prices)):
    #         if (prices[i] < min): min = prices[i]
    #         if(prices[i] - min > max): max = prices[i] - min
    #     return max
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        i = 0
        n = len(prices)
        while ( i < n ):
            for j in range(i+1, n):
                if prices[j] >= prices[i]:
                    mp += prices[j] - prices[i]
                    i = j - 1
                    break
                else:
                    break
            i += 1
        return mp
