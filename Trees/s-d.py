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
        def rserialize(string,node):
            if node == None:
                string += '#,'
                return string
            string += str(node.val) + ","
            string = rserialize(string, node.left)
            string = rserialize(string, node.right)
            return string
        return rserialize('', root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(items):
            if items[0] == '#':
                items.pop(0)
                return None
            root = TreeNode(items[0])
            items.pop(0)
            root.left = rdeserialize(items)
            root.right = rdeserialize(items)
            return root
        return rdeserialize(data.split(','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
