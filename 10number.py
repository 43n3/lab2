#Дано натуральное число. Определите сумму и количество его цифр.
n=int(input())
summa=0
count=0
while n>0:
    d=n%10
    summa+=d
    count+=1
    n=n//10
print(summa,count)