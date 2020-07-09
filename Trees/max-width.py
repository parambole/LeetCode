# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        if not root:
            return max_width
        queue = deque()
        queue.append((root,0))
        while queue:
            level = len(queue)
            _, curr = queue[0]
            for _ in range(level):
                node, val = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * val))
                if node.right:
                    queue.append((node.right, 2 * val + 1))
            max_width = max(max_width, val - curr + 1)
        return max_width
