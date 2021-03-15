class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(List[0], index, 0) for index, List in enumerate(nums)]
        
        heapq.heapify(heap)
        
        max_val = max([List[0] for List in nums])
        
        smallest_range = -sys.maxsize - 1, sys.maxsize
        
        while heap:
            min_val, list_index, num_index = heapq.heappop(heap)
            
            if max_val - min_val < smallest_range[1] - smallest_range[0]:
                smallest_range = min_val, max_val
                
            if num_index + 1 == len(nums[list_index]):
                return smallest_range
            
            max_val = max(nums[list_index][num_index + 1], max_val)
            
            heapq.heappush(heap, (nums[list_index][num_index + 1], list_index, num_index + 1))
