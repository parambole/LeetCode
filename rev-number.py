class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        isNeg = True if x < 0 else False
        x = -x if isNeg else x
        while x:
            #  Python is not strongly typed language
            # if temp // 10 != rev:
            #     return 0
            rev = rev * 10 + x % 10
            if  rev > pow(2,31):
                return 0
            x //= 10

        return -rev if isNeg else rev
