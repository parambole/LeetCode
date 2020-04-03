class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while n != 1:
            if dict.get(n):
                return False;
            else:
                dict[n] = 1
            temp = n
            n = 0
            while  temp > 0 : 
                n += (temp % 10)**2
                temp //= 10
        return True
        
