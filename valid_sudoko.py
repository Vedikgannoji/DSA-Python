#36 Valid Sudoko
import collections
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def valid_sudoko(board):
    row=collections.defaultdict(set)
    column=collections.defaultdict(set)
    square=collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c]==".":
                continue
            if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[(r//3,c//3)]:
                return False
            row[r].add(board[r][c])
            column[c].add(board[r][c])
            square[(r//3,c//3)].add(board[r][c])
    return True
print(valid_sudoko(board))