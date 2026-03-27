#Известны год и номер месяца сегодняшнего дня, а также год и номер месяца
#рождения человека (нумерация месяцев с 1: январь - 1 и т.д.). Определите возраст
#человека (число полных лет).
year_now=int(input())
month_now=int(input())
year_person=int(input())
month_person=int(input())
yy=year_now-year_person
mm=month_now-month_person
if month_now < month_person:
    yy -= 1
print(yy)