class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        
        c = collections.Counter(s)
        
        oddCounter = 0
        
        for i in c.values():
            if i % 2 != 0:
                oddCounter += 1
                
        return True if oddCounter <= k else False
