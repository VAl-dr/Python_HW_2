# Даны две строки. Удалить в первой строке первое вхождение второй строки.

def f(str_1, str_2):

    result = ' '

    for i in str_1.split(str_2):
        result += i + ' '

    result = result.rstrip()

    print(result)

f('Даны две строки. Удалить в первой строке первое вхождение второй строки.', 'две строки.')
