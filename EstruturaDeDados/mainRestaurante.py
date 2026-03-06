from restaurante import *

# Exemplo de uso
try:
    restaurante = FilaRestaurante()

    while True:
        restaurante.exibir_filas()
        print("(e) Inserir cliente na fila de atendimento")
        print("(c) Chamar cliente em espera")
        print("(i) Iniciar preparo da refeição")
        print("(r) Realizar entrega do pedido")
        print("(s) Sair do programa")
        opcao = input("Opção: ")

        if opcao.lower() == "e":
            restaurante.inserir_cliente()

        elif opcao.lower() == "c":
            restaurante.chamar_cliente()

        elif opcao.lower() == "i":
            restaurante.iniciar_preparo()

        elif opcao.lower() == "r":
            restaurante.realizar_entrega()

        elif opcao.lower() == "s":
            break

        else:
            print("Opção inválida. Tente novamente.")


except KeyboardInterrupt:
    print("O Programa foi encerrado pelo usuário - (CTRL ^C)")
