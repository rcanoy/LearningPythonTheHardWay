import numpy as np
import matplotlib.pyplot as plt
from random import randint
from assess import *

class GameOfLife(object):
    """_summary_
            This class initiates the structure of the game of life.
            Board Size: (100, 100)

    _args_:
        object (_type_): _description_
    """
    
    def __init__(self):
        """_summary_
        
        _output_:
            self.shape_list = ['square', diamond]
        """
        self.shape_list = ['square', 'diamond']        

    def board_init(self, shape_init, dim=(100,100)):
        """_summary_

        _args_:
            shape_init (_type_): _description_
            dim (tuple, optional): _description_. Defaults to (100,100).

        _returns_:
            _board_: initial set up is either a square or a diamond
        """
        
        board = np.zeros(dim)
        if shape_init.lower() == 'square':
            board[[40], [i for i in range(40, 61)]] = 1
            board[[i for i in range(40, 61)], [40]] = 1
            board[[60], [i for i in range(40, 61)]] = 1
            board[[i for i in range(40, 61)], [60]] = 1
        elif shape_init.lower() == 'diamond':
            board[[i for i in range(50, 40-1, -1)], [i for i in range(40, 50+1, 1)]] = 1
            board[[i for i in range(40, 50+1, 1)], [i for i in range(50, 60+1, 1)]] = 1
            board[[i for i in range(50, 60+1, 1)], [i for i in range(40, 50+1, 1)]] = 1
            board[[i for i in range(60, 50-1, -1)], [i for i in range(50, 60+1, 1)]] = 1
        else:
            pass
        
        return board

# Initialisation
a = GameOfLife()
board = a.board_init(a.shape_list[1])
plt.imshow(board, cmap = 'gray')
plt.show()

rows = [row for row in range(2, board.shape[0]-1)]
cols = [col for col in range(2, board.shape[1]-1)]

while True:
    board_temp = board
    for row in rows:
        for col in cols:
            board_temp = assess(board, row, col)
    board = board_temp
    plt.imshow(board, cmap="gray")
    plt.show()
    plt.close()