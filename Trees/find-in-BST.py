# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(root, val):
            if root == None:
                return None
            if root.val == val:
                return root
            elif val < root.val:
                return search(root.left, val)
            else:
                return search(root.right, val)
        return search(root, val)
