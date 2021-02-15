class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_count = collections.defaultdict(int)
        s_count = collections.defaultdict(int)
        
        res = []

            
        np = len(p)
        ns = len(s)
        
        if ns < np:
            return res
        
        for ch in p:
            p_count[ch] += 1        
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            
            if i >= np:
                s_count[s[i - np]] -= 1
                if s_count[s[i - np]] == 0:
                    del s_count[s[i - np]]
                    
            if p_count == s_count:
                res.append(i - np + 1)
                
        return res    
