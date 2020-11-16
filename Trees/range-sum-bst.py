# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0
        if not root:
            return self.sum
        self.low = low
        self.high = high
        self.dfs(root)
        return self.sum
        
    def dfs(self, root):
        
        if root.val >= self.low and root.val <= self.high:
            self.sum += root.val
        
        if root.val > self.low and root.left != None:
            self.dfs(root.left)
            
        if root.val < self.high and root.right != None:
            self.dfs(root.right)
