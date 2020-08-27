class Solution:
    def binarySearch(self, space, key):
        low = 0
        high = len(space)
        while low < high:
            mid = (low + high) // 2
            if space[mid][0] == key:
                return space[mid][1]
            elif space[mid][0] < key:
                low = mid + 1
            else:
                high = mid
        return space[low][1] if (low >= 0 and low < len(space)) else -1
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        space = []
        result = []
        for i, e in enumerate(intervals):
            space.append((e[0], i))
            
        space = sorted(space)
        
        for interval in intervals:
            result.append(self.binarySearch(space, interval[1]))
            
        return result
