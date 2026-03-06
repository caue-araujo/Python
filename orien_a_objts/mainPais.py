from pais import paiss
brasil = paiss(8516000, 'Brasil', 'Distrito Federal')
argetina = paiss(278000, 'Argentina', 'Bueno Aires')
eua = paiss(8005151, 'Estados Unidos', 'washington')
brasil.adicionar_fronteira("argentina")
brasil.adicionar_fronteira("mexico")
if brasil.faz_fronteira('mexico'):
    print('sim, faz fronteira com o Brasil')
else:
    print('nao faz fronteira com o brasl')
print(argetina)
print(brasil)
print(eua)
