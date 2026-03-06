num = float(input())
porcentagem = 0
if num >= 0 and num <= 2000:
    print('Isento')
elif num > 2000.01 and num <= 3000.00:
    porcentagem = (1000 * 8) / 100 
    print('R$ {:.2f}'.format(porcentagem))
elif num > 3000.01 and num < 4500.00:
    porcentagem = (1000 * 18) / 100
    print('R$ {:.2f}'.format(porcentagem))
elif num > 4500.00:
    porcentagem = (1000 * 28) / 100
    print('R$ {:.2f}'.format(porcentagem))
