resto = float(input())

nota100 = resto // 100
resto = resto % 100
nota50 = resto // 50
resto = resto % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota5 = resto // 5
resto = resto % 5
nota2 = resto // 2
resto = resto % 2
moeda1 = resto // 1
resto = resto % 1
moeda050 = resto // 0.50
resto = resto % 0.50
moeda025 = resto // 0.25
resto = resto % 0.25
moeda10 = resto // 0.10
resto = resto % 0.10
moeda5 = resto // 0.05
resto = resto % 0.05
moeda01 = resto // 0.01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(nota100))
print('{:.0f} nota(s) de R4 50.00'.format(nota50))
print('{:.0f} nota(s) de R$ 20.00'.format(nota20))
print('{:.0f} nota(s) de R$ 10.00'.format(nota10))
print('{:.0f} nota(s) de R$ 5.00'.format(nota5))
print('{:.0f} nota(s) de R$ 2.00'.format(nota2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(moeda1))
print('{:.0f} moeda(s) de R$ 0.50'.format(moeda050))
print('{:.0f} moeda(s) de R$ 0.25'.format(moeda025))
print('{:.0f} moeda(s) de R$ 0.10'.format(moeda10))
print('{:.0f} moeda(s) de R$ 0.05'.format(moeda5))
print('{:.0f} moeda(s) de R$ 0.01'.format(moeda01))