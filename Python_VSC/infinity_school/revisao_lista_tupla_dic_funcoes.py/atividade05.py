# '''Dado um dicionário que representa as vendas de
# produtos, encontre o produto mais vendido (ou os
# produtos mais vendidos, se houver um empate).'''

produtos_vendidos = [
    {'nome': 'pc', 'numero de vendas': 10},
    {'nome': 'xbox', 'numero de vendas': 35},
    {'nome': 'ps5', 'numero de vendas': 35},
    {'nome': 'iphone 15', 'numero de vendas':20}
]


def achando_maior_venda():
   mais_vendido = 0
   lista_mais_vendidos = []

   for maior in produtos_vendidos:
      if maior['numero de vendas'] > mais_vendido:
        mais_vendido = maior['numero de vendas']

   for igual in produtos_vendidos:
      if igual['numero de vendas'] == mais_vendido:
        lista_mais_vendidos.append(igual)


   if len(lista_mais_vendidos)> 1:
    print(f'tivemos um empate entre os mais vendidos: \n{lista_mais_vendidos[0]} \n{lista_mais_vendidos[1]}')

   else:
     vencedor = lista_mais_vendidos[0]
     print(f'produto mais vendido foi: {vencedor['nome']} com {vencedor['numero de vendas']} vendas ')

    
  
achando_maior_venda()


