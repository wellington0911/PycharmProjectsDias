listadeProdutos = []  # Aqui vai ficar minha lista de Produtos


# -------------------- INICIO Cadastrar Produto --------------------

def cadastrarProduto(cp):  # Função para cadastrar os Produtos
    print('Bem vindo ao CADASTRO de Produtos')  # Bem-vindo
    print('O Código do Produto a ser cadastrado é: {}'.format(
        cp))  # fiz um contador e coloquei como cp. para gerar códigos
    nome = input('Digite o Nome do Produto: ')  # Cadastro do produto
    fabricante = input('Digite o Fabricante do Produto: ')  # Cadastro do Fabricante
    valor = float(input('Digite o Valor (R$) do Produto: '))  # Cadastro do valor do produto
    dicionarioProduto = {'cp': cp,
                         'nome': nome,
                         'fabricante': fabricante,  # DICIONÁRIO
                         'valor': valor}
    listadeProdutos.append(dicionarioProduto.copy())  # Cópia do discionário dentro da lista


# -------------------- FIM Cadastrar Produto ------------------------

# -------------------- INICIO Consultar Produto ---------------------

def consultarProduto():  # Consulta de Produtos
    while True:  # Laço de repetição caso o usuario digite algo errado
        try:  ## try dentro do Laço de repetição caso o usuario digite algo errado
            print('Bem vindo a CONSULTA de produtos')
            opcaoConsultar = int(input('Escolha a opção desejada:\n'
                                       '1 - Consultar Todos os Produtos\n'
                                       '2 - Consultar Produtos por Códigos\n'  # Menu para consultas 
                                       '3 - Consultar Produtos por Fabricante\n'
                                       '4 - Retornar'
                                       '\n>>'))
            if (opcaoConsultar == 1):
                print('Bem-vindo ao Consultar TODOS')  # Consulta de todos os produtos
                for produto in listadeProdutos:  # Selecionar cada dicionário da minha lista (cada produto da lista)
                    for key, value in produto.items():  # selecionar cada conjunto chave/valor do dicionário
                        print('{} : {}'.format(key, value))  # print na tela
            elif (opcaoConsultar == 2):
                print('Bem-vindo ao Consultar por Código')
                entrada = int(input('Digite o Código desejado: '))  # Usuario digitando o código desejado
                for produto in listadeProdutos:  # Selecionar cada dicionário da minha lista (cada produto da lista)
                    if (produto['cp'] == entrada):  # if verificando se o codigo é igual a entrada
                        for key, value in produto.items():  # selecionar cada conjunto chave/valor do dicionário
                            print('{} : {}'.format(key, value))  # print na tela
            elif (opcaoConsultar == 3):
                print('Bem-vindo ao Consultar por Fabricante')
                entrada = input('Digite o Fabricante desejado: ')  # Usuario digitando o fabricante desejado
                for produto in listadeProdutos:  # Selecionar cada dicionário da minha lista (cada produto da lista)
                    if (produto['fabricante'] == entrada):  # if verificando se o fabricante é igual a entrada
                        for key, value in produto.items():  # selecionar cada conjunto chave/valor do dicionário
                            print('{} : {}'.format(key, value))  # Print na tela
            elif (opcaoConsultar == 4):  # Retornar ao menu principal
                return
            else:
                print('Não temos essa opção no menu')  # caso o usuario digite algum vaor diferente

        except ValueError:
            print(
                'Essa opção não tem no menu. Digite um NÚMERO INTEIRO!')  # caso o usuario digite algum vaor diferente


# -------------------- FIM Consultar Produto ------------------------

# -------------------- INICIO Remover Produto -----------------------

def removerProduto():
    print('Bem vindo ao REMOVER produto')
    entrada = int(input('Digite o Código do Produto que deseja Remover: '))  # Usuario digitando o código desejado
    for produto in listadeProdutos:  # Selecionar cada dicionário da minha lista (cada produto da lista)
        if (produto['cp'] == entrada):  # if verificando se o codigo é igual a entrada
            listadeProdutos.remove(produto)  # Removendo o produto
            print('Produto removido!')

        # -------------------- FIM Remover Produto --------------------------


# -------------------- INICIO Programa Principal --------------------
print('Bem vindo ao Controle de Estoque da Mercearia do Wellington Camargo Dias')  # Bem-vido
codigoProduto = 0  # Contador
while True:  # Laço para repetição do menu
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1 - Cadastrar Produto\n'
                          '2 - Consultar Produtos\n'  # Menu 
                          '3 - Remover Produto\n'
                          '4 - Sair'
                          '\n>>'))
        if (opcao == 1):
            codigoProduto = codigoProduto + 1  # Caso o usuario escolha a opção 1 o programa vai fazer a contagem e ir para cadastro
            cadastrarProduto(codigoProduto)
        elif (
                opcao == 2):  # Caso o usuario escolha a opção 2 o programa vai fazer a consulta e ir para as opções de consulta
            consultarProduto()
        elif (
                opcao == 3):  # Caso o usuario escolha a opção 3 o programa vai nas opções de remover e ir para as opções de consulta
            removerProduto()
        elif (opcao == 4):
            print('Finalizando o Programa!')  # Caso digite a opção 4 irá sair do programa
            break
        else:
            print('Não temos essa opção no menu')  # caso o usuario digite algum vaor diferente
            continue
    except ValueError:
        print('Essa opção não tem no menu. Digite um NÚMERO INTEIRO!')  # caso o usuario digite algum valor diferente
# -------------------- FIM Programa Principal -----------------------