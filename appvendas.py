# Boas vindas
print('Bem Vindo a Loja do Wellington Camargo Dias Atacado')
# Valor do produto
pdt = float(input('Entre com o valor do produto? '))
# Quantidade do produto
qtd = int(input('Entre com o valor da quantidade? '))

# --------------------------------------------Descontos--------------------------------------------#

# Até 4 sem desconto
if (qtd <= 4):
    # Desconto 0
    des0 = pdt * qtd
    # mensagem
    print('Total da compra: {}'.format(des0))

# Entre 5 e 19 3%
elif (qtd >= 5) and (qtd <= 19):
    # Sem desconto
    des0 = pdt * qtd
    # Desconto 3%
    des3 = des0 * (3 / 100)
    # Mensagem  final
    print('Parabéns você ganhou 3% de desconto.')
    print('Total sem desconto: {}'.format(des0))
    print('Total com desconto: {}'.format(des0 - des3))

# Entre 20 e 99 6%
elif (qtd >= 20) and (qtd <= 99):
    # Sem desconto
    des0 = pdt * qtd
    # Desconto 6%
    des6 = des0 * (6 / 100)
    # Mensagem  final
    print('Parabéns você ganhou 6% de desconto.')
    print('Total sem desconto: {}'.format(des0))
    print('Total com desconto: {}'.format(des0 - des6))

# Maior ou igual a 100 10%
elif (qtd >= 100):
    # Sem desconto
    des0 = pdt * qtd
    # Desconto 10%
    des10 = des0 * (10 / 100)
    # Mensagem  final
    print('Parabéns você ganhou 10% de desconto.')
    print('Total sem desconto: {}'.format(des0))
    print('Total com desconto: {}'.format(des0 - des10))

# --------------------------------------------Caso valor esteja incorreto--------------------------------------------#

else:
    print('Valor incorreto!')

    print('Encerrando programa!')