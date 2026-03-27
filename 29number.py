'''Дан список из n вещественных чисел, введенных с клавиатуры (среди чисел есть
по крайней мере одно положительное и отрицательное число).
Сформируйте из него 2 списка:
 положительных чисел, используя списковые включения;
 отрицательных чисел, не используя списковые включения.
Выведите на экран:
 исходный список;
 получившиеся списки;
 среднее арифметическое первого списка и среднее геометрическое
второго списка.
При выводе вещественных результатов оставьте два знака после запятой.'''

n = int(input())
nums = list(map(float, input().split()))

positive = [x for x in nums if x > 0]

negative = []
for x in nums:
    if x < 0:
        negative.append(x)

avg_pos = sum(positive) / len(positive)


product = 1
for x in negative:
    product *= x

avg_neg = product ** (1 / len(negative))


print(nums)
print(positive)
print(negative)
print(f"{avg_pos:.2f}")
print(f"{avg_neg:.2f}")