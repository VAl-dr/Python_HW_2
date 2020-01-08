# Дано натуральное число. Получить строку, в которой тройки цифр этого числа разделены пробелом,
# начиная с правого конца. Например, число 1234567 преобразуется в 1 234 567.

def Int_to_Str(a):

    k = 3
    str_a = str(a)[::-1]

    if len(str_a) % k == 0:
        n = 2 * (len(str_a) // k) - 1
    else:
        n = 2 * (len(str_a) // k) + 1

    str_b = [' '] * n

    for i in range(0, n, 2):
        str_b[i] = str_a[int(i / 2 * k):int((i / 2 + 1) * k)]

    Result = ''

    for i in str_b:
        Result += i

    Result = Result[::-1]

    print(str_a[::-1], '-', Result)

Int_to_Str(5465246546582)