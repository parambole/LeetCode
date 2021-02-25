class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        output = []
        
        
        def removeHelper(s, output, iStart, jStart, openB, closeB):
            numOpen = 0
            numClosed = 0
            
            for i in range(iStart, len(s)):
                if s[i] == openB:
                    numOpen += 1
                if s[i] == closeB:
                    numClosed += 1
                    
                if numClosed > numOpen:
                    for j in range(jStart, i + 1):
                        if s[j] == closeB and ( j == jStart or s[j -1] != s[j]):
                            removeHelper(s[:j] + s[j+1:],output, i, j, openB, closeB)
                            
                    return
                
                
                
            
            rev = s[::-1]
            
            if (openB == '('):
                removeHelper(rev, output, 0, 0, ')', '(')
            else:
                output.append(rev)
        
        
        
        removeHelper(s, output, 0, 0, '(', ')')

        
        
        return output
