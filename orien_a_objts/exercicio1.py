class Carro:
    def __init__(self,portas,motor,tetos,marca, preço):
        self.portas = portas
        self.motor = motor
        self.tetos = tetos
        self.marca = marca
        self.preço = preço


polo  = Carro(4,1.0,True,'BMW', 1500)

print(polo.portas)
print(polo.marca)
print(polo.motor)
print(polo.preço)
print(polo.tetos)

