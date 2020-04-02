class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        for i in nums:
            val ^= i
        return val
