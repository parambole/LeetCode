from itertools import combinations
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        combs = combinations([p1,p2,p3,p4], 2)
        dic = collections.defaultdict(int)
        for c in combs:
            dic[self.getDistance(c)] += 1
        return set(dic.values()) == set([4,2])
            
    
    def getDistance(self, c):
        return (c[0][0] - c[1][0])**2 + (c[0][1] - c[1][1])**2
