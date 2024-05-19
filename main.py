# Juego de la Vida Conway

import board
import time, copy

HEIGHT = 10
WIDTH = 10

tablero = board.Board(HEIGHT, WIDTH)
tablero.inicialize_board()
tablero.bring_to_life((3,5))
tablero.bring_to_life((3,6))
tablero.bring_to_life((4,6))
tablero.bring_to_life((4,7))
tablero.bring_to_life((5,5))

# tablero.bring_to_life((6,6))
# tablero.bring_to_life((7,6))
tablero.print_board()
iteracion = 0

while not tablero.is_board_dead():
    tableroReadOnly = copy.deepcopy(tablero)
    print(f"Iteración: {iteracion}")
    for row in range(tablero.height):
        for column in range(tablero.width):
            alive_neighbours  = tableroReadOnly.alive_neighbours((row,column))

            # Una Célula muerta puede revivir si tiene tres vecinas vivas
            if tableroReadOnly.board[row][column] == tablero.dead_char and alive_neighbours == 3:
                tablero.bring_to_life((row,column))

            # Solo si una célula tiene a dos o tres vecinas vivas -> Sobrevive
            if tableroReadOnly.board[row][column] == tablero.alive_char and alive_neighbours != 2 and alive_neighbours != 3:
                tablero.kill((row,column))
    
    
    tablero.print_board()
    iteracion+=1
    time.sleep(0.2)
    print()
    
    

