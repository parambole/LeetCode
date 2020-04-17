import collections 

class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = collections.deque()
        stackStar = collections.deque()
        
        stackOpen = []
        stackS = []
        
        for i, val in enumerate(s):
            if val == '(':
                stack.append(val)
                stackOpen.append(i)
            elif val == '*':
                stackStar.append(val)
                stackS.append(i)
            elif val == ')':
                if len(stack) != 0:
                    stack.pop()
                    stackOpen.pop()
                elif len(stackStar) != 0:
                    stackStar.pop()
                    stackS.pop()
                else:
                    return False

        if len(stack) != 0 and len(stackStar) < len(stack):
            return False
        else:
            while len(stackOpen) != 0:
                x = stackOpen.pop()
                y = stackS.pop()
                if ( y < x):
                    return False
                
            return True
