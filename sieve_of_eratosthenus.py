# Опишите словами алгоритм решения задачи
# Ввод: натуральное число n
# Вывод: количество простых чисел строго меньше n
# Решение должно быть вычислительно-эффективным


from time import perf_counter

n = int(input())
start = perf_counter()

inp = [0] * n
for i in range(3, n, 2):
    inp[i] = i
out = []
for i in inp:
    if i:
        out.append(i)
        for j in range(i**2, n, i):
            inp[j] = 0
print(len(out) + 1)
print(perf_counter() - start)
