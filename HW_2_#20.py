# Даны два слова. Найдите только те символы слов, которые встречаются в обоих словах только один раз.

def s_list(a):

    list_a = []

    for i in a:
        list_a += i

    list_a.sort()

    for _ in range(len(list_a)):
        if list_a.count(list_a[0]) > 1:
            for _ in range(list_a.count(list_a[0])):
                list_a.remove(list_a[0])
        else:
            list_a.append(list_a[0])
            list_a.remove(list_a[0])
    return(list_a)

def find_same_letters(word_1, word_2):

    same_letters = []

    for i in s_list(word_1):
        for j in s_list(word_2):
            if j == i:
                same_letters += j
    if len(same_letters) == 0:
        print('Совпадений по единичным символам нету!')
    else:
        print(same_letters)

find_same_letters('approximated', 'counterclockwise')