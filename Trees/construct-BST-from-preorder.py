# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            self.build(root,preorder[i])
        return root
            
    def build(self, root, val):
        
        if root.val > val:
            if root.left != None:
                self.build(root.left, val)
            else:
                root.left = TreeNode(val)
                return
        elif root.val < val:
            if root.right != None:
                self.build(root.right, val)
            else:
                root.right = TreeNode(val)
                return
