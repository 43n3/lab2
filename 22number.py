#Даны n вещественных чисел. Определите максимальное и минимальное из них.
#При выводе вещественных результатов оставьте два знака после запятой.
n=int(input())
nums=[]
for i in range(n):
    nums.append(float(input()))

print(round(max(nums), 2))
print(round(min(nums),2))