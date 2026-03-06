from conta_corrente import contaCorrente
contas = []

for i in range(1):
    '''
    cada numero de conta tem que ser preenchido de forma crescente, começando a partir do 0,
    para assim o código funcionar perfeitamente
    '''
    numero = int(input('numero da conta: '))
    nome_titular = input('nome do titular da conta: ')
    saldo = float(input('Saldo: '))
    conta = contaCorrente(nome_titular, numero, saldo)
    contas.append(conta)
print(contas)
opcao = None

while opcao != "r":
    print()
    print("(d) Depositar")
    print("(s) Sacar")
    print("(ss) Saldo")
    print("(r) Sair")

    print("===============")
    opcao = input("Opção: ")

    if opcao == "d":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor a ser depositado: "))
        contas[numero].depositar(valor)

    elif opcao == "s":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor a ser sacado: "))
        if contas[numero].sacar(valor):
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    elif opcao == "ss":
        numero = int(input("Número da conta: "))
        print(contas[numero])

