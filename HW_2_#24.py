# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов,
# иначе дополнить строку символами 'o' до длины 12.

def f(str_1):

    if len(str_1) > 10:
        str_1 = str_1[:6]
    else:
        for _ in range(12 - len(str_1)):
            str_1 += 'o'
    print(str_1)

f('rrrrrrrrrr')