"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        stack = []
        mover = head
        
        while mover:
            if mover.child:
                if mover.next:
                    stack.append(mover.next)
                mover.next = mover.child
                mover.child.prev = mover
                mover.child = None
            if mover.next == None:
                if len(stack) > 0:
                    node = stack.pop()
                    mover.next = node
                    node.prev = mover
            mover = mover.next
        
        return head
