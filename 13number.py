#Для введенных с клавиатуры положительных целых чисел a и b (a≤b) определите:
# сумму всех целых чисел от a до b;
# произведение всех целых чисел от a до b;
# среднее арифметическое всех целых чисел от a до b;
# среднее геометрическое нечетных чисел от a до b.
#Отрезок поиска включает сами числа a и b. При выводе вещественных результатов
#оставьте два знака после запятой.
a=int(input())
b=int(input())
summa_all=0
prod_all=1
count=0
prod_nechet=1
count_nechet=0
for i in range(a, b+1):
    summa_all+=i
    prod_all*=i
    count+=1
    if i%2!=0:
        prod_nechet*=i
        count_nechet+=1
avg=summa_all/(b-a+1)
geo=prod_nechet**(1/count_nechet)
print(summa_all)
print(prod_all)
print(round(avg,2))
print(round(geo,2))