class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                count = stack.pop()[1]
                count += 1
                if count != k:
                    stack.append((c, count))
            else:
                stack.append((c, 1))
        
        res = ""
        for ch, count in stack:
            res += ch * count
            
        return res
