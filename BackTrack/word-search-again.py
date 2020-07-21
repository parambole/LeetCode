class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        
        for i in range(r):
            for j in range(c):
                if self.dfs(i,j,r,c,board,word,0,""):
                    return True
        return False
                
    def dfs(self,i,j,r,c,board,word,idx,res):
        if res == word:
            return True
        
        if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != word[idx]:
            return
        temp = board[i][j]
        board[i][j] = "#"
        status =  (self.dfs(i + 1,j, r,c,board,word,idx+1,res+word[idx])
        or self.dfs(i,j + 1, r,c,board,word,idx+1,res+word[idx])
        or self.dfs(i - 1,j, r,c,board,word,idx+1,res+word[idx])
        or self.dfs(i,j - 1, r,c,board,word,idx+1,res+word[idx]))
        if status:
            return True
        else:
            board[i][j] = temp
