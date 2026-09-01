from chessGame.pieces.ChessPiece import ChessPiece

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.move = 1
        self._cell = (1, 5)
        self._list_move = []    
        
    def get_move(self):
        return self.move
    
    def compute_fisible_set(self, grid):
        self._list_move = []

        if(grid[self._cell[0] + self.move][self._cell[1] + self.move] == None):
            self._list_move.append([self._cell[0] + self.move, self._cell[1] + self.move])
        
        if(grid[self._cell[0] - self.move][self._cell[1] + self.move] == None):
            self._list_move.append([self._cell[0] - self.move, self._cell[1] + self.move])
        
        if(grid[self._cell[0] + self.move][self._cell[1] - self.move] == None):
            self._list_move.append([self._cell[0] + self.move, self._cell[1] - self.move])
        
        if(grid[self._cell[0] - self.move][self._cell[1] - self.move] == None):
            self._list_move.append([self._cell[0] - self.move, self._cell[1] - self.move])
        
        if(grid[self._cell[0] + self.move][self._cell[1]] == None):
            self._list_move.append([self._cell[0] + self.move, self._cell[1]])
        
        if(grid[self._cell[0] - self.move][self._cell[1]] == None):
            self._list_move.append([self._cell[0] - self.move, self._cell[1]])
        
        if(grid[self._cell[0]][self._cell[1] + self.move] == None):
            self._list_move.append([self._cell[0], self._cell[1] + self.move])
        
        if(grid[self._cell[0]][self._cell[1] - self.move] == None):
            self._list_move.append([self._cell[0], self._cell[1] - self.move])
        
        print(sorted(self._list_move))
        return None
    
    def get_fisible_set(self):
        return self._list_move