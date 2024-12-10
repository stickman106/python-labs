def Quarter(x, y):
    while True:
        try:
            x = float(input("Введите число x не равное 0: "))
            if x == 0:
                print("x должно быть не рано 0, введите снова")
            else:
                break
        except ValueError:
            print("Это не число")
    while True:
        try:
            y = float(input("Введите число y не равное 0: "))
            if y == 0:
                print("y должно быть не рано 0, введите снова")
            else:
                break
        except ValueError:
            print("Это не число")
    if x > 0 and y > 0:
        ans = 1
    elif x < 0 and y > 0:
        ans = 2 
    elif x < 0 and y < 0:
        ans = 3
    elif x > 0 and y < 0:
        ans = 4
    return ans
#main
x = y = 0
for i in range(3):
    print('Точка находится в', Quarter(x, y), 'четверти')