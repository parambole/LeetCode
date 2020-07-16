class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mypower(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                y = mypower(x, n/2)
                return y * y
            else:
                return x * mypower(x, n-1)
            
        if n < 0:
            return 1/mypower(x,n * -1)
        else:
            return mypower(x,n)
