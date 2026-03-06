quantidade = int(input())
coelho = sapo = rato = 0

for i in range(1,quantidade + 1):
    qtde = input().split()
    a,b, = qtde
    if b == 'C':
        coelho += int(a)
    if b == 'R':
        rato += int(a)
    if b == 'S':
        sapo += int(a)
    total = coelho + sapo + rato
    pc = (coelho/total) *100
    pr = (rato/total)*100
    ps = (sapo/total)*100
    print('Total: {} cobaias'.format(total))
    print('Total de coelhos: {}'.format(coelho))
    print('Total de ratos: {}'.format(rato))
    print('Total de sapos: {}'.format(sapo))
    print('Percentual de coelhos: {:.2f} %'.format(pc))
    print('Percentual de ratos: {:.2f} %'.format(pr))
    print('Percentual de sapos: {:.2f} %'.format(ps))