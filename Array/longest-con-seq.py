class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        max_count = 0
        for n in nums_set:
            
            # Only check from the begining of the loop
            
            if n - 1 not in nums_set:
                curr_num = n
                
                # Single number is considered to be a streak
                count = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    count += 1
                max_count = max(max_count, count)
                    
        return max_count
