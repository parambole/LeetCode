import random

class Solution:
    
    # This is not correct because we need to be random. So this is correct

    def __init__(self, w: List[int]):
        self.weighted = []
        self.weighted.append(w[0])
        
        for i in range(1, len(w)):
            self.weighted.append(self.weighted[i - 1] + w[i])
        self.n = len(self.weighted)

    def pickIndex(self) -> int:
        number = self.weighted[-1] * random.random()
        low = 0
        high = self.n - 1
        while low < high:
            mid = (low + high) // 2

            if number > self.weighted[mid]:
                low = mid + 1
            elif number < self.weighted[mid]:
                high = mid
        
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
