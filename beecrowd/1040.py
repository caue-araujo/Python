n1,n2,n3,n4 = input().split()
n1,n2,n3,n4 = float(n1),float(n2),float(n3),float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media > 5.0 or media < 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: {}'.format(nota_exame))
    nova_media = (nota_exame + media) / 2
    if nova_media >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(nova_media))
    elif nova_media < 4.9:
        print('Aluno reprovado')
        print('Media final: {:.1f}'.format(nova_media))
