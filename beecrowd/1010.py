soma_total = 0
soma1 = 0
soma2 =0
codigo1,num1,valor1 = input().split()
codigo2, num2,valor2 = input().split()
codigo1,num1, codigo2,num2 = int(codigo1), int(num1),int(codigo2), int(num2)
valor1,valor2 = float(valor1), float(valor2)
soma1 += (valor1* num1)
soma2 += (valor2 * num2)
soma_total = soma1 + soma2

print('VALOR A PAGAR: R$ {:.2f}'.format(soma_total))
