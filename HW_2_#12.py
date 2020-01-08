# В строке записано десятичное число. Запишите данное число римскими цифрами.

def Dec_to_Rom(a):
    dec = [1000, 500, 100, 50, 10, 5, 1]
    rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    b = a
    Result = ''
    for i in range(len(dec)):
        if (int(a[0]) == 4) or (int(a[0]) == 9):
            if int(a) // dec[i] == 9:
                Result += rom[i] + rom[i - 2]
                a = str(int(a) % dec[i])
            elif int(a) // dec[i] == 4:
                Result += rom[i] + rom[i - 1]
                a = str(int(a) % dec[i])
        else:
            Result += (int(a) // dec[i]) * rom[i]
            a = str(int(a) % dec[i])
    print(b, '-', Result)

Dec_to_Rom('1984')
