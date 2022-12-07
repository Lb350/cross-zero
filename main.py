def greet():
    print("~~~~~~~~~~~~~~~~")
    print("  PDEV - 19  ")
    print("А.В. Кравченко  ")
    print("~~~~~~~~~~~~~~~~")
    print("Игра 'Крестики-нолики'" )
    print("X-0 " * 5)
    print("Формат ввода: x, y")
    print("x - номер строки")
    print("y - номер столбца")
    print("~~~~~~~~~~~~~~~~")


def field_output():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  ---------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ---------------- ")
    print()

def ask():
    while True:
        cords = input("     Куда будем ходить?:").split()

        if len(cords) != 2:
            print(" Нужно ввести 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Нужно ввести числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне зоны поля игры!")
            continue

        if field[x][y] != " ":
            print(" Тут занято! Давай еще раз!")
            continue

        return x, y

def check_win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        symbols = []
        for c in comb:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл >>> X <<< крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл >>> 0 <<< нолик!!!")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    field_output()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break
    if count == 9:
        print("Эх...Ничья")
        break
