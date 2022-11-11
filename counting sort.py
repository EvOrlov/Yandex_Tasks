# Дан неупорядоченный массив из печатных ASCII символов
# Опишите своими словами (без кода и псевдокода) алгоритм сортировки, позволяющий упорядочить этот массив
# по алфавиту за линейное время
# Необходимо описать действия на каждом шаге алгоритма
# Возможен ли стабильный вариант такого алгоритма сортировки?

asc = list(input())
out = [[] for i in range(96)]
for i in range(len(asc)):
    out[ord(asc[i]) - 32].append(i)
for i in range(96):
    print(chr(i + 32) * len(out[i]), end='')
