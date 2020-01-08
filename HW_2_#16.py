# Даны две строки. Вывести большую по длине строку столько раз, на сколько символов отличаются строки.

def f(str_1, str_2):

    if len(str_2) == len(str_1):
        print('Строки равны по количеству символов.')
    if len(str_1) > len(str_2):
        max = str_1
        min = str_2
    elif len(str_2) > len(str_1):
        max = str_2
        min = str_1
    if len(str_2) != len(str_1):
        for i in range(len(max) - len(min)):
            print(max)

f('aaaa', 'bbbb')