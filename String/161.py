class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        # Dont USE The above method like this as the value will change
        if n > m:
            # s, t = t, s
            return self.isOneEditDistance(t,s)
        
        if n - m > 1:
            return False
        
            
            
        
        for i in range(n):
            
            if s[i] != t[i]:
                
                if n == m:
                    return s[i+1:] == t[i+1:]
                
                else:
                    return s[i:] == t[i+1:]
        
        
        # IMP step 
        
        return n + 1 == m
        
        
        
