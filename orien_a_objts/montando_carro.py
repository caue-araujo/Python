class carro:
    def __init__(self, marca, valor, num_portas, tanque):
        self.marca = marca
        self.valor = valor
        self.num_portas = num_portas
        self.tanque = tanque
    def __str__(self):
        return f'marca: {self.marca} | valor do carro: {self.valor} | numero de portas:{self.num_portas} | tanque: {self.tanque} | {self.km}  km(s) rodado(s) |  {self.litros} litros abastecido' 
    def abastecer(self, litros):
        self.litros = litros 
        self.tanque += litros
        if self.tanque <= 0:
            self.tanque += litros
    def dirigir(self, km):
        self.km = km
        self.tanque -= km

#main 
polo = carro('bmw', 78000, 4, 15)

while True:
    a = int(input(('digite 1 para para abastecer | 2 para dirigir e 3 para sair: ')))
    if a == 1:
        polo.abastecer(int(input('digite a quantidade de litro abastecido: ')))
    elif a == 2:
        polo.dirigir(int(input('digite quantidade de km rodado: ')))
    else:
        print('fim da brincadeira!!!!!!!!!!!')
        break

