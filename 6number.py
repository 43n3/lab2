#Даны вещественные числа a, b, c (a≠0).
#Решите уравнение ax2+bx+c=0. При выводе значений оставьте 1 знак после запятой.
from math import *
a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))
d=b**2-4*a*c
if d>0:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print(round(x1,1), round(x2,1))
elif d==0:
    x=-b/(2*a)
    print(round(x, 1))
else:
    print("Корней нет")