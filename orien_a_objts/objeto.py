class Pessoa:
    def __init__(self,nome,idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

caue = Pessoa('Cauê', 18, 'Programador')

print(caue)
print(type(caue))
print(caue.nome)
print(caue.idade)
print(caue.profissao)

if caue.nome == 'Cauê':
    print(True)
else:
    print(False)

if caue.idade >= 18:
    print('Ele é maior de 18')


print(type(caue))