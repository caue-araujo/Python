salario = float(input('Digite um número: '))

if salario >= 0 and salario <= 400.00:
    novo_salario = (salario * 15) / 100
    salario += novo_salario
    percentual = 15
elif salario >= 400.01 and salario <= 800.00:
    novo_salario = (salario * 12) / 100
    salario += novo_salario
    percentual = 12
elif salario >= 800.01 and salario <= 1200.00:
    novo_salario = (salario * 10) / 100
    salario += novo_salario
    percentual = 10
elif salario >= 1200.01 and salario <= 2000.00:
    novo_salario = (salario * 7) /100
    salario += novo_salario
    percentual = 7
else:
    novo_salario = (salario * 4) /100
    salario += novo_salario
    percentual = 4

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(novo_salario))
print('Em percentual: {} %'.format(percentual))




