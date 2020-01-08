# Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно.

def ab_to_AB(str_1):

    str_2 = ''

    for word in str_1.split('a'):
        str_2 += word + 'A'

    str_3 = ''

    for word in str_2.split('b'):
        str_3 += word + 'B'

    str_3 = str_3[:-2]
    print(str_1)
    print(str_3)

#ab_to_AB('These nested replacement fields may contain a field name, conversion flag and format specification, '
#         'but deeper nesting is not allowed.')
def f(ab):

    while (ab.find('a') >= 0):
        m = ab.find('a')
        ab = ab[:m] + 'A' + ab[(m + 1):]
    while (ab.find('b') >= 0):
        n = ab.find('b')
        ab = ab[:n] + 'B' + ab[(n + 1):]

    print(ab)

f('These nested replacement fields may contain a field name, conversion flag and format specification, '
  'but deeper nesting is not allowed.')