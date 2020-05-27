class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = -1
        
        count = 0
        maxSub = 0
        
        for i,num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count not in dic:
                dic[count] = i
            else:
                maxSub = max(maxSub, i - dic[count])
        return maxSub
        
