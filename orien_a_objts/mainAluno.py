from aluno import aluno

caue = aluno('20231050', 'caue de araujo silva')
print(caue.nome) # deverá imprimir meu nome
print(caue.matricula) # deverá imprimir minha matricula
caue.adicionarNotas(10)
print(caue.media()) # media deverá ser 10
print(caue.getMatriculaFormatada()) # imprime a matricula no formato 0000.0.000
caue.adicionarNotas(8)
caue.adicionarNotas(4)
print(caue.media()) # media deverá ser 7.3
print(caue.notas) # [10,8,4]
