# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

            res.append(str(node.val) if node else '*')
        return ",".join(res) 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tree_data = data.split(",")

        queue = collections.deque()
        root = TreeNode(int(tree_data[0]))
        queue.append(root)
        i = 1
        
        while queue and i < len(tree_data):
            node = queue.popleft()
            
            if tree_data[i] != '*':
                node.left = TreeNode(int(tree_data[i]))
                queue.append(node.left)
            i += 1
            
            if tree_data[i] != '*':
                node.right = TreeNode(int(tree_data[i]))
                queue.append(node.right)
            i += 1
        return root
            
        
        
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
