class contaCorrente:
    def __init__(self, nome_titular, numero, saldo):
        self.nome_titular = nome_titular
        self.numero = numero
        self.saldo = saldo
    
    @property
    def nome_titular(self):
        return self.__nome_titular
    
    @nome_titular.setter
    def nome_titular(self, nome_titular):
        self.__nome_titular = nome_titular
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    def depositar(self, valor: float):
        self.saldo += valor
    
    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False
    def __str__(self):
        return f" Número: {self.numero}, Titular: {self.nome_titular}, Saldo: {self.saldo}"
    