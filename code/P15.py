def is_valid(board, row, col, num):
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        if board[block_row + i // 3][block_col + i % 3] == num:
            return False
    return True


def is_valid_sudoku(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != "?":
                board[row][col] = "?"
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num
    return True


def find_missing_number(board):
    if not is_valid_sudoku(board):
        return -1

    question_mark_row = question_mark_col = -1
    for row in range(9):
        for col in range(9):
            if board[row][col] == "?":
                question_mark_row, question_mark_col = row, col
                break
        if question_mark_row != -1:
            break

    for num in "123456789":
        if is_valid(board, question_mark_row, question_mark_col, num):
            return num
    return -1


board = []
for _ in range(9):
    board.append(input().strip().split(","))
print(find_missing_number(board))
