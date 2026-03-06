qtde_par = 0
qtde_impar = 0
qtde_pos = 0
qtde_neg = 0

for i in range(5):
    num = int(input())

    if num % 2 == 0:
        qtde_par += 1
    if num % 2 != 0:
        qtde_impar += 1
    if num > 0:
        qtde_pos += 1
    if num < 0:
        qtde_neg += 1

print('{} valor(es) par(es)'.format(qtde_par))
print('{} valor(es) impar(es)'.format(qtde_impar))
print('{} valor(es) positivo(s)'.format(qtde_pos))
print('{} valor(es) negativo(s)'.format(qtde_neg))