#Даны целые числа a и b (a может быть больше b). Напечатайте:
# числа от минимального до максимального в строчку (разделяя пробелом);
# числа от максимального до минимального «столбиком».
a=int(input())
b=int(input())
start=min(a,b)
end=max(a,b)
for i in range(start, end+1):
    print(i, end=" ")
print()
x=end
while x>=start:
    print(x)
    x-=1