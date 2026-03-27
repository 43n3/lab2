#Известна масса каждого предмета в кг., загружаемого в грузовик. Определить,
#возможна ли перевозка груза, если грузоподъемность грузовика равна p кг.
gruz=int(input())
massa=int(input())
summa=0
while massa!=0:
    summa+=massa
    massa=int(input())
if summa<=gruz:
    print("Перевозка возможна")
else:
    print("Перевозка невозможна")