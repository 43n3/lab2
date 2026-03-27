#Дано число n. Из чисел 0,5,10,15,20,25,... напечатать те, которые не превышают n.
n=int(input())
x=0
count=[0]
while n>=x:
    count.append(x)
    x+=5
print(*count)