# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxValue = 0
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            d = left + right
            self.maxValue = max(d, self.maxValue)
            return 1 + max(left, right)
        
        depth(root)
        return self.maxValue
        
