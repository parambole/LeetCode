# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = collections.deque([])
        self.inorder(root)
        
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.queue.append(node.val)
        self.inorder(node.right)
        

    def next(self) -> int:
        return self.queue.popleft()
        

    def hasNext(self) -> bool:
        return True if len(self.queue) > 0 else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
