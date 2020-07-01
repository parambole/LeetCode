class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        
        while low <= high:
            mid = ( low + high ) // 2
            coins  = (( mid * ( mid + 1)) // 2)
            if n == coins:
                return mid
            elif n > (( mid * ( mid + 1)) // 2):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1
