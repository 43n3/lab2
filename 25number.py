#Выведите на экран таблицу умножения на n (2<n≤9)
n=int(input())
for i in range(1,n+1):
    row=[]
    for j in range(1,n+1):
         row.append(str(i) + " x " + str(j) + " = " + str(i*j))
    print("    ".join(row))