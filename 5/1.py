while True:
    while True:
        try:
            a = int(input("Введите число a:"))
            break
        except ValueError:
            print("Это не целое число")
    while True:
        try:
            b = int(input("Введите число b:"))
            break
        except ValueError:
            print("Это не целое число")
    if a < b:
        break
    else:
        print("a должно быть меньше b, введите снова")
s=[]
n=0
for i in range(a, b+1):
    s.append(i)
    n+=1
s=s[:len(s)-2]
print("Строка: ", *s)
print("Число элемнтов: ", n)
