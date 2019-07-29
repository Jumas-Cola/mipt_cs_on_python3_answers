# Упражнение 1
import matplotlib.pyplot as plt
import time
import os


def get_pop_time(size, repeat_count, pop_position=None):
    '''
    size - размер списка из нулей на котором будем тестировать скорость операции pop
    repeat_count - количество повторений для усреднения
    pop_position - позиция с которой делаем pop
    '''
    l = [0] * size
    start_time = time.time()

    for _ in range(repeat_count):
        l.pop() if pop_position is None else l.pop(pop_position)
        l.append(0)

    end_time = time.time()
    return (end_time - start_time) / repeat_count


cwd = os.path.dirname(os.path.abspath(__file__))

# repeat_count = 10000
# values1 = [get_pop_time(size, repeat_count) for size in range(10, 1000)]
# values2 = [get_pop_time(size, repeat_count, 0) for size in range(10, 1000)]
# values3 = [get_pop_time(size, repeat_count, -1) for size in range(10, 1000)]
#
# plt.plot(values1, label='Pop no args')
# plt.plot(values2, label='Pop start list')
# plt.plot(values3, label='Pop end list')
# plt.ylabel('pop time')
# ax = plt.subplot(111)
# ax.legend()
# plt.show()


# Упражнение 2
# A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
# B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
# for x in A:
#     if x not in B:
#         print(x, end='')


# Упражнение 3
# A = set('0123456789')
# B = set('02468')
# C = set('12345')
# D = set('56789')
# E = ((A - B) & (C - D)) | ((D - A) & (B - C))
# print(E)


# Упражнение 4
# import string
#
# with open(os.path.join(cwd, 'LICENSE.txt')) as f:
#     text = f.read().translate(str.maketrans('', '', string.punctuation)).lower()
#
# max_freq_elems = {}
# text_list = text.split()
# text_dict = {word: text_list.count(word) for word in text_list}
#
# for _ in range(10):
#     max_freq = 0
#     max_elem = None
#     for key in text_dict:
#         if (text_dict[key] >= max_freq) and (key not in max_freq_elems):
#             max_elem = key
#             max_freq = text_dict[key]
#     max_freq_elems[max_elem] = max_freq
#
# print(max_freq_elems)


# Упражнение 5
# with open(os.path.join(cwd, 'task4_en-ru'), encoding='utf-8') as f:
#     en_ru = {pair.split('	-	')[0]: pair.split('	-	')[1].strip()
#              for pair in f.readlines()}
#
# with open(os.path.join(cwd, 'task4_input.txt'), encoding='utf-8') as inp:
#     out = open(os.path.join(cwd, 'task4_output.txt'), 'w')
#     for line in inp.readlines():
#         out.write(line)
#         out.write(' '.join(
#             [en_ru[word.lower()] if word.lower() in en_ru else word for word in line.split()])+'\n')
#     out.close()


# Упражнение 6
# with open(os.path.join(cwd, 'task5_input.txt'), encoding='utf-8') as inp:
#     cntry_lngs = {s.split(' : ')[0]: s.split(' : ')[1].split() for s in inp.readlines()}
# lng_cntrys = {}
# for c in cntry_lngs:
#     for l in cntry_lngs[c]:
#         if l in lng_cntrys:
#             lng_cntrys[l].append(c)
#         else:
#             lng_cntrys[l] = [c]
#
# with open(os.path.join(cwd, 'task5_output.txt'), 'w', encoding='utf-8') as out:
#     for i in lng_cntrys:
#         out.write(f'{i} : {" ".join(lng_cntrys[i])}\n')


# Упражнение 7
# with open(os.path.join(cwd, 'task6_en-ru.txt'), encoding='utf-8') as inp:
#     cntry_lngs = {s.split('	-	')[0]: s.split('	-	')[1].strip().split(', ') for s in inp.readlines()}
# lng_cntrys = {}
# for c in cntry_lngs:
#     for l in cntry_lngs[c]:
#         if l in lng_cntrys:
#             lng_cntrys[l].append(c)
#         else:
#             lng_cntrys[l] = [c]
#
# with open(os.path.join(cwd, 'task6_ru-en.txt'), 'w', encoding='utf-8') as out:
#     for i in sorted(lng_cntrys.keys()):
#         out.write(f'{i}	-	{", ".join(lng_cntrys[i])}\n')


# Упражнение 8
# with open(os.path.join(cwd, 'task7_en-ru.txt'), encoding='utf-8') as inp:
#     en_ru = {s.split('	-	')[0]: s.split('	-	')[1].strip().split(',') for s in inp.readlines()}
# with open(os.path.join(cwd, 'task7_ru-en.txt'), encoding='utf-8') as inp:
#     ru_en = {s.split('	-	')[0]: s.split('	-	')[1].strip().split(',') for s in inp.readlines()}
#
# for en_word in en_ru:
#     for ru_word in en_ru[en_word]:
#         if ru_word not in ru_en:
#             ru_en[ru_word] = [en_word]
#         else:
#             if en_word not in ru_en[ru_word]:
#                 ru_en[ru_word].append(en_word)
#
# for ru_word in ru_en:
#     for en_word in ru_en[ru_word]:
#         if en_word not in en_ru:
#             en_ru[en_word] = [ru_word]
#         else:
#             if ru_word not in en_ru[en_word]:
#                 en_ru[en_word].append(ru_word)
#
# with open(os.path.join(cwd, 'task7_ru_en.txt'), 'w', encoding='utf-8') as out:
#     for i in sorted(ru_en.keys()):
#         out.write(f'{i}	-	{", ".join(ru_en[i])}\n')
#
# with open(os.path.join(cwd, 'task7_en_ru.txt'), 'w', encoding='utf-8') as out:
#     for i in sorted(en_ru.keys()):
#         out.write(f'{i}	-	{", ".join(en_ru[i])}\n')
