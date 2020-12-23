# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:        
        def helper(node):
            
            # Empty tree has height one
            if not node:
                return (-1, True)
            
            l_depth, l_balance = helper(node.left)
            r_depth, r_balance = helper(node.right)
            
            return (max(l_depth, r_depth) + 1,  (l_balance and r_balance and abs(l_depth - r_depth) <= 1))
        
        return helper(root)[-1]
