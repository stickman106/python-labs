def RecSt(n):
    if n % 2 != 0:
        return 'No'
    else:
        if n == 2:
            return 'Yes'
        elif n < 1:
            return 'No'
        else:
            return RecSt(n / 2)
#main
while True:
    try:
        n = int(input("Введите натуральное число N: "))
        if n <= 0:
            print("N должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не натуральное число")
print(RecSt(n))