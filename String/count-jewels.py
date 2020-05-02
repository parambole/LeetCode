class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel = set(J)
        
        return sum(s in jewel for s in S)

        
        
#         jewel = set()
        
#         count = 0
        
#         for s in J:
#             jewel.add(s)
            
#         for s in S:
#             if s in jewel:
#                 count += 1
                
#         return count
