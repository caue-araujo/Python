class veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self, ligado):
        self.ligado = ligado
        print("vrumm") if ligado == 'true' else print('off')

class carro(veiculo):
    def __init__(self, rodas, marca,teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar

class caminhao(carro):
    def __init__(self, rodas, marca, teto_solar, bau):
        super().__init__(rodas, marca, teto_solar)
        self.bau = bau

    

        

    
    
    
ferrari = carro(4, "Audi", True)
print(ferrari.teto_solar)
print(ferrari.marca)
print(ferrari.rodas)
ferrari.ligar('true')
caminhaoo = caminhao(6, 'volvo', True, True)
print(caminhaoo.teto_solar)
