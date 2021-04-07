class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = collections.deque([])
        max_q = collections.deque([])
        
        
        right = 0
        left = 0
        
        max_length = 0
        
        n = len(nums)
        
        while right < n:
            num = nums[right]
            while min_q and num < min_q[-1]:
                min_q.pop()
            min_q.append(num)
            
            min_val = min_q[0]
            
            while max_q and num > max_q[-1]:
                max_q.pop()
            max_q.append(num)
            
            max_val = max_q[0]
            
            while abs(min_q[0] - max_q[0]) > limit:
                curr_num = nums[left]
                
                if min_q[0] == curr_num:
                    min_q.popleft()
                    
                if max_q[0] == curr_num:
                    max_q.popleft()                    
                
                left += 1
                
            max_length = max(max_length, right - left + 1 )
            right += 1
            
        return max_length
