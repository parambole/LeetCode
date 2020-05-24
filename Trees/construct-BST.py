# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    
        def buildTree(node, val):
                
                
            # in treee construction do it in base condition only
            
            
            if val < node.val:
                if node.left != None:
                    buildTree(node.left, val)
                else:
                    node.left = TreeNode(val)
                    
            
            elif val > node.val:
                if node.right != None:
                    buildTree(node.right, val)
                else:
                    node.right = TreeNode(val)
                
                
            
        if len(preorder) == 0:
            return root
        root = TreeNode()

        root.val = preorder[0]

        for i in range(1, len(preorder)):
            buildTree(root, preorder[i])
        
        return root
    
