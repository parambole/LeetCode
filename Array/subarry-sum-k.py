class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_till_now = 0
        count = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        
        
        for i, n in enumerate(nums):
            sum_till_now += n
            
            # This is a special case for zero
            if sum_till_now - k in dic:
                count += dic.get(sum_till_now - k)
            dic[sum_till_now] += 1
            
        return count
