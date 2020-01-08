a = 'But their use is allowed for new code and for big refactorings.'
b = ''
title = ''
for i in a.split():
    title = b
    if len(b) <= 26:
        b += i + ' '
    if len(b) > 26:
        break
print(title + '...')