class TrieNode:
    
    def __init__(self):
        
        # This is a very important understanding. That 
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        """
        Initialize your data structure here.
        """
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
        """
        Inserts a word into the trie.
        """
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        return node.isWord
        """
        Returns if the word is in the trie.
        """
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
