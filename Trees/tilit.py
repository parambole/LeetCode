# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.finalValue = 0
        self.traverse(root)
        return self.finalValue
    
    def traverse(self, root):
        
        if root == None:
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        value = abs(left - right)
        
        self.finalValue += value
        
        return left + right + root.val
