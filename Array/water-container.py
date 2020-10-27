class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height) - 1
        maxarea = 0
        """
        You want to maximize it so it can be done in two ways
        1. You start with max width
        2. Now you try to move only if there is increase in height
        3. Now you minize width but maximize height
        4. Out of all combo get the best one
        """
        while (l < h):
            maxarea = max(maxarea, min(height[l], height[h]) * (h - l))
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1
                
        return maxarea
