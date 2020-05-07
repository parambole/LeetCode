# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dic = {}
        def dfs(node, parent, level, x, y):
            nonlocal dic
            if node == None:
                return
        
            if node.val == x or node.val == y:
                dic[node.val] = (parent, level) 
                
            if node.left != None:
                dfs(node.left, node, level + 1, x, y)
                
            if node.right != None:
                dfs(node.right, node, level + 1, x, y)
        
        
        # Remeber the call needs to always always come back to the main caller. If you are doing some checks after that
        
         # Also when you have multiple things to pack and unpack better to store it somewhere. 
        
        dfs(root, None, 0, x, y)
        
        if x in dic and y in dic:
            return dic[x][0] != dic[y][0] and dic[x][1]  == dic[y][1]
        else:
            return False
            
