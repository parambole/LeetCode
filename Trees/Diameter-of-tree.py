class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxval = 0
        return self.dfs(root)
    
    def dfs(self, node):
        if node == None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.maxval = max(self.maxval, left + right)

        return 1 + max(left, right)
