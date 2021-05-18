class Solution:
    
    
    # The idea is to use a 2 pointer method
    
    def minWindow(self, S: str, T: str) -> str:
        
        # Expand and then contract is the main idea
        
        sidx, slen = 0, len(S)
        tidx, tlen = 0, len(T)
        
        ret = ''
        while sidx < slen:
            if S[sidx] == T[tidx]:
                tidx += 1
            
            if tidx == tlen: # Found the answer
                
                # Shrink to get the starting point
                end = sidx + 1
                
                # We have overshot
                while tidx > 0:
                    
                    if T[tidx - 1] == S[sidx]:
                        tidx -= 1
                    sidx -= 1
                        
                # Since we would have undershot towards the end
                sidx += 1
                
                if len(ret) == 0 or end - sidx < len(ret):
                    ret = S[sidx:end]
                    
            sidx += 1
        return ret
                
                
