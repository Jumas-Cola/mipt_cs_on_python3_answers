import doctest
import timeit


# Упражнение №1: Z - функция
def z_func(s):
    """
    >>> z_func('aaaaa')
    [0, 4, 3, 2, 1]
    >>> z_func('aaabaab')
    [0, 2, 1, 0, 2, 1, 0]
    >>> z_func('abacaba')
    [0, 0, 1, 0, 3, 0, 1]
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


# Упражнение №2: Поиск подстроки
def z_find(p, t):
    """
    >>> z_find('aba', 'abacabaabacabaaaaaaaaabaaa')
    (0, 4, 7, 11, 21)
    >>> z_find('', 'abacabaaba')
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> z_find('b', 'abacabaaba')
    (1, 5, 8)
    >>> z_find('b', 'spameggs')
    ()
    >>> z_find('spam', '')
    ()
    """
    len_p = len(p)
    len_t = len(t)
    z = z_func('{}#{}'.format(p, t))
    return tuple(i for i in range(len_t) if z[i + len_p + 1] == len_p)


# Упражнение №3: Количество разных подстрок
def z_substrings(s):
    """
    >>> z_substrings('abcde')
    15
    >>> z_substrings('aaaaa')
    5
    >>> z_substrings('abacabadabacaba')
    85
    """
    k = 0
    t = ''
    for i in s:
        t += i
        t_r = t[::-1]
        z_max = max(z_func(t_r))
        k += len(t) - z_max
    return k


# Упражнение №4: Период строки
def z_period(s):
    """
    >>> z_period('abcd')

    >>> z_period('abcdabcdabcd')
    4
    >>> z_period('abaabaaba')
    3
    """
    len_s = len(s)
    z = z_func(s)
    for i in range(len(z)):
        if i + z[i] == len_s and not len_s % i:
            return i


# Упражнение №5: Префикс-функция
def p_func(s):
    """
    >>> p_func('abcabcd')
    [0, 0, 0, 1, 2, 3, 0]
    """
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


# Упражнение №6: Поиск подстроки
def p_find(p, t):
    """
    >>> p_find('aba', 'aaaabaaaaba')
    [3, 8]
    """
    n = len(p)
    s = '{}#{}'.format(p, t)
    p_s = p_func(s)
    len_p_s = len(p_s)
    res = []
    for i in range(n + 1, len_p_s):
        if p_s[i] == n:
            res.append(i - 2 * n)
    return res


# Упражнение №7: Поиск подстроки онлайн
# Сдвигает строку на один символ влево и находит Pi для последнего символа
def pi_func(s, l, pi):
    n = l * 2 + 1
    pi = pi[0: l + 1] + pi[-l + 1:] + [0]
    j = pi[n - 2]
    while j > 0 and s[n - 1] != s[j]:
        j = pi[j - 1]
    if s[n - 1] == s[j]:
        j += 1
    pi[n - 1] = j
    return pi


def p_find_online():
    p = input('Введите паттерн:')
    len_p = len(p)
    char = input()
    string = ''
    counter = 1
    res = []
    pi = []
    while char:
        string += char
        if len(string) == len_p:
            if not pi:
                pi = p_func(p + '#' + string)
            else:
                pi = pi_func(p + '#' + string, len_p, pi)
            if pi[-1] == len_p:
                res.append(counter - len_p)
            string = string[1:]
        char = input()
        counter += 1
    return res


# print(p_find_online())


# Упражнение №8: Количество разных подстрок
def p_substrings(s):
    """
    >>> p_substrings('abcde')
    15
    >>> p_substrings('aaaaa')
    5
    >>> p_substrings('abacabadabacaba')
    85
    """
    k = 0
    t = ''
    for i in s:
        t += i
        t_r = t[::-1]
        p_max = max(p_func(t_r))
        k += len(t) - p_max
    return k


# Упражнение №9: Период строки
def p_period(s):
    """
    >>> p_period('abcd')

    >>> p_period('abcdabcdabcd')
    4
    >>> p_period('abaabaaba')
    3
    """
    n = len(s)
    pi = p_func(s)
    k = n - pi[n - 1]
    if n % k == 0 and n != k:
        return k


doctest.testmod()
