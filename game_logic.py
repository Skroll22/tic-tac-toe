def make_move(status, x, y):
    # Проверка возможности хода
    if status["board"][x-1][y-1] != " ":
        print("Клетка занята!")
        return False # Ячейка занята
    status["board"][x-1][y-1] = status["current_player"]
    return True # Ход выполнен успешно

def check_win(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Проверка столбцов
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Проверка главной диагонали
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Проверка побочной диагонали
    if board[2][0] == board[1][1] == board[0][2] != " ":
        return True

    return False  # Игра продолжается

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

