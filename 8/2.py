def IsPowerN(K, N):
    i = 0
    ans = False
    sn = N
    while N <= K:
        if K==N:
            ans = True
            break
        else:
            i+=1
            N = sn ** i
    return(ans)
def AddK(n):
    l=[]
    for i in range(n):
        while True:
            try:
                k = int(input("Введите число K > 0: "))
                if k <= 0:
                    print("K должно быть > 0, введите снова")
                else: 
                    l.append(k)
                    break
            except ValueError:
                print("Это не число")
    return l
#main
c=0
while True:
    try:
        n = int(input("Введите число N > 1: "))
        if n <= 1:
            print("N должно быть > 1, введите снова")
        else: 
            break
    except ValueError:
        print("Это не число")

for k in AddK(10):
    if IsPowerN(k, n) == True:
        c+=1
print(c)