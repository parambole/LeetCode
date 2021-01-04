class Solution:
    
    
    def getNumMines(self,board, x, y):
        num = 0
        direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i, j in direction:
            r = x + i
            c = y + j
            if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == 'M':
                num += 1
                    
        return num

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
            
        x,y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        else:
            num = self.getNumMines(board, x, y)
            if num:
                board[x][y] = str(num)
            else:
                board[x][y] = 'B'
                for r in range(x-1, x+2):
                    for c in range(y-1, y+2):
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] != 'B':
                            
                            self.updateBoard(board, [r,c])
                
        return board
