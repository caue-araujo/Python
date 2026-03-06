from ListaDuplamenteEncadeada import *
from jogo import *
from time import sleep
import csv
import re
import datetime

"""


 Arquivo criado para se comportar como uma biblioteca de funções para que o 

desenvolvedor consiga manipular os dados do arquivo csv e modificá-los.



 """


def ler_arquivo_csv(nome_arquivo) -> list:
    """
    Função para ler um arquivo CSV e corrigir campos com múltiplas vírgulas.

    Argumentos:
    nome_arquivo: O caminho do arquivo CSV a ser lido.

    Retorna:
    Uma lista onde cada elemento é uma lista representando uma linha do arquivo CSV.
    """
    linhas_corrigidas = (
        []
    )  # Inicializa uma lista vazia para armazenar as linhas corrigidas do CSV
    with open(nome_arquivo, newline="") as csvfile:  # Abre o arquivo CSV
        leitor_csv = csv.reader(csvfile)  # Cria um leitor CSV
        next(leitor_csv)  # Pula a primeira linha
        for linha in leitor_csv:  # Itera sobre cada linha do arquivo CSV
            linha_corrigida = (
                []
            )  # Inicializa uma lista para armazenar a linha corrigida
            for campo in linha:  # Itera sobre cada campo da linha
                campo_corrigido = re.sub(",", ",", campo)
                linha_corrigida.append(campo_corrigido)
            linhas_corrigidas.append(
                linha_corrigida
            )  # Adiciona a linha corrigida à lista 'linhas_corrigidas'
    
    return linhas_corrigidas  # Retorna a lista contendo as linhas do arquivo CSV, exceto a primeira


def exibir_painel() -> str:
    """
    Função para exibir um Menu mostrando as opções a serem escolhidas pelo usuário.

    """
    print("============= Menu Principal ==============")
    print("(1) Listar Jogos por sistema operacional")
    print("(2) Pesquisar jogo")
    print("(3) Listar Jogos por ano de lançamento")
    print("(4) Listar O Sistema Operacional com mais jogos disponíveis")
    print("(5) Listar Quantidade de itens carregados")
    print("(6) Listar Quantidade de jogos lançados por ano")
    print("(7) Listar Quantidade de itens descartados")
    print("(0) Sair")


def obter_sistema_operacional_com_maisJogos(lista_de_jogos) -> (str, int):
    """
    Função para identificar o sistema operacional mais popular entre os jogos.

    Argumentos:
        lista_de_jogos: Lista de objetos do tipo Jogo.

    Retorna:
        Uma tupla com o sistema operacional mais popular e a quantidade de jogos.
    """

    # Passo 1: Inicializar um dicionário para contar a quantidade de cada sistema operacional
    sistemas_operacionais = {}

    # Passo 2: Contar a ocorrência de cada sistema operacional em todos os jogos
    for jogo in lista_de_jogos:
        # Itera sobre cada sistema operacional do jogo
        for sistema_operacional in jogo.sistema_op:
            # Remove o espaço em branco do início e do fim do sistema operacional
            sistema_operacional = sistema_operacional.strip()

            # Se o sistema operacional for "windows", substitui por "microsoft windows"
            if sistema_operacional == "windows":
                sistema_operacional = "microsoft windows"

            # Verifica se o sistema operacional já está no dicionário, se não estiver, adiciona com contagem zero
            if sistema_operacional not in sistemas_operacionais:
                sistemas_operacionais[sistema_operacional] = 0
            # Incrementa a contagem de ocorrências do sistema operacional
            sistemas_operacionais[sistema_operacional] += 1

    # Passo 3: Identificar o sistema operacional com a maior quantidade de jogos
    sistema_operacional_mais_popular = None
    maior_quantidade_de_jogos = 0

    for sistema_operacional, quantidade_de_jogos in sistemas_operacionais.items():
        # Verifica se a quantidade de jogos desse sistema operacional é maior que a maior quantidade registrada até o momento
        if quantidade_de_jogos > maior_quantidade_de_jogos:
            maior_quantidade_de_jogos = quantidade_de_jogos
            sistema_operacional_mais_popular = sistema_operacional

    # Retorna o sistema operacional mais popular e a quantidade de jogos
    return sistema_operacional_mais_popular.upper(), maior_quantidade_de_jogos


def formatar_data_para_br(data):
    """
    Formata uma data no formato americano para o formato brasileiro.

    Args:
      date: A data a ser formatada.

    Returns:
      A data formatada no formato brasileiro.
    """

    # Converte a data para o formato datetime.
    try:
        dt = datetime.datetime.strptime(data, "%B %d, %Y")
    except ValueError:
        return None

    # Troca a ordem dos elementos da data.
    return dt.strftime("%d/%m/%Y")

def obter_quantidade_de_jogos_por_ano(lista_de_jogos) -> dict:
    """
    Função para exibir quantos jogos foram lançados em cada ano, por ordem decrescente de ano.

    Argumentos:
        lista_de_jogos: Lista de objetos do tipo Jogo.

    Retorna:
        Um dicionário com o ano e a quantidade de jogos lançados.
    """

    # Cria um dicionário para armazenar a quantidade de jogos por ano
    quantidade_de_jogos_por_ano = {}

    for jogo in lista_de_jogos:
        jogo_data_de_lancamento = datetime.datetime.strptime(jogo.data_de_lancamento, "%d/%m/%Y")
        ano_de_lancamento = jogo_data_de_lancamento.year

        # Obtém o ano de lançamento do jogo
        ano_de_lancamento = jogo_data_de_lancamento.year

        # Verifica se o ano já existe no dicionário
        if ano_de_lancamento not in quantidade_de_jogos_por_ano:
            quantidade_de_jogos_por_ano[ano_de_lancamento] = 0

        # Incrementa a quantidade de jogos para o ano
        quantidade_de_jogos_por_ano[ano_de_lancamento] += 1

    # Ordena o dicionário em ordem decrescente de ano
    quantidade_de_jogos_por_ano = dict(
        sorted(quantidade_de_jogos_por_ano.items(), key=lambda x: x[0], reverse=False)
    )

    return quantidade_de_jogos_por_ano

def obter_jogos_por_sistema_operacional(sistema_operacional, lista_de_jogos) -> list:
    """
    Função para exibir os jogos suportados por um sistema operacional.

    Argumentos:
        sistema_operacional: Sistema operacional em str.
        lista_de_jogos: Lista de objetos do tipo Jogo.

    Retorna:
        Uma lista de tuplas contendo informações de jogo, gênero e desenvolvedor.
    """
    # Cria uma lista para armazenar os jogos com informações adicionais
    jogos_suportados = []

    if sistema_operacional.lower() in ['windows', 'microsoft windows']:
        for jogo in lista_de_jogos:
            if 'microsoft windows' in jogo.sistema_op or 'windows' in jogo.sistema_op:
                jogos_suportados.append((jogo.nome_do_jogo, jogo.genero, jogo.desenvolvedor))
    else:
        for jogo in lista_de_jogos:
            if sistema_operacional in jogo.sistema_op:
                jogos_suportados.append((jogo.nome_do_jogo, jogo.genero, jogo.desenvolvedor))

    # Verifica se a lista de jogos está vazia
    if not jogos_suportados:
        # Imprime uma mensagem de erro
        print(f"Não há jogos compatíveis com o sistema operacional {sistema_operacional}.")

    return jogos_suportados




        
def obter_nomes_dos_jogos_lancados_no_ano(ano_passado, lista_de_jogos) -> list[str]:
    """
    Função para obter os nomes dos jogos lançados no ano passado pelo usuário

    Argumentos:
        ano_passado: Ano passado pelo usuário.
        lista_de_jogos: Lista de objetos do tipo Jogo.

    Retorna:
        Uma lista com os nomes dos jogos lançados no ano passado pelo usuário.
    """

    # Cria uma lista para armazenar os nomes dos jogos lançados no ano passado
    nomes_dos_jogos_lancados = []

    for jogo in lista_de_jogos:
        # Obtém o ano da data de lançamento do jogo
        ano_de_lancamento = jogo.data_de_lancamento[6:]

        # Verifica se o ano do jogo é igual ao ano passado
        if int(ano_de_lancamento) == ano_passado:
            # Adiciona o nome do jogo à lista
            nomes_dos_jogos_lancados.append(jogo.nome_do_jogo)

    return nomes_dos_jogos_lancados



def Ocorrencia_da_palavra(lista_de_jogos, nome_do_jogo)-> list[object]:
    '''
    Função para comparar nome de um jogo passado como argumento com os jogos da lista duplamente encadeada
    usando o algoritmo de Levenshtein, usando como base o limiar(quantidade de caracteres do nome passado pelo usuário)

    Argumentos:
        nome_do_jogo: nome do jogo passado pelo usuário
        lista_de_jogo: lista de objetos do tipo Jogo
    Retorna:
       Uma lista de objetos



    ''' 
    
    limiar = len(nome_do_jogo) # limiar será igual a quantiade de caracteres que o usuário passar
    jogos_encontrados = [] # lista para armazenar os objetos da lista encadeada, so ira armazenar se o noime do jogo passado pelo usuario for igual ao jogo da lista encadeada, até o caractere limiar
    for jogo in lista_de_jogos: # iterar sobre a lista - jogo ira passar por cada objeto da lista_de_jogos
        if nome_do_jogo[:limiar] == jogo.nome_do_jogo[:limiar].lower(): # comparando até um certo caractere do nome do jogo
            jogos_encontrados.append(jogo) # aadicionado o jogo se os caracteres forem iguais
    return jogos_encontrados # retornando a lista com os objetos armazenados



def Levenshtein(lista_de_jogos, nome_do_jogo, limiar=3)-> list[object]:
    '''
    Função para comparar nome de um jogo passado como argumento com os jogos da lista duplamente encadeada
    usando o algoritmo de Levenshtein, usando como base o limiar(quantidade de caracteres passado pelo usuário no argumento: limiar)

    Argumentos:
        nome_do_jogo: nome do jogo passado pelo usuário
        lista_de_jogo: lista de objetos do tipo Jogo
        limiar =  será igual a quantidade de caracteres que o usuário passar para realizar a comparação dos nomes

    Retorna:
       Uma lista de objetos



    ''' 
    
    jogos_encontrados = [] # lista para armazenar os objetos da lista encadeada, so ira armazenar se o noime do jogo passado pelo usuario for igual ao jogo da lista encadeada, até o caractere limiar
    for jogo in lista_de_jogos: # iterar sobre a lista - jogo ira passar por cada objeto da lista_de_jogos
        if nome_do_jogo[:limiar] == jogo.nome_do_jogo[:limiar].lower(): # comparando até um certo caractere do nome do jogo
            jogos_encontrados.append(jogo) # aadicionado o jogo se os caracteres forem iguais
    return jogos_encontrados # retornando a lista com os objetos armazenados


def exibir_jogos_com_genero_e_dev(listaDeJogos):
    if listaDeJogos:
        print("=" * 90)
        print(
            "{:<4} {:<35} {:<25} {:<25}".format("N°", "Jogo", "Gênero", "Desenvolvedor")
        )
        print("=" * 90)

        count = 1

        for jogo_info in listaDeJogos:
            jogo = jogo_info.nome_do_jogo
            genero = jogo_info.genero
            desenvolvedor = jogo_info.desenvolvedor

            # Separe o nome do jogo em linhas de tamanho máximo
            linhas_jogo = [jogo[i : i + 35] for i in range(0, len(jogo), 35)]

            # Imprimindo cada informação em colunas
            print(
                f"{count:<4} {linhas_jogo[0]:<35} | {genero[0]:<25} | {desenvolvedor}"
            )
            sleep(0.01)

            # Se houver mais de um gênero, imprima nas linhas subsequentes
            if len(genero) > 1:
                for subgenero in genero[1:]:
                    print(f"{'':<4} {'':<35} | {subgenero:<25} | {'':<25}")

                # Se o nome do jogo possuir mais de uma linha, imprima nas linhas subsequentes
                if len(linhas_jogo) > 1:
                    for linha in linhas_jogo[1:]:
                        print(f"{'':<4} {linha:<35} | {'':<25} | {'':<25}")

            count += 1
    else:
        print("NÃO HÁ JOGO(s) A SEREM EXIBIDO(s)")

