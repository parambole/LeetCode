
# This solution is not 100 mine
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = collections.defaultdict(int)
        
        
        for nums in s:
            dic[nums] = dic[nums] + 1
        
        
        # This part i didn;t think of
        for i, nums in enumerate(s):
            if dic[nums] == 1:
                return i
        
        return -1
