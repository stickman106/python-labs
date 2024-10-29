from math import sqrt, cos, sin, tan, log
def f(x):
    if x < 0:
        return 3 * sqrt(x) - (x**4) * cos(2*x)
    elif x==0:
        return sin(2 * x**3 - x) + x**2
    else:
        if (5*log(x)) == 0:
            print("Деление на ноль невозможно")
        else:
            return (tan(x**3 - 3))/(5*log(x))
x = float(input())
print("Результат: ", f(x))
