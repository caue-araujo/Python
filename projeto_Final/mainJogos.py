from jogo import *
from ListaDuplamenteEncadeada import *
from time import sleep
from funcoes import *

####################################                 MAIN      #######################################


lista_de_jogos = (Lista())  # Cria uma lista duplamente encadeada com o nome de 'lista_de_jogos onde será armazenado os dados do arquivo csv'
nome_do_arquivo = "computer_games.csv"  # Altere para o nome do seu arquivo CSV
dados_csv = ler_arquivo_csv(nome_do_arquivo)  # Chama a função ler_arquivo_csv para realizar a leitura do arquivo e  retornar uma lista com os dados dos arquivos por linha

   

# Inicializa um conjunto vazio para armazenar os nomes dos jogos únicos
jogos_adicionados = []

itens_carregados = 0  # cria uma variável para contar quantos itens foram adicionados
itens_descartados = 0
# Itera sobre cada linha na lista de dados
qtde = 0
for linha in dados_csv:
    # Desempacota os valores da linha (supondo que cada linha tenha seis campos)
    nome, dev, produtora, genero, sistema_op, data = linha

    tokens_genero = genero.split(", ")
    tokens_sistema_operacional = sistema_op.lower().split(", ")

    data_formatada = formatar_data_para_br(data)
    # Verifica se o jogo já foi adicionado à lista

    if data_formatada != None:
        # Cria um objeto Jogo com os valores da linha
        jogo = Jogo(nome,dev,produtora,tokens_genero,tokens_sistema_operacional,data_formatada)
        qtde += 1

        if qtde > 1:
            if nome in jogos_adicionados: # se o nome do jogo ja estiver na lista de jogos, ele descarta
                itens_descartados += 1
                continue
            else:
                # Adiciona o jogo à lista_de_jogos
                lista_de_jogos.append(jogo)
        else:
            jogos_adicionados.append(nome)
            lista_de_jogos.append(jogo)

        itens_carregados += 1
    else:
        itens_descartados += 1
        # print(f"O JOGO '{nome}' SERÁ DESCARTADO...")
        #sleep(0.1)

try:
    while True:
        try:
            exibir_painel()

            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                print("Encerrando programa... Até mais.")
                break

            elif opcao == 1:

                # Código para exibir os jogos suportados pelo sistema operacional com gênero e desenvolvedor
                sistema_operacional = input("Digite um sistema operacional: ").lower()
                jogos_suport = obter_jogos_por_sistema_operacional(sistema_operacional, lista_de_jogos)

                # Verifique se há jogos suportados antes de imprimir

                if jogos_suport:
                    print("="*90)
                    print(
                        f"Resultado (S0): {sistema_operacional.upper()}"
                    )
                    print(
                        "{:<4} {:<35} {:<25} {:<25}".format(
                            "N°", "Jogo", "Gênero", "Desenvolvedor"
                        )
                    )
                    print("=" * 90)

                    count = 1

                    for jogo_info in jogos_suport:
                        jogo, genero, desenvolvedor = jogo_info

                        # Separe o nome do jogo em linhas de tamanho máximo
                        linhas_jogo = [
                            jogo[i : i + 35] for i in range(0, len(jogo), 35)
                        ]

                        # Imprimindo cada informação em colunas
                        print(
                            f"{count:<4} {linhas_jogo[0]:<35} | {'' if not genero else genero[0]:<25} | {desenvolvedor}")
                    

                        # Se houver mais de um gênero, imprima nas linhas subsequentes
                        if len(genero) > 1:
                            for subgenero in genero[1:]:
                                print(f"{'':<4} {'':<35} | {subgenero:<25} | {'':<25}")

                        # Se o nome do jogo possuir mais de uma linha, imprima nas linhas subsequentes
                        if len(linhas_jogo) > 1:
                            for linha in linhas_jogo[1:]:
                                print(f"{'':<4} {linha:<35} | {'':<25} | {'':<25}")

                        count += 1

            elif opcao == 2:
                try:
                    tipo_de_busca = int(input("Tipo de busca: (1) Levenshtein (2) Occorrência da palavra: "))

                    if tipo_de_busca != 1 and tipo_de_busca != 2:
                        print("OPÇÃO INVÁLIDA! TENTE 1 OU 2")

                    if tipo_de_busca == 1:
                        nome = input("Jogo: ").lower()
                        jogo_pesquisado = Levenshtein(lista_de_jogos, nome)

                        if jogo_pesquisado:
                            exibir_jogos_com_genero_e_dev(jogo_pesquisado)
                        else:
                            print(f"NENHUM EXISTE NENHUM JOGO COM O NOME '{nome}'")


                    elif tipo_de_busca == 2:
                        nome = input("Jogo: ").lower()
                        jogo_pesquisado = Ocorrencia_da_palavra(lista_de_jogos, nome)

                        if jogo_pesquisado:
                            exibir_jogos_com_genero_e_dev(jogo_pesquisado)
                        else:
                            print(f"NENHUM EXISTE NENHUM JOGO COM O NOME '{nome}'")
                            
                except ValueError:
                    print("OPÇÃO INVÁLIDA! TENTE 1 OU 2")
                
                    
                    
            elif opcao == 3:
                try:
                    ano_de_lancamento = int(input("digite um ano: "))
                    jogos_ano = obter_nomes_dos_jogos_lancados_no_ano(ano_de_lancamento, lista_de_jogos)

                    if jogos_ano:
                        print("===============================")
                        print(f"JOGOS LANÇADOS NO ANO DE {ano_de_lancamento}: ")
                        print("===============================")
                        print

                        for jogos in jogos_ano:
                            print(f"-> {jogos}")
                        print()

                    else:
                        print(f"NENHUM JOGO LANÇADO NO ANO {ano_de_lancamento}")

                except ValueError:
                    print("TIPO DE DADO INVÁLIDO! DIGITE UM ANO NO FORMATO DE NÚMEROS -> 0000 <- ")
                    



            elif opcao == 4:

                sistema, qntd_jogos = obter_sistema_operacional_com_maisJogos(lista_de_jogos)
                print(f"SISTEMA OPERACIONAL COM MAIS JOGOS DISPONÍVEIS: -> {sistema} <- COM {qntd_jogos} JOGOS.")
                sleep(1)



            elif opcao == 5:
                print(f"QUANTIDADE DE ITENS CARREGADOS: {itens_carregados} ITENS.")
                sleep(1)

            elif opcao == 6:
                ano_lancamento = obter_quantidade_de_jogos_por_ano(lista_de_jogos)
                print("JOGOS LANÇADOS POR ANO DE FORMA CRESCENTE.")



                for ano, quantidade in ano_lancamento.items():
                    print(f"{ano}: {quantidade} JOGOS.")
                    sleep(0.1)


            elif opcao == 7:
                print(f"QUANTIDADE DE ITENS DESCARTADOS: {itens_descartados}")
                sleep(1)



            else:
                print("OPCAO INVÁLIDA! TENTE DE 0 A 7.")
                sleep(1)


        except ValueError:
            print("CARACTERES ESPECIAIS E LETRAS SÃO INVÁLIDOS! TENTE UM NÚMERO INTEIRO DE 0 A 7.")
            sleep(1)
            
except KeyboardInterrupt:
    print("PROGRAMA ENCERRADO PELO USUÁRIO! ATÉ MAIS...")
