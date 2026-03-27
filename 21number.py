#Известно количество учеников в классе и их рост (см.); рост мальчиков условно
#задан отрицательными числами. Определите средний рост мальчиков и средний
#рост девочек.
#При выводе вещественных результатов оставьте один знак после запятой.
n=int(input())
sum_boys=0
count_boys = 0
sum_girls = 0
count_girls = 0
for i in range(n):
    h = int(input())
    if h < 0:
        sum_boys += abs(h)
        count_boys += 1
    else:
        sum_girls += h
        count_girls += 1

avg_boys = sum_boys / count_boys
avg_girls = sum_girls / count_girls
print("Средний рост девочек:", avg_boys)
print("Средний рост мальчиков:", avg_girls)