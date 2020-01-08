# Дан текст. Найдите наибольшее количество подряд идущих пробелов в нем.

def space_function(text):

    n = 1
    q = []

    for i in range(len(text)):
        if text[i] != ' ':
            continue
        elif (text[i] == ' ') and (text[i + 1] == ' '):
            n += 1
        else:
            if n > 1:
                q.append(n)
                n = 1
    print('Наибольшее количество подряд идущих пробелов -', max(q))


space_function('  These  nested replacement fields may contain    a field name, conversion flag   and format '
               'specification, but    deeper nesting       is not   allowed.')