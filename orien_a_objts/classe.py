class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    
nome_, idade_ = input("Digite o nome e a idade: ").split()
a = Pessoa(nome_, idade_)
print(a.nome)
print(a.idade)
