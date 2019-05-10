class Stack:
    """ Инициализация объекта """

    def __init__(self, *items):
        self.stack = list(items)

    """ Очистка стека """

    def clear(self):
        self.stack = []

    """ Извлечение элемента из стека """

    def pop(self):
        return self.stack.pop()

    """ Добавление элемента в стек """

    def push(self, item):
        self.stack.append(item)

    """ Проверка на пустоту стека """

    def is_empty(self):
        return not bool(self.stack)