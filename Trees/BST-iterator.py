# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._left_inorder(root)
        
        
    def _left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        

    def next(self) -> int:
        topmost = self.stack.pop()
        
        if topmost.right:
            self._left_inorder(topmost.right)
            
        return topmost.val
        

    def hasNext(self) -> bool:
        
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
