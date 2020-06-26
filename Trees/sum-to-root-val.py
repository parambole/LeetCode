# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack = []
        curr = ""
        total = 0
        stack.append((root, curr))
        
        while stack:
            node, curr = stack.pop()
            curr += str(node.val)
            if node.left == None and node.right == None:
                total += int(curr)
            if node.right != None:
                stack.append((node.right, curr))
            if node.left != None:
                stack.append((node.left, curr))
        return total
