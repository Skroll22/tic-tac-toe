def get_player_move():
    while True:
        try:
            x, y = map(int, input("Введите координаты X Y (от 1 до 3) через: ").split())
            if 0 < x < 4 and 0 < y < 4:
                return x, y
            print("Ошибка! Числа должны быть от 1 до 3.")
        except ValueError:
            print("Ошибка! Введите 2 числа через пробел.")
