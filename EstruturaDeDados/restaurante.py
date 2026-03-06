class Cliente:
    """Classe que representa um cliente do restaurante."""

    def __init__(self, nome):
        """Inicializa um cliente com um nome e nenhum pedido."""

        self.nome = nome
        self.pedido = None


class Pedido:
    """Classe que representa um pedido feito por um cliente."""

    def __init__(self, descricao):
        """Inicializa um pedido com uma descrição."""
        self.descricao = descricao


class FilaRestaurante:
    """Classe que gerencia as filas de espera, preparo e entrega do restaurante."""

    def __init__(self):
        """Inicializa as filas vazias."""
        self.fila_espera = []
        self.fila_preparo = []
        self.fila_entrega = []

    def inserir_cliente(self):
        """Adiciona um novo cliente à fila de espera."""


        nome = input("Nome do cliente: ")
        cliente = Cliente(nome)

        self.fila_espera.append(cliente)
        print(
            f"<< Aguarde... você está na {len(self.fila_espera)}º posição no atendimento. Aguarde! >>"
        )

    def chamar_cliente(self):
        """Chama o próximo cliente da fila de espera para fazer o pedido."""
        if self.fila_espera:
            cliente = self.fila_espera.pop(0)

            pedido_descricao = input(f"O que o/a sr(a) {cliente.nome} deseja? ")
            cliente.pedido = Pedido(pedido_descricao)

            print(f"Olá {cliente.nome}!")
            print(f"Informações do pedido: {cliente.pedido.descricao}")
            confirmacao = input("Confirma o pedido (S/N)? ")

            if confirmacao.lower() == "s":
                self.fila_preparo.append(cliente)
                print(f"Pedido realizado com sucesso!!! Vamos preparar seu prato.")

                print(
                    f"<< Seu pedido está na {len(self.fila_preparo)}ª posição na fila de preparo e ficará pronto em {len(self.fila_preparo) * 20} min >>"
                )
                
            else:
                print(f"Pedido do cliente {cliente.nome} cancelado.")
        else:
            print("Não há clientes a serem chamados")

    def iniciar_preparo(self):
        """Inicia a preparação do pedido para o próximo cliente na fila de preparo."""
        
        if self.fila_preparo:
            cliente = self.fila_preparo.pop(0)
            self.fila_entrega.append(cliente)

            print(f"Pedido da vez: {cliente.pedido.descricao}")
            confirmacao = input("Pedido já está pronto para entrega (S/N)? ")

            if confirmacao.lower() == "s":
                print(
                    f"<< Seu pedido está na {len(self.fila_entrega)}ª posição para entrega. É rápido, temos vários entregadores >>"
                )
            else:
                print(f"Pedido do cliente {cliente.nome} não confirmado para entrega.")
        else:
            print(f"Não existem pedidos para iniciar o preparo")

    def realizar_entrega(self):
        """Realiza a entrega do pedido para o próximo cliente na fila de entrega."""
        
        if self.fila_entrega:
            cliente = self.fila_entrega.pop(0)
            print(f"Pedido do(a) {cliente.nome} saindo para entrega!!!")
            print(f"{cliente.pedido.descricao}")  # Exibe o pedido sendo entregue

        else:
            print(f"Não há pedidos a serem entregues")

 
    def exibir_filas(self):
        """Exibe o estado atual das filas de espera, preparo e entrega."""
        print("------------------------------------")
        print("<< Filas >>")
        print("------------------------------------")
        print("Espera        Preparo       Entrega")
        print("=" * 14, "=" * 14, "=" * 14)
        
        # Define um flag para indicar se o primeiro nome já foi impresso
        primeiro_nome_espera = True
        primeiro_nome_preparo = True
        primeiro_nome_entrega = True

        for i in range(7):
            if i < len(self.fila_espera):
                # Imprime o sinal de maior apenas para o primeiro nome da fila de espera
                if primeiro_nome_espera:
                    print(
                        f"> {self.fila_espera[i].nome}",
                        end=" " * (15 - len(self.fila_espera[i].nome)),
                    )
                    primeiro_nome_espera = False
                else:
                    print(
                        f"  {self.fila_espera[i].nome}",
                        end=" " * (15 - len(self.fila_espera[i].nome)),
                    )
            else:
                print(" " * 14, end=" ")

            if i < len(self.fila_preparo):
                # Imprime o sinal de maior apenas para o primeiro nome da fila de preparo
                if primeiro_nome_preparo:
                    print(
                        f"> {self.fila_preparo[i].nome}",
                        end=" " * (15 - len(self.fila_preparo[i].nome)),
                    )
                    primeiro_nome_preparo = False
                else:
                    print(
                        f"  {self.fila_preparo[i].nome}",
                        end=" " * (15 - len(self.fila_preparo[i].nome)),
                    )
            else:
                print(" " * 14, end=" ")

            if i < len(self.fila_entrega):
                # Imprime o sinal de maior apenas para o primeiro nome da fila de entrega
                if primeiro_nome_entrega:
                    print(
                        f"> {self.fila_entrega[i].nome}",
                        end=" " * (15 - len(self.fila_entrega[i].nome)),
                    )
                    primeiro_nome_entrega = False
                else:
                    print(
                        f"  {self.fila_entrega[i].nome}",
                        end=" " * (15 - len(self.fila_entrega[i].nome)),
                    )
            else:
                print(" " * 14, end=" ")

            print()
        print("=" * 14, "=" * 14, "=" * 14)

