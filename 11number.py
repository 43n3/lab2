#Вывести в строку 10 первых натуральных чисел, оканчивающихся на цифру k,
#кратных числу s и находящихся в интервале, левая граница которого равна start.
start=int(input())
k=int(input())
s=int(input())
count=0
x=start
while count<10:
    if x%10==k and x%s==0:
        print(x, end=" ")
        count+=1
    x+=1
