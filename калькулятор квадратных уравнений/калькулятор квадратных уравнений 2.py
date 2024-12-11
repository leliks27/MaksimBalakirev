from math import *
print('Калькулятор для вычисления квадратных уравнений')
print('Впишите коэффиценты для решения уравнения')
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

d = (b**2) - (4 * a * c)

if d > 0:
    x1 = (-b + math.sqrt(d)) // (2 * a)
    x2 = (-b - math.sqrt(d)) // (2 * a)
    print(x1,x2)
elif d == 0:
    x = -b / (2*a)
    print(x)
else:
    print('Нет корней')