# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DRY RUN is very important in such questions
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxV = 0
        
        # Learn how to go top to bottom and bottom to top
        
        # This can be done when you dont know what value you need to pass to the root
        self.traverse(root, root.val, root.val)
        
        return self.maxV 
        
    def traverse(self, root, curr_max, curr_min):
        if root == None:
            return
        
        self.maxV = max(self.maxV, abs(root.val - curr_max), abs(root.val - curr_min))
        
        # POST_ORDER
        
        curr_max = max(root.val, curr_max)
        curr_min = min(root.val, curr_min)
        
        self.traverse(root.left, curr_max, curr_min)
        self.traverse(root.right, curr_max, curr_min)        
