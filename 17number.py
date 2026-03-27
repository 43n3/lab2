#Решите задачу № 2.7, организовав бесконечный цикл, который бы прерывался при
#выполнении условия, используя оператор break.
summa=0
while True:
    x=int(input())
    if x==0:
        break
    summa+=x
print(summa)