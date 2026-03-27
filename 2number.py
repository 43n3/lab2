#Определите максимальное и минимальное значения из двух различных целых чисел.
a=int(input())
b=int(input())
if a>b:
    max=a
    min=b
else:
    max=b
    min=a
print("Максимум:", + max)
print("Минимум:", + min)