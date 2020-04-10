class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
    
        stackS = []
        
        for s in S:
            if s == '#' and not len(stackS) == 0:
                stackS.pop()
            elif s != '#':
                stackS.append(s)
        
        stackT = []
        
        for s in T:
            # back space is an operation
            if s == '#' and not len(stackT) == 0:
                stackT.pop()
            elif s != '#':
                stackT.append(s)
                
        return stackS == stackT
