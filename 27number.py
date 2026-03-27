#Выведите на экран (в строку) n первых простых чисел.

n = int(input())
num = 2
while n > 0:
    simple = True
    for i in range(2, num):
        if num % i == 0:
            simple = False
    if simple:
        print(num, end=" ")
        n -= 1
    num += 1