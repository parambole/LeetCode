# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        def dfs(node, idx, arr):
            
            # Check exit conition
            if idx >= len(arr) or node == None or node.val != arr[idx]:
                return False
            
            # Then Check LEAF is very very imp and idx - 1
            if node.left == None and node.right == None and idx == len(arr) - 1:
                return True
        
            return dfs(node.left, idx + 1, arr) or dfs(node.right, idx + 1, arr)
            
        
        return dfs(root, 0, arr)
