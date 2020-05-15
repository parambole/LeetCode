class Solution:
    
    # This is n2 solution
    
#     def maxSubarraySumCircular(self, A: List[int]) -> int:
        
#         n = len(A)
        
#         maxVal = A[0]
#         for i in range(n):
#             dp = [0] * n
#             dp[0] = A[i]
            
#             for j in range(1, n):
#                 idx = (i + j) % n
#                 dp[j] = max(A[idx], dp[j-1] + A[idx])
#                 maxVal = max(maxVal, dp[j])
                
#         return maxVal
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        maxVal, minVal = A[0], A[0]
        dpMax , dpMin = [0] * n, [0] * n
        
        dpMax[0], dpMin[0] = maxVal, minVal
        
        TS = A[0]
        
        for i in range(1, n):
            TS += A[i]
            
            dpMax[i] = max(A[i], dpMax[i - 1] + A[i])
            maxVal = max(dpMax[i], maxVal)
            
            dpMin[i] = min(A[i], dpMin[i - 1] + A[i])
            minVal = min(dpMin[i], minVal)            
            
            
        return maxVal if minVal == TS else max(maxVal, TS - minVal)       
                
        
