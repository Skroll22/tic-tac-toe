def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)