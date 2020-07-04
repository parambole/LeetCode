import heapq 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        li = [2,3,5]
        result = {1,}
        heapq.heapify(li)
        num = 1
        while len(result) != n:
            num = heapq.heappop(li)
            if num not in result:
                result.add(num)
                for i in [2 , 3, 5]:
                    new = num * i
                    heapq.heappush(li,new)
        return num
