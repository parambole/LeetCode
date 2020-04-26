# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        # This is one of the most difficult questions that I have solved that involves so much of thinking see how you can develope this kind of thinking
        
        def maxGain(node):
            
            nonlocal maxValue
            
            if node == None:
                return 0
            
            # Over here it's like Kandane Algorithm where you decide where to pick a node or not
            maxLeft = max(maxGain(node.left), 0)
            
            # Over here it's like Kandane Algorithm where you decide where to pick a node or not
            maxRight = max(maxGain(node.right), 0)
            
            # Now here you decide by adding whether you have picked up the nodes when standing at a particular node l - N - R
            
            # This is the beauty you are doing this for each node to know which is better
            newRoute = node.val + maxLeft + maxRight
            
            maxValue = max(maxValue, newRoute)
            
            # Now here each node will always return only one of its childern as its a path
            return node.val + max(maxLeft, maxRight)
        
        maxValue = float('-inf')
        maxGain(root)
        return maxValue
            
            
