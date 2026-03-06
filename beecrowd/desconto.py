salario = float(input('Digite o salario: '))
vendas = float(input('Digite: '))

comissao = (vendas * 10) / 100
salario += comissao
print('TOTAL = R$ {:.2f}'.format(salario))