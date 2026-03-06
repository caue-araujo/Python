a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if b > a and b > c:
    a, b = b, a
elif c > a and c > b:
    a, c = c, a

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
    if a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
    if a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    else:
        if a == b or b == c or a == c:
            print('TRIANGULO ISOSCELES')
