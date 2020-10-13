class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = -sys.maxsize - 1
        self.getMax(root)
        return self.max
        
    
    def getMax(self, root):
        if root == None:
            return 0
        
        left = max(self.getMax(root.left), 0)
        right = max(self.getMax(root.right), 0)
        
        
        path = root.val + left + right
        
        self.max = max(self.max, path)
        
        return root.val + max(left , right)
