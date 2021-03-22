class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        n = len(num1)
        m = len(num2)
        

        
        """
        
        i = 0
        j = 1
        
                    012
       i pointer =  123
       
                    012
       j pointer =  456
       
       
       product = 5
        
        resPos = i + j + 1 = 2
        carryPos = i + j  = 1
        
        
        temp = result[i + j + 1] + product = 1 + 5 = 6
        
        result[i + j + 1] = temp % 10 = 6 = 6
        
        result[i + j] += temp // 10 = 0 + 1
        
                 [0,1,2,3,4,5]
        result = [0,5,6,0,8,8]
        
        
        
        """
        
        # This is the main idea
        result = [0] * (n + m)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                product = int(num1[i]) * int(num2[j])
                temp = result[i + j + 1] + product
                result[i + j + 1] = temp % 10
                result[i + j] += temp // 10
                
                
        result = ''.join(map(str, result))
        return '0' if not result.lstrip('0') else result.lstrip('0')
