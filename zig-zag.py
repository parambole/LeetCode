# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
                
        temp, result = [], []
        if root == None:return result
        queue = deque()
        queue.append(root)
        queue.append(None)
        left = True
        while len(queue) > 0:
            node = queue.popleft()
            if node == None:
                result.append(temp)
                if len(queue) > 0:
                    temp = []
                    queue.append(None)
                    left = not left
            else:
                if left: temp.append(node.val)
                else: temp.insert(0,node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return result
