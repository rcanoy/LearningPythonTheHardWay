import numpy as np
import matplotlib.pyplot as plt


def assess(board, row, col, dim=(3,3)):
    rows = [row_ind for row_ind in range(row-1, (row+1)+1)]
    cols = [col_ind for col_ind in range(col-1, (col+1)+1)]
    
    live_count = 0
    for row_ind in rows:
        for col_ind in cols:
            if row_ind == row and col_ind == col:
                pass
            elif board[row_ind, col_ind] == 1:
                live_count += 1
            else:
                pass
    
    if live_count >= 2:
        board[row, col] = 1
        return board
    elif live_count == 0 or live_count < 2:
        board[row, col] = 0
        return board
    else:
        pass