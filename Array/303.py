class NumArray:

    def __init__(self, nums: List[int]):
        # self.prefix = { -1: 0}
        # for i in range(n):
        #     self.prefix[i] = self.prefix[i - 1] + nums[i]
    
        n = len(nums)
        self.prefix = [0]
        for i in range(n):
            self.prefix.append(self.prefix[i] + nums[i])
        
        
    def sumRange(self, left: int, right: int) -> int:
        
        # return self.prefix[right] - self.prefix[left - 1]
        return self.prefix[right + 1] - self.prefix[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
