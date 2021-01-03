# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        queueO, queueC = collections.deque(), collections.deque()   
        queueO.append(original)
        queueC.append(cloned)
        while queueO:
            size = len(queueO)
            for i in range(size):
                nodeO = queueO.popleft()
                nodeC = queueC.popleft()

                if nodeO == target:
                    return nodeC

                if nodeO.left is not None:
                    queueO.append(nodeO.left)
                    queueC.append(nodeC.left)

                if nodeO.right is not None:
                    queueO.append(nodeO.right)
                    queueC.append(nodeC.right)
                        
        return None
                    
            
            
            
            
