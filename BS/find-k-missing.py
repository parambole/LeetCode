class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        low = 0
        high = len(arr) - 1
        ans = -1 
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if arr[mid] - ( mid + 1) < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
                        
        return low + k if ans == -1 else ans + k
                
        
