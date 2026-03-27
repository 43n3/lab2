'''Дано предложение. Выведите его на экран, удалив из него все слова, содержащие
произвольную букву (вводится с клавиатуры).'''

text = input()
letter = input()
words = text.split()
result = []
for word in words:
    if letter not in word:
        result.append(word)
print(' '.join(result))