# Дан неупорядоченный массив из печатных ASCII символов
# Опишите своими словами (без кода и псевдокода) алгоритм сортировки, позволяющий упорядочить этот массив
# по алфавиту за линейное время
# Необходимо описать действия на каждом шаге алгоритма
# Возможен ли стабильный вариант такого алгоритма сортировки?

def ascii_order(lst):
    out = [[] for _ in range(96)]
    for i in range(len(lst)):
        out[ord(lst[i]) - 32].append(i)
    return ''.join([chr(i + 32) * len(out[i]) for i in range(96)])


# Формирую входной список из строки для удобства
# asc = list(input())
asc = list('lskchxtyjrtzztmpmuvwmbibpietdbabi')
print(ascii_order(asc))
print(list(ascii_order(asc)))
