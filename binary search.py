# Дан массив неповторяющихся чисел, который был отсортирован,
# а затем циклически сдвинут на неизвестное число позиций.
# Опишите без кода и псевдокода алгоритм поиска максимума в таком массиве
# Оцените сложность предложенного алгоритма
# Изменится ли сложность если массив содержит повторяющиеся числа?

from time import perf_counter


def divide(lst):
    mid = len(lst) // 2
    if lst[mid] > lst[-1]:
        return lst[mid:]
    else:
        return lst[:mid + 1]


def find_max(arr):
    if arr[0] <= arr[-1]:
        return arr[-1]
    lst = divide(arr)
    while True:
        if len(lst) == 1 or lst[0] > lst[1] or lst[0] == lst[1] and len(lst) == 2:
            return lst[0]
        lst = divide(lst)


# array = list(range(int(1e7), int(10e7))) + [int(1e10), int(1e10)] + list(range(100000))
# array = [11, 12, 13] + list(range(3))
array = [3, 3, 4, 5, 2, 2, 2]
# array = [1]
# array = list(range(5))
start = perf_counter()
print(find_max(array))
print(perf_counter() - start)
