class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
                
                    
        minSum = 0
        costs.sort(key=lambda x: x[1] - x[0])
        n = N//2
        for i in range(n):
            minSum += costs[i][1] + costs[i+n][0]
            
        
        return minSum
        
