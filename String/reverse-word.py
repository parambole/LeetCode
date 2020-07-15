class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        i = 0
        for i in range(len(words) - 1, -1, -1):
            result += words[i] + " "
        return result.strip()
