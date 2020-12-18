class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        # Remeber this is true for any combination. It should be true for any combination for mathematics
        
        dic = collections.defaultdict(int)
        
        for i in A:
            for j in B:
                res = -( i + j)
                dic[res] += 1
                
        count = 0
        for i in C:
            for j in D:
                res = i + j
                count += dic[res]
                
        return count
