class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i , j, r, c):
            
            if i >= r or i < 0 or j >= c or j < 0 or board[i][j] != 'O':
                return
            
            board[i][j] = 'D'
            dfs(board, i+1, j, r, c)
            dfs(board, i, j + 1, r, c)
            dfs(board, i - 1, j, r, c)
            dfs(board, i, j - 1, r, c)
                
        if not board:
            return

        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                if (i in [0, r - 1] or j in [0, c - 1] ) and board[i][j] == 'O':
                    dfs(board, i , j, r , c)
                            
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'
        
