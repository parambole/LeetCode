# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxValue = -sys.maxsize - 1
        if root == None:
            return maxValue
        stack = collections.deque()
        stack.append(root)
        
        
        
        while len(stack) != 0:
            node = stack.pop()
            maxValue = max(self.getMaxGain(node), maxValue)
            
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
            
        return maxValue
    
    
    def getMaxGain(self, root: TreeNode):
        
        if root == None:
            return 0
        
        left = self.getMaxGain(root.left)
        right = self.getMaxGain(root.right)
        
        
        v1 = root.val
        # v2 = root.val + left
        # v3 = root.val + right
        v4 = root.val + max(left, right)
        
        
        #print(max(v1,v2,v3,v4))
        
        print(max(v1,v4))
        
        
        return max(v1,v4)
        
        
        # if (left + right) > 0:
        #     return root.val + left + right if (root.val + left + right) > root.val else root.val
        # else:
        #     return root.val + max(left, right) if root.val + max(left, right) else root.val
        
