class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        if not board:
            return
        
        def dfs(i, j, board):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            
            board[i][j] = '.'
            dfs(i+1, j, board)
            dfs(i-1, j, board)
            dfs(i, j+1, board)
            dfs(i, j-1, board)
        
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                dfs(i,j,board)  
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                dfs(i,j,board)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        return board
