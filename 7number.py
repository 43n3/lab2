#Дана непустая последовательность целых чисел, оканчивающаяся нулем. Найти
#сумму и количество введенных чисел.
ab=int(input())
count=0
summa=0
while ab!=0:
    count+=1
    summa+=ab
    ab=int(input())
print(summa, count)