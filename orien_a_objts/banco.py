class banco:
    def __init__(self, nome, saldo):
        self.saldo = saldo
        self.nome = nome
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'{valor} depositado na conta de {self.nome}')

    def sacar(self, valor):
        self.saldo -= valor
        print(f'{valor} sacado da conta de {self.nome}')
        
    def transferencia(self, outra_conta, valorDaTransferencia):
        self.saldo -= valorDaTransferencia
        outra_conta.saldo += valorDaTransferencia


contaCaue = banco('caue', 520)
contaCaue.deposito(5000)
print(contaCaue.saldo)
contaCaue.sacar(1532)
print(contaCaue.saldo)
contaMaria = banco('maria', 55)
contaCaue.transferencia(contaMaria, 1000)
print(contaMaria.saldo)



     
