# Строка состоит из слов, разделенных одним или несколькими пробелами.
# Поменяйте местами наибольшее по длине слово и наименьшее.

def max_to_min_to_max(text):

    min_word = text.split(' ')[0]
    max_word = ''
    num_min, num_max = 0, 0

#

    for i in text.split(' '):

        if i.isalpha():
            if len(i) < len(min_word):
                min_word = i
            if len(i) > len(max_word):
                max_word = i
        else:
            if ((len(i) - 1) < len(min_word)) and (i != ''):
                min_word = i[:-1]
            if (len(i) - 1) > len(max_word):
                max_word = i[:-1]

#

    word_array = text.split(' ')

    for j in word_array:
            if (j != max_word) and (j[:-1] != max_word):
                num_max += 1
            else:
                break
    for j in word_array:
            if (j != min_word) and (j[:-1] != min_word):
                num_min += 1
            else:
                break

#

    if word_array[num_min].isalpha():
        word_array[num_min] = max_word
    else:
        word_array[num_min] = max_word + word_array[num_min][-1]

    if word_array[num_max].isalpha():
        word_array[num_max] = min_word
    else:
        word_array[num_max] = min_word + word_array[num_max][-1]

#

    result = ''

    for i in word_array:
        result += i + ' '

    result = result.rstrip()

    print(text)
    print(result)

max_to_min_to_max('These nested replacement fields may contain a field name, conversion flag and format '
                  'specification, but deeper nesting is not allowed.')