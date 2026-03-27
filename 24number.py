#Дано n вещественных чисел. Определите, является ли последовательность
#упорядоченной по возрастанию. В случае отрицательного ответа выведите
#порядковый номер числа, нарушающего такую упорядоченность.
nums = []
for x in input().split():
    nums.append(float(x))

index = -1

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        index = i + 1
        break

if index == -1:
    print("YES")
else:
    print(index)