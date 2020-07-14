# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queueA = deque()
        queueB = deque()
        
        queueA.append(p)
        queueB.append(q)
        while queueA:
            A = queueA.pop()
            B = queueB.pop()
            
            if A == None and B == None:
                continue
            
            if not self.check(A,B):
                return False
            
            queueA.append(A.left)
            queueB.append(B.left)
            
            queueA.append(A.right)
            queueB.append(B.right)
        return True

            
    def check(self,A, B):
        
        if A == None and B == None:
            return True
                
        if not A or not B:
            return False

        return A.val == B.val
                
            
