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
        def rSerialize(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rSerialize(root.left, string)
                string = rSerialize(root.right, string)
            return string
        return rSerialize(root, '')
                
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rDeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rDeserialize(l)
            root.right = rDeserialize(l)
            return root
        
        data = data.split(',')
        return rDeserialize(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
