class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if num == "":
            return "0"
        
        stack = []
        
        if num[0] != '0':
            stack.append(num[0])
        
        for n in range(1, len(num)):
            
            while k > 0 and len(stack) != 0 and num[n] < stack[-1]:
                    stack.pop()
                    k -= 1
                    
            if len(stack) == 0 and num[n] == '0':
                continue
            else:
                stack.append(num[n])
        print(k)
                
        if k > 0:
            while k > 0 and len(stack) != 0:
                stack.pop()
                k -= 1
                
        
        return "0" if len(stack) == 0 else "".join(stack)
