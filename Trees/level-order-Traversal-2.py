# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = collections.deque()
        result = []
        temp = []
        queue.append(root)
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node == None:
                if len(queue) > 0:
                    queue.append(node)
                result.insert(0, temp)
                temp = []
            else:
                temp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return result
            
