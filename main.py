# lista de compras
compras = ['Ovos', 'Macarrão', 'Feijão', 'Arroz', 'Leite', 'Chocolate']

# exibe a lista
for i in range(len(compras)):
    print(f'Índice {i}: {compras[i]}.')

# tratamento de exceção
try:
    # usuário informa o item que deseja retirar
    indice = int(input('\nÍndice do item que deseja retirar:'))

    # retira item da lista
    del(compras[indice])
    print('\nItem retirado com sucesso.\n')
except:
    print('\nNão foi possível excluir.\n')
finally:
    for i in range (len(compras)):
        print(f'Índice {i}: {compras[i]}.')