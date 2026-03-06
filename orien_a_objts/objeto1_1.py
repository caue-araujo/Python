class Pessoa:
    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

caue = Pessoa(input('Digite o nome: '),int(input('Digite a idade: ')), input('diga a profissão: '))

print(caue)
print(type(caue))
print(caue.nome)
print(caue.idade)
print(caue.profissao)

if caue.nome == 'Cauê':
    print(True)
else:
    print(False)