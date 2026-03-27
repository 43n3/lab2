'''Вводится список из n годовых вкладов, предлагаемых банками, в формате:
Банк Сумма Процент
где:
 все значения разделены пробелом и сами не содержат пробелов;
 наименование банка уникально;
 Сумма: сумма для открытия вклада в руб. (целое число, >0);
 Процент: годовой процент по вкладу (вещественное число, (0,100]).
Сохраните введенные данные в виде списка словарей:
[
{"name": "Банк 1", "initial_sum": 50000, "rate": 5.2},
...
]
Далее определите (гарантируется, что искомый банк - один):
 самый доступный банк (с наименьшей первоначальной суммой);
 самый выгодный банк, принимая, что за
год прибыль = сумма * процент / 100.
При выводе финансовых значений оставьте два знака после запятой.'''


n = int(input())
banks = []

for _ in range(n):
    s = input().split()
    bank = {
        "name": s[0],
        "initial_sum": int(s[1]),
        "rate": float(s[2])
    }
    banks.append(bank)

cheap = banks[0]
for b in banks:
    if b["initial_sum"] < cheap["initial_sum"]:
        cheap = b

best = banks[0]
for b in banks:
    profit = b["initial_sum"] * b["rate"] / 100
    best_profit = best["initial_sum"] * best["rate"] / 100
    if profit > best_profit:
        best = b

cheap_profit = cheap["initial_sum"] * cheap["rate"] / 100
best_profit = best["initial_sum"] * best["rate"] / 100

print("Доступный:", cheap["name"], f"{cheap['initial_sum']:.2f}")
print("Выгодный:", best["name"], f"{best_profit:.2f}")