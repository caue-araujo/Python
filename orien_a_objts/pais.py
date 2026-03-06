class paiss:
    def __init__(self, tamanho, nome, nome_capital):
        self.tamanho = tamanho
        self.nome = nome
        self.nome_capital = nome_capital
        self.fronteira = []
    @property
    def nome_pais(self):
        return self.__nome
    @nome_pais.setter
    def nome_pais(self, nome):
        self.__nome = nome
    
    @property
    def capital(self):
        return self.__nome_capital
    @capital.setter
    def capital(self, nome_capital):
        self.__nome_capital = nome_capital

    @property
    def dimensao(self):
        return self.__tamanho
    @dimensao.setter
    def dimensao(self, tamanho):
        self.__tamanho = tamanho
    
    def adicionar_fronteira(self, pais:str):
        pais = pais.lower()

        if pais in self.fronteira:
            return False
        else:
            self.fronteira.append(pais)
            return True
    def __str__(self):
        return f'{self.nome}, {self.nome_capital}, {self.tamanho} km²'

    def faz_fronteira(self, outro_pais: "pais") -> bool:
        return outro_pais.lower() in self.fronteira


