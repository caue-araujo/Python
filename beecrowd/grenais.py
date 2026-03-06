grenais = inter = gremio = empates = novo = qtde_inter= qtde_gremio= 0
while True:
    print('Novo grenal (1-sim 2-nao)')
    if novo == 2:
        break
    grenais += 1
    inter, gremio = input().split()
    inter,gremio = int(inter), int(gremio)
    novo = int(input())
    if inter > gremio:
        qtde_inter += 1
    if gremio > inter:
        qtde_gremio += 1
    if inter == gremio:
        empates += 1
        
print('{} grenais'.format(grenais))
print('Inter:{}'.format(qtde_inter))
print('Gremio:{}'.format(qtde_gremio))
print('Empates:{}'.format(empates))
if qtde_inter > qtde_gremio:
    print('Inter venceu mais')
else:
    print('gremio venceu mais')
