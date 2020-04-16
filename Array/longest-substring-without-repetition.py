class Solution:
    
    # This stupid code is failing for spaces.  In any case
    
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     n = len(s)
    #     if s == None:
    #         return 0
    #     maxLength = 1
    #     for i in range(n):
    #         count = 1
    #         freq = [0] * 26
    #         freq[ord(s[i]) - ord('a')] = 1
    #         for j in range(i+1, n):
    #             if freq[ord(s[j]) - ord('a')] == 1:
    #                 break
    #             else:
    #                 freq[ord(s[j]) - ord('a')] = 1
    #                 count +=1
    #                 maxLength = max(maxLength, count)
    #     return maxLength
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        
        n = len(s)
        
        maxValue, i , j = 0, 0, 0
        
        while i < n and j < n:
            if s[j] not in freq:
                freq.add(s[j])
                j += 1
                maxValue = max(maxValue, j - i)
            else:
                freq.remove(s[i])
                i += 1
        return maxValue
    
                    
                
        
