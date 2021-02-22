# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        queue = collections.deque()
        queue.append((root, 0, 0))
        
        dic = collections.defaultdict(list)
        minCol = sys.maxsize
        maxCol = -sys.maxsize - 1
        
        while queue:
            for _ in range(len(queue)):
                node, row, col = queue.popleft()
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                dic[col].append((row, node.val))
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1 ))
                    
        res = []
        
        for i in range(minCol, maxCol + 1):
            res.append([val for _, val in sorted(dic[i])])
            
        return res
                
            
        
