class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        while y:
            answer = x ^ y
            carry  = (x & y) << 1
            x , y = answer, carry
        return bin(x)[2:]
#         numa = 0
#         numb = 0
        
#         for i in range(len(a)):
#             if a[-1 - i] == '1':
#                 numa += 2 ** i
            
#         for i in range(len(b)):
#             if b[-1 - i] == '1':
#                 numb += 2 ** i 
                
#         return bin(numa + numb).replace("0b", "")
        
    
    
