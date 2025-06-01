def init_status():
    return {
        "board": [[" " for _ in range(3)] for _ in range(3)],
        "current_player": "X",
        "game_over": False,
        "winner": None
    }