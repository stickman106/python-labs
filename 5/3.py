from math import sin
while True:
    try:
        n = int(input("Введите число N:"))
        if n <= 0:
            print("Это не натуральное число")
        else: break    
    except ValueError:
        print("Это не натуральное число")
r=0
j=0
for i in range(1, n+1):
    j = j + sin(i)
    if j==0:
        print("присутствует деление на ноль")
        break
    else:
        r = r + (1/sin(j)) 
print("Результат: ", r)
