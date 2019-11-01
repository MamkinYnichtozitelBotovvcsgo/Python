a = int(input())

if 0 <= a <= 7:
    print ('Ночь')
elif 7 < a <= 11:
    print ('Утро')
elif 12 <= a < 17:
    print ('День')
elif 17 <= a <= 23:
    print ('Вечер')
else:
    print('Ярык, будь человеком, нет такого часа!')
