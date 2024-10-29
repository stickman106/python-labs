while True:
    try:
        n = int(input("Введите целое число N>0:"))
        if n <= 0:
            print("N должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
k=1
while k**2<=n:
    k+=1
print('Результат: ', k)
    
