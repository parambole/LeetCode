import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        li = []
        heapq.heapify(li)
        
        for point in points:
            dis = point[0] ** 2 + point[1] ** 2
            heapq.heappush(li,(-dis,point))
            
            
            if len(li) > K:
                heapq.heappop(li)
                
                
        return [ p[1] for p in li]
            
