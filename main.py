from display import show_board
from status import init_status
from status_handler import get_player_move


def main():
    status = init_status()

    while not status["game_over"]:
        show_board(status["board"])

        x, y = get_player_move()
