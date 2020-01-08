# Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'. Если какого-то из символов нет,
# вывести сообщение об этом.

def func(str_1):

    s1 = 'x'
    s2 = 'w'

    if str_1.find(s1) == -1:
        print(f'Символ {s1} отсутствует в строке!')
    if str_1.find(s2) == -1:
        print(f'Символ {s2} отсутствует в строке!')
    else:
        for i in range(len(str_1)):
            if str_1[i] == s1:
                num_s1 = i
                break
        for i in range(len(str_1)):
            if str_1[i] == s2:
                num_s2 = i
                break
        if num_s1 < num_s2:
            print(f'Символ {s1} расположен в строке раньше, чем символ {s2}.')
        else:
            print(f'Символ {s2} расположен в строке раньше, чем символ {s1}.')


func('Pop up a dialog window for input of a string. Parameter title is the title of the dialog window, '
     'prompt is a text mostly describing what information to input.')
