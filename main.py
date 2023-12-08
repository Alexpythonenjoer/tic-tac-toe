print('Приветствуем вас в игре крестики нолики!')
print('Форма ввода: x y')
print('x-номер строки')
print('y-номер столбца')

field=[[" "]*3 for i in range(3)]

#ВЫЗОВ ПОЛЯ
def fiel_forma():
    print("  0 1 2")
    for i in range(3):
        info=" ".join(field[i])
        print(f'{i} {info}')

fiel_forma()

#ПРОВЕРКА ВВЕДЕННЫХ ПОЛЬЗОВАТЕЛЕМ ДАННЫХ
def ask():
    while True:
        coords=map(int,input('        Ваш ход:').split())
        x, y = coords
        if 0>x or x>2 or 0>y or y>2:
            print('Координаты вне диапазона!')
            continue
        # x, y = coords
        if field[x][y]!=" ":
            print('Клетка занята!')
            continue
        return x,y

x,y=ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symb = []
        for i in cord:
            symb.append(field[i[0]][i[1]])
        if symb == ["x", "x", "x"]:
            print("Выиграл x")
            return True
        if symb == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

num=0
while True:
    num+=1
    fiel_forma()
    if num%2==1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x,y=ask()

    if num%2==1:
        field[x][y]='x'
    else:
        field[x][y]='0'

    if check_win():
        break

    if num==9:
        print('Ничья!')
        break






