def hello():
    print('  Добро пожаловать  ')
    print('       в игру       ')
    print('!!!крестики нолики!!!')
    print('')
    print('Координаты для ввода: "x" "y", где:')
    print('"x" - номер строки')
    print('"y" - номер столбца')


def game_field():
    print('    0   1   2')
    for i in range(3):
        print('  -------------')
        print(f'{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')
    print('  -------------')


def ask():
    while True:
        coordinates = input('Ваш ход: ').split()

        if len(coordinates) != 2:
            print('Введите две координаты!')
            continue

        x, y = coordinates

        if not x.isdigit() or not y.isdigit():
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введите координаты в диапазоне от 0 до 2!')
            continue

        if field[x][y] != ' ':
            print('Поле занято!')
            continue

        return x, y


def win():
    win_coordinates = (((0, 0), (0, 1), (0, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 0), (1, 1), (2, 2)),
                       ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coordinates:
        a = cord[0]
        b = cord[1]
        c = cord[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
            print(f'Выиграл {field[a[0]][a[1]]}!')
            return True
    return False


hello()
field = [[' ', ' ', ' '] for i in range(3)]
n = 0
while True:

    n += 1

    game_field()

    if n % 2 != 0:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = ask()

    if n % 2 != 0:
        field[x][y] = 'Х'
    else:
        field[x][y] = 'О'

    if n == 9:
        print("Ничья!")
        break

    if win():
        break
