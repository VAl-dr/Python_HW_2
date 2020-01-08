# В строке найдите все серии подряд идущих пробелов и замените каждую на один пробел.

def f(text):

    result = ''

    for word in text.split():
        result += word + ' '

    result = result.rstrip()
    print(result)

f('Alternatively, you can   provide the entire regular   expression pattern by   overriding the class attribute pattern.')