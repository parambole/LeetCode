# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    # O(1) memory
    def flatten(self, root: TreeNode):
        
        if not root:
            return None
        
        
        node = root
        
        while node:
            
            if node.left:
                
                rightMost = node.left
                
                
                # REMEBER YOU NEED TO GO ONLY TILL BUT one
                while rightMost.right:
                    rightMost = rightMost.right
                    
                rightMost.right = node.right
                
                # MAKING THE SAME MISTAKE AGAIN
                node.right = node.left
                
                node.left = None
                
            
            # SINCE BY THIS TIME WE HAVE ELIMINATED THE LEFT 
            # V V V IMP TO realize that
            node = node.right
            
        
            
        
        
        
    
    
    # THIS IS WITH O(1) memory 
    
    # Do it without memory
#     def flattenTree(self, node: TreeNode):
#         """
#         Do not return anything, modify root in-place instead.
#         """
        
        
#         if not node:
#             return None
        
#         if not node.left and not node.right:
#             return node
        
#         leftTail = self.flattenTree(node.left)
#         rightTail = self.flattenTree(node.right)
        
        
#         if leftTail:
            
#             leftTail.right = node.right
#             node.right = node.left
#             node.left = None
            
        
#         # This is for special cases
        
#         return rightTail if rightTail else leftTail
    
#     def flatten(self, root: TreeNode):
#         self.flattenTree(root)
    
    
    
        
