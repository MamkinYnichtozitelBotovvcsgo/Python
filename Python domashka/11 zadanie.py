a = int(input())

if a > 0 and a % 2 == 0:
    print (f'{a} - положительное четное число')
else:
    print (f'{a} - положительное нечетное число')

if a < 0 and a % 2 == 0:
    print (f'{a} - отрицательное четное число')
else:
    print (f'{a} - отрицательное нечетное число')
    
if a == 0:
    print (f'{a} - нулевое число')
