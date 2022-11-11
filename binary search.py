# Дан массив неповторяющихся чисел, который был отсортирован,
# а затем циклически сдвинут на неизвестное число позиций.
# Опишите без кода и псевдокода алгоритм поиска максимума в таком массиве
# Оцените сложность предложенного алгоритма
# Изменится ли сложность если массив содержит повторяющиеся числа?

from time import perf_counter


def divide(array):
    mid = int(len(array) // 2)
    if array[mid] > arr[-1]:
        return array[mid:]
    else:
        return array[:mid + 1]


# arr = list(range(int(1e7), int(10e7))) + [int(1e10), int(1e10)] + list(range(100000))
# arr = [11, 12, 13] + list(range(3))
arr = [3, 3, 4, 5, 2, 2, 2]
start = perf_counter()
if arr[0] > arr[-1]:
    lst = divide(arr)
    while True:
        if len(lst) == 1 or lst[0] > lst[1] or lst[0] == lst[1] and len(lst) == 2:
            print(lst[0])
            break
        lst = divide(lst)
else:
    print('max=', arr[-1])
print(perf_counter() - start)
