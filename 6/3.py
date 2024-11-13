from random import randint
while True:
    try:
        n = int(input("Введите целое число N > 0: "))
        if n <= 0:
            print("N должно быть > 0, введите снова")
        else: 
            break
    except ValueError:
        print("Это не целое число")
while True:
    try:
        c = float(input("Введите число C: "))
        break
    except ValueError:
        print("Это не число")
lnumb = [randint(-100, 100) for i in range(n)]
count=0
prois=1
maxn=0
numi=0
for i in range(len(lnumb)):
    if lnumb[i] > c: 
        count+=1
for i in range(len(lnumb)):
    if abs(lnumb[i]) > maxn: # > если нужен первый max, >= если нужен последний max
        
        numi = i
        maxn = abs(lnumb[i])
for i in range(numi+1, len(lnumb)):
    prois = prois * lnumb[i]
print('Список: ', lnumb)
print('Кол-во элементов > N: ', count)
print('Произведение чисел после максимального по модулю элемента: ', prois)


    
