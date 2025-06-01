from display import show_board
from game_logic import make_move, check_win, is_draw
from status import init_status
from status_handler import get_player_move


def main():
    status = init_status()

    while not status["game_over"]:
        show_board(status["board"])
        x, y = get_player_move()

        if make_move(status, x, y):
            if check_win(status["board"]):
                show_board(status["board"])
                print(f'Игрок {status["current_player"]} победил!')
                status["game_over"] = True
            elif is_draw(status["board"]):
                show_board(status["board"])
                print("Ничья!")
                status["game_over"] = True
            status["current_player"] = "X" if  status["current_player"] == "O" else "O"

if __name__ == "__main__":
    main()