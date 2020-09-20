class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        
        for n in nums:
            if n - 1 not in num_set:
                
                current_num = n
                
                curr_streak = 1
                
                while current_num + 1 in num_set:
                    curr_streak += 1
                    current_num += 1
                    
                
                longest_streak = max(longest_streak, curr_streak)
                
        return longest_streak
