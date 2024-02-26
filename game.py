def hello():
    print("Привутствую в игре крестики и нолики")
    print("Формат ввода")
    print("x , y ")
    print("x - номер строки")
    print("y - нормер столбца")

def inputgame():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {game[i][0]}|{game[i][1]}|{game[i][2]}")


def ask():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print("Введите 2 координаты")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if game[x][y] == " ":
                return x, y
            else:
                print("Эта клетка занята, введите новые координаты")
        else:
            print("Координаты вне диапозона")


def proverka():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for cord in win_cords:
        symbol=[]
        for i in cord:
            symbol.append(game[i[0]][i[1]])
        if symbol == ["X", "X", "X"]:
            print("Выйграл X")
            return True
        if symbol == ["O", "O", "O"]:
            print("Выйгал О")
            return True
    return False


hello()
game = [[" ", " ", " "] for i in range(3)]
count = 0
while True:
    count += 1
    inputgame()
    if count % 2 == 1:
        print("Ходят крестики")
    else:
        print("Ходят нолики")
    x, y = ask()
    if count % 2 == 1:
        game[x][y] = "X"
    else:
        game[x][y] = "O"
    if proverka():
        break
    if count == 9:
        print("Ничья")
        break