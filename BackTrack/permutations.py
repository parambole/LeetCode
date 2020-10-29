class Solution:
    def backprop(self, curr, list_vale, nums, n, result):
        if len(curr) == n:
            result.append(list_vale)
            return
        
        for i in nums:
            if i not in curr:
                curr.add(i)
                self.backprop(curr, list_vale + [i], nums, n, result)
                curr.remove(i)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        self.backprop(set(), [], nums, n, result)
        return result
