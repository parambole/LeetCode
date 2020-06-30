class TrieNode:
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for w in word:
            
            # This create a new if it does not exist
            
            node = node.children[w]
        node.isWord = True
        
    def search(self, word):
        
        node = self.root
        
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
        
        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        
        def dfs(board, i, j, n, m, node, word, res):
            
            
            # This is for single character words
            
            if node.isWord:
                res.append(word)
                node.isWord = False  
            
            
            if i < 0 or j < 0 or i >= n or j >= m:
                return       
            
            # [["a","a"]] ["aaa"] ONE IMP THING THAT YOU FORGOT
            
            temp = board[i][j]
            
            node = node.children.get(temp)
            
            if not node:
                return
            
            board[i][j] = '#'
            
            
            
            dfs(board, i + 1, j, n, m, node, word+temp, res)
            dfs(board, i , j + 1, n, m, node, word+temp, res)
            dfs(board, i - 1, j, n, m, node, word+temp, res)
            dfs(board, i , j - 1, n, m, node, word+temp, res)
            
            board[i][j] = temp
            
        res = []
        trie = Trie()
        
        # This is to traverse the Trie
        node = trie.root
        
        for w in words:
            trie.insert(w)
        
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                dfs(board, i , j, n ,m, node, "", res)
                
        return res
