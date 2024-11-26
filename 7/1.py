from random import randint

while True:
    try:
        m = int(input("Введите целое число M > 0:"))
        if m <= 0:
            print("M должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
while True:
    try:
        n = int(input("Введите целое число N > 0:"))
        if n <= 0:
            print("N должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
sp = [[randint(1, 20) for j in range(n)] for i in range(m)]
print(sp)
stolb = 1
els = []
while stolb <= n-1:
    for i in sp:
        els.append(i[stolb])
    for i in range(len(sp)):
        sp[i][stolb] = els[(i*(-1)-1)]
    els=[]
    stolb += 2
print(sp)