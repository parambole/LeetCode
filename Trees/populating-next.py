"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            temp = None
            while size > 0:
                node = queue.popleft()
                node.next = None
                if temp:
                    temp.next = node
                temp = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                size -= 1
                
        return root
