import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            # Becareful while extraction of -negative
            if y != x:
                heapq.heappush(stones, (x-y))
        
        if len(stones) == 0:
            return 0
        else:
            return -1 * heapq.heappop(stones)
