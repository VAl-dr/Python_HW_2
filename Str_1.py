title = "В ЮАР всё плохо!"
b = ''
for word in title.split():
    if word[0].istitle():
        b += word + ' '
    else:
        b += word.capitalize() + ' '
b = b.rstrip()
print(b)