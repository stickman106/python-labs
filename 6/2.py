while True:
    try:
        n1 = int(input("Введите целое число N1 > 0:"))
        if n1 <= 0:
            print("N1 должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
while True:
    try:
        n2 = int(input("Введите целое число N2 > 0:"))
        if n2 <= 0:
            print("N2 должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
while True:
    s1 = input("Введите строку S1 >= N1: ")
    if len(s1) < n1:
        print("Строка S1 должна быть >= N1")
    else:
        break
while True:
    s2 = input("Введите строку S2 >= N2: ")
    if len(s2) < n2:
        print("Строка S2 должна быть >= N2")
    else:
        break

s3 = ''
for i in range(n1):
    s3 = s3 + s1[i]
for i in range(n2, 0, -1):
    i1 = -abs(i)
    s3 = s3 + s2[i1]
print('s1: ', s1)
print('s2: ', s2)
print('Новая строка: ', s3)

    
