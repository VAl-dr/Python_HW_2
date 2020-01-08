# Дан массив строк. Переставить строки в зависимости от количества цифр в строке.

def f(str_array):

    num_array = []
#    zero = 0

    for i in str_array:
        n = 0
        if i.isalpha():
            num_array.append(0)
#            zero += 1
        elif i.isdigit():
            num_array.append(len(i))
        elif i.isalnum():
            for j in i:
                if j.isdigit():
                    n +=1
            num_array.append(n)

    for _ in range(len(num_array)):
        for j in range(1, len(num_array)):
            if num_array[j-1] > num_array[j]:
                min_num = num_array[j]
                min_str = str_array[j]
                num_array[j] = num_array[j - 1]
                str_array[j] = str_array[j - 1]
                num_array[j - 1] = min_num
                str_array[j - 1] = min_str

#    str_array = str_array[(zero + 1):] + str_array[:(zero + 1)]

    print(str_array)

f(['dhf', 'fd5nn432b', 'f', '44', 'ttttt', 'ggrgt6tgr'])