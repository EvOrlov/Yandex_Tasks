# Опишите словами алгоритм решения задачи
# Ввод: натуральное число n
# Вывод: количество простых чисел строго меньше n
# Решение должно быть вычислительно-эффективным


from time import perf_counter


def sieve(n):
    if n <= 2:
        return 0
    lst = [0] * n
    count = 1
    root_n = n ** 0.5
    for i in range(3, n, 2):
        lst[i] = 1
    for i in range(n):
        if lst[i]:
            count += 1
            if i <= root_n:
                for j in range(i ** 2, n, i):
                    lst[j] = 0
    return count


a = int(input())
start = perf_counter()

print(sieve(a))
print(perf_counter() - start)
