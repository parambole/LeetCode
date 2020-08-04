import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]+', '', s)
        temp = s[::-1]
        return s == temp
