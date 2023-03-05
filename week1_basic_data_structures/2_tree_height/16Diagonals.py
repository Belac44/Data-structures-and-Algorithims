# import math 

# board = [[0]*5 for _ in range(5)]

# def diagonalise(row,col,board):
#     if row % 5 == 4 and col % 5 == 4:
#         if find_sum(board) >= 16:
#             print(board)
#             exit()
#         return
#     if  find_sum(board) >= 16:
#            print(board)
#            exit()


#     i = col // 5
#     j = col % 5
#     if can_diagonalise(i, j, 1, board):
#         board[i][j] = 1
#         diagonalise(i, j+1, board)
#         board[i][j] = 0

#     if can_diagonalise(i, j, 2, board):
#         board[i][j] = 2
#         diagonalise(i, j+1, board)
#         board[i][j] = 0

#     diagonalise(i, j, board)


# def can_diagonalise(row,col, value, board):
#     if row == 0 and col == 0:
#         return True
#     if row == 0:
#         #check before
#         if board[row][col-1] + value == 3:
#             return False
#         return True
#     if col == 0:
#         #check above
#         if board[row-1][col] + value == 3:
#             return False
#         #check cell above right
#         if board[row-1][col+1] + value == 2:
#             return False
#         return True
#     if col == len(board) - 1:
#         #check above
#         if board[row-1][col] + value == 3:
#             return False
#         #check previous:
#         if board[row][col-1] + value == 3:
#             return False
#         #check above left
#         if board[row-1][col-1] + value == 4:
#             return False        
#     else:
#          #check above
#         if board[row-1][col] + value == 3:
#             return False
#         #check previous:
#         if board[row][col-1] + value == 3:
#             return False
#         #check above left
#         if board[row-1][col-1] + value == 4:
#             return False
#         #check above right
#         if board[row-1][col+1] + value == 2:
#             return False
#         return True


# def find_sum(board):
#     summation = 0
#     for i in range(5):
#         for j in range(5):
#             summation += math.ceil(board[i][j]/2)
#     return summation


# diagonalise(0, 0, board)

size = 5
board = [['.'] * size for i in range(size)]

def canPlace(p, i, j, board):
    if p == 0:
        if (j>0 and board[i][j-1] == 1 ) or (i>0 and board[i-1][j] == 1) or (i>0 and j>0 and board[i-1][j-1] == 0):
            return False
    if p == 1:
        if (j>0 and board[i][j-1] == 0) or (i>0 and board[i-1][j] == 0) or (i>0 and j+1<size and board[i-1][j+1] == 1):
            return False
    return True



def dfs(x, count):
    if (size*size - x + 1) + count < 16:
        return
    if x == size*size:
        if count == 16:
            print(board)
        return

    i = x // size
    j = x % size
    if canPlace(0, i, j, board):
        board[i][j] = 0
        dfs(x+1, count+1)
        board[i][j] = '.'
    if canPlace(1, i, j, board):
        board[i][j] = 1
        dfs(x+1, count+1)
        board[i][j] = '.'
    dfs(x+1, count)

dfs(0,0)