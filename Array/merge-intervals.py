class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = results[-1]
            if intervals[i][0] <= curr[1]:
                curr[1] = max(intervals[i][1], curr[1])
                
            else:
                results.append(intervals[i])
                
        return results
