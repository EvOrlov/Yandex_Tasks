from random import shuffle, randrange
from time import perf_counter


class NodeTree:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None


def insert(root, key, correct=True):
    if root is None:
        return NodeTree(key)
    elif root.value > key:
        # correct = False создает ошибку в BST для теста
        if correct:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    elif root.value < key:
        if correct:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def is_bst(root):
    # Функция позволяет обойти дерево и проверить, является ли дерево BST за один проход без создания списка.
    # В случае обнаружения ошибки, алгоритм прерывается на ошибке
    # Работает следующм образом:
    # Двигаемся по левой ветке до конца, все пройденные узлы записываем с стек
    # Снимаем по одному узлу со стека.
    # Если у узла есть правая ветвь, переходим туда и повторяем цикл: левая ветвь в стек, снимаем, ищем правую
    stack = []
    prev, visited = None, None
    while True:
        # проход по левой ветке до конца с записью узлов в стек
        # visited ограничивает повторное движение по той же левой ветке
        while root and root != visited:
            stack.append(root)
            root = root.left
        # если в правой ветке ничего нет и стек пуст, проверка завершена. Это BST.
        if not stack and not root.right:
            return True
        visited = stack.pop()
        root = visited
        print(root.value, end=' ')
        # если предыдущее число не меньше последующего, это не BST. Проверка завершена.
        if prev and prev >= root.value:
            return False
        prev = root.value
        if root.right:
            root = root.right


lst = list(range(1, 1000))
shuffle(lst)
print(f'Случайный список: {lst}')
rand = randrange(1, 1000)
print(f'Случайное неправильное число: {rand}')
print(f'Случайный корень дерева: {lst[-1]}')
t = NodeTree(lst.pop())
for i in lst:
    if i == rand:
        t = insert(t, i, False)
    else:
        t = insert(t, i)
start = perf_counter()
print(f'\nЭто{[" НЕ ", " "][is_bst(t)]}двоичное дерево поиска')
print(f'Время выполнения проверки: {perf_counter() - start}')
