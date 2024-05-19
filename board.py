class Board:
    def __init__(self, height:int, width:int, dead_char='-', alive_char='x') -> None:
        self.height = height
        self.width = width
        self.board = list()
        self.dead_char = dead_char
        self.alive_char = alive_char

    def inicialize_board(self)-> None:
        for row in range(self.height):
            newRow = [self.dead_char] * self.width
            self.board.append(newRow)

    def is_board_dead(self)-> bool:
        for row in self.board:
            if self.alive_char in row:
                return False
        return True
        
    def bring_to_life(self, coords:tuple)-> None:
        cell_row,cell_column = coords
        self.board[cell_row][cell_column] = self.alive_char

    def kill(self, coords:tuple)-> None:
        cell_row,cell_column = coords
        self.board[cell_row][cell_column] = self.dead_char

    def is_alive(self, coords:tuple)->bool:
        cell_row, cell_column = coords
        if self.board[cell_row][cell_column]==self.alive_char:
            return True
        return False

    def print_board(self):
        board = ""
        for row in self.board:
            for elemento in row:
                board += (f"{elemento}\t")
            board += "\n"
        print(board)

    def alive_neighbours(self, coords:tuple)-> int:
        cell_row, cell_column = coords
        neighbours_counter = 0
        try:
            if self.is_alive((cell_row-1,cell_column-1)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row,cell_column-1)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row+1,cell_column-1)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row-1,cell_column)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row+1,cell_column)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row-1,cell_column+1)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row,cell_column+1)):
                neighbours_counter+=1
        except:
            pass
        try:
            if self.is_alive((cell_row+1,cell_column+1)):
                neighbours_counter+=1
        except:
            pass
        return neighbours_counter
    
    # Una Célula muerta puede revivir si tiene tres vecinas vivas
    
    # Solo si una célula tiene a dos o tres vecinas vivas -> Sobrevive


                

