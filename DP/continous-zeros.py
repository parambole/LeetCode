class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dic = {}
        dic[0] = -1
        count = 0
        maxLength = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            if num == 1:
                count += 1
                
            # Create equation on own
            if count in dic:
                maxLength = max(maxLength, abs(i - dic[count]))
            else:
                dic[count] = i


        return maxLength
