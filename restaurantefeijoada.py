# ------------------------------INICIO VOLUME FEIJOADA----------------------------------------------
def volumeFeijoada():  # FUNÇÃO PARA CALCULAR O VOLUME DA FEIJOADA
    while True:
        try:
            print('Menu Volume Feijoada')
            volumeF = int(input('Entre com a quantidade desejada(ml): '))  # ENTRANDO COM O VOLUME
            if (volumeF >= 300) and (volumeF <= 5000):  # VOLUME DEVE SER MAIOR QUE 300ML E MENOR QUE 5000ML
                volumeF = volumeF * 0.08  # MULTIPLICADO PELO VALOR DO VOLUME
                return volumeF
            else:
                print(
                    'Não aceitamos porções menores que 300ml ou maiores que 5l. Tente novamente!')  # CASO DIGITE OPÇÃO DIFERENTE DO QUE FOI INFORMADO
                continue
        except ValueError:
            print('Opção inválida. Tente novamente!')  # CASO DIGITE OPÇÃO INVALIDA
            continue

        # ------------------------------FIM VOLUME FEIJOADA--------------------------------------------------


# ------------------------------INICIO OPÇÃO FEIJOADA------------------------------------------------

def opcaoFeijoada():  # FUNÇÃO PARA ESCOLHA DAS OPÇÕES DE FEIJOADA
    while True:

        print('Menu Opção Feijoada')
        print('Entre com a opção da Feijoada:')
        print('b - Básica = |Feijão | Paiol | Costelinha |')  # MENU
        print('p - Premium = |Feijão | Paiol | Costelinha | Partes de porco |')
        print('s - Suprema = |Feijão | Paiol | Costelinha | Partes de porco | Charque | Calabresa | Bacon |')
        y = input('>>')

        if (y == 'b'):  # SE ESCOLHER A BASICA RECEBE O VALOR
            y = 1.00
            return y
        elif (y == 'p'):  # SE ESCOLHER A PREMIUM RECEBE O VALOR
            y = 1.25
            return y
        elif (y == 's'):  # SE ESCOLHER A SUPREMA RECEBE O VALOR
            y = 1.50
            return y
        else:
            print('Você não digitou uma opção válida!')  # CASO DIGITE ALGUM VALOR INVALIDO
            continue

        # ------------------------------FIM OPÇÃO FEIJOADA---------------------------------------------------


# ------------------------------INICIO ACOMPANHAMENTO FEIJOADA---------------------------------------

def acompanhamentoFeijoada():  # FUNÇÃO PARA ACOMPANHAMENTO DE FEIJOADA
    while True:
        try:
            global acumulador  # PRECISEI DE UM CONTADOR POIS O MENU SE REPETE
            print('Deseja mais algum acompanhamento: ')
            opcoes = int(input('0 - Não desejo mais acompanhamento (encerrar pedido)\n'
                               '1 - 200g de arroz\n'  # MENU 
                               '2 - 150g de farofa especial\n'
                               '3 - 100g de couve cozida\n'
                               '4 - 1 laranja descascada'
                               '\n>>'))

            if (opcoes == 0):  # CASO ESCOLHA 0 ENCERRA O PEDIDO
                print('Encerrando pedido...')
                return

            elif (opcoes == 1):  # CASO ESCOLHA OPÇÃO 1 RECEBE O VALOR DO ITEM
                acumulador = acumulador + 5.00

            elif (opcoes == 2):  # CASO ESCOLHA OPÇÃO 2 RECEBE O VALOR DO ITEM
                acumulador = acumulador + 6.00

            elif (opcoes == 3):  # CASO ESCOLHA OPÇÃO 3 RECEBE O VALOR DO ITEM
                acumulador = acumulador + 7.00

            elif (opcoes == 4):  # CASO ESCOLHA OPÇÃO 4 RECEBE O VALOR DO ITEM
                acumulador = acumulador + 3.00

            else:
                print('Opção inválida')  # CASO DIGITE ALGUM VALOR INVALIDO
                continue

        except ValueError:
            print('Não existe essa opção. DIGITE NUMEROS INTEIRO DE 1 A 4')  # CASO DIGITE OPÇÃO INVALIDA
            continue

        # ------------------------------FIM ACOMPANHAMENTO FEIJOADA-------------------------------------


# ------------------------------Programa Principal----------------------------------------------
acumulador = 0  # PRECISEI PARA SOMAR AS OPÇÕES ACOMPANHAMENTO
print('Bem vindo ao programa de Feijoada do Wellington Camargo Dias')
op = volumeFeijoada()  # FUNÇÃO VOLUME EXECUTA PRIMEIRO
op1 = opcaoFeijoada()  # FUNÇÃO DE OPÇÃO EXECUTA POR SEGUNDO
op2 = acompanhamentoFeijoada()  # FUNÇÃO ACOMPANHAMENTO POR TERCEIRO
total = op * op1 + acumulador  # VALOR QUE A EMPRESA COBRA É ESSA EQUAÇÃO
print('O valor a ser pago é (R$): {} (volume = {} * opção = {} + Acompanhamento = {}'.format(total, op, op1,
                                                                                             acumulador))  # PRINT DO VALOR QUE O CLIENTE DEVERÁ PAGAR
print('Finalizando o programa!')