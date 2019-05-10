from stack_class import Stack
import doctest
#import cProfile

# Упражнение №1
"""
s = Stack()
for i in range(1, 11):
    s.push(i)
while not s.is_empty():
    print(s.pop())
"""


# Упражнение №2
def str_valid(string):
    """
    >>> str_valid('//(/){}')
    False
    >>> str_valid('/(/{/(//{})/}/)///')
    True
    """
    prev = ''
    while string != prev:
        prev = string
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        string = string.replace('//', '')
        string = string.replace('<>', '')
    return not string


def stack_str_valid(string):
    """
    >>> stack_str_valid('[](]){}')
    False
    >>> stack_str_valid('[([]{})]')
    True
    """
    stack = Stack()
    for i in string:
        if i in '({[':
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            item = stack.pop()
            if i == ')' and item == '(':
                pass
            elif i == '}' and item == '{':
                pass
            elif i == ']' and item == '[':
                pass
            else:
                return False
    return stack.is_empty()


# cProfile.run("stack_str_valid('{}[()[]{{}}]'*100000)")
# cProfile.run("str_valid('{}[()[]{{}}]'*100000)")

# Упражнение №3
"""
(3+4∗(2−1))/5
Обратная польская нотация: 3 4 2 1 - * + 5 /
Прямая польская нотация: / + 3 * 4 - 2 1 5
"""


# Упражнение №4
def rpn(expr):
    """
    >>> rpn('2 3 - 12 10 - * 4 2 / +')
    0.0
    >>> rpn('3 4 2 1 - * + 5 /')
    1.4
    >>> rpn('3 4 2 1 - + * + 5 /')
    Выражение составлено некорректно!
    >>> rpn('3 4 2 1 - k * + 5 /')
    Выражение составлено некорректно!
    >>> rpn('3')
    3.0
    >>> rpn('/')
    Выражение составлено некорректно!
    >>> rpn('')

    >>> rpn('y')
    Выражение составлено некорректно!
    """
    if not expr:
        return
    s = Stack()
    for i in expr.split():
        try:
            if i.isdigit():
                s.push(i)
            elif i in '+-*/':
                y = s.pop()
                x = s.pop()
                s.push(str(eval(x + i + y)))
            else:
                raise
        except:
            print('Выражение составлено некорректно!')
            return
    res = float(s.pop())
    if s.is_empty():
        return res
    else:
        print('Выражение составлено некорректно!')


# Упражнение №5
def to_rpn(expr):
    """
    >>> to_rpn('2 + 3')
    '2 3 +'
    >>> to_rpn('2 - 3 * 4 + 8')
    '2 3 4 * - 8 +'
    >>> to_rpn('( 2 - 3 ) *  ( 12 - 10 ) + 4 / 2')
    '2 3 - 12 10 - * 4 2 / +'
    >>> to_rpn('2 + 4 * ( 0 ) / 3 + ( 7 * ( 15 - 3 + ( 9 / ( 1 ) ) ) )')
    '2 4 0 * 3 / + 7 15 3 - 9 1 / + * +'
    >>> to_rpn('( 3 + 4 * ( 2 - 1 ) ) / 5')
    '3 4 2 1 - * + 5 /'
    """
    priority = {'+': 1, '-': 1, '/': 2, '*': 2, '(': 0, ')': 0}
    res = []
    s = Stack()
    for i in expr.split():
        if i.isdigit():
            res.append(i)
        elif i in '+-/*':
            while not s.is_empty():
                x = s.pop()
                if (priority[i] <= priority[x]) or (priority[i] == priority[x] and i not in '-/'):
                    res.append(x)
                else:
                    s.push(x)
                    break
            s.push(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            x = s.pop()
            while x != '(':
                res.append(x)
                x = s.pop()
    while not s.is_empty():
        res.append(s.pop())
    return ' '.join(res)


doctest.testmod()
