class Jogo:
    def __init__(self,nome_do_jogo,desenvolvedor,produtora,genero,sistema_op,data_de_lancamento,):
        self.nome_do_jogo = nome_do_jogo
        self.desenvolvedor = desenvolvedor
        self.produtora = produtora
        self.sistema_op = sistema_op
        self.data_de_lancamento = data_de_lancamento
        self.genero = genero
    """
    
    Cria um objeto Jogo.

    Args:
        nome: O nome do jogo.
        dev: O desenvolvedor do jogo.
        produtora: A produtora do jogo.
        genero: O gênero do jogo.
        sistema_op: O sistema operacional suportado pelo jogo.
        data: A data de lançamento do jogo.

    Returns:
        Um objeto Jogo.
        
    """

    def get_nome_do_jogo(self):
        return self.nome_do_jogo

    def get_desenvolvedor(self):
        return self.desenvolvedor

    def get_produtora(self):
        return self.produtora

    def get_genero(self):
        return self.genero

    def get_sistema_operacional(self):
        return self.sistema_op

    def get_data_de_lancamento(self):
        return self.data_de_lancamento
