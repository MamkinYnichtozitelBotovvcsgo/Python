a = int(input())
b = int(input())
c = int(input())

x = ('Такой треугольник существует')
y = ('Невозможно')

if a + b > c and a + b != c:
    print (x)
elif b + c > a and b + c != a:
    print (x)
elif c + a > b and c + a != b:
    print (x)
elif c == a == b:
    print (x)
elif a + b <= c:
    print (y)
elif a + c <= b:
    print (y)
elif b + c <= a:
    print (y)
elif a == b or b == c or a == c:
    print (y)
else:
    print ('Ты тупой, мальчик?!')
    

