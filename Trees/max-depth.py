# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxValue = 1
        self.dfs(root, 1)
        return self.maxValue

    def dfs(self, node, currVal):
        if not node:
            return
        self.maxValue = max(self.maxValue, currVal)
        self.dfs(node.left, currVal + 1)
        self.dfs(node.right, currVal + 1)
