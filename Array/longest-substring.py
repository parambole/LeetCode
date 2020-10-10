class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if len(s) == 0:
            return 0
        
        dic = collections.defaultdict(int)
        
        i = 0
        j = 0
        maxVal = 0
        while i < n and j < n:
            ch = s[j]
            dic[ch] += 1
            
            if dic[ch] > 1:
                rem = s[i]
                i += 1
                del dic[rem]
            else:
                j += 1
            maxVal = max(maxVal, j - i)
            
        return maxVal
