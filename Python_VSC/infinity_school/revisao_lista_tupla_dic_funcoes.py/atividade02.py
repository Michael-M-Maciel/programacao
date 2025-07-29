'''Crie um dicionário com informações de produtos,
incluindo nome, preço e quantidade em estoque.
Implemente funções para adicionar, remover e atualizar
produtos no dicionário.'''

lista_produtos = []


dicionario_de_produtos = {
    'id': 1,
    'nome':'pc',
    'preço': 5000,
    'estoque':10
}
lista_produtos.append(dicionario_de_produtos)



def listar(lista_produtos):
    for c in lista_produtos:
        print(c)




def adicionar(produtos):
    nome = input('nome do produto: ')
    preco = float(input('preço do produto: '))
    estoque = int(input('numero em estoque: '))
    id = len(lista_produtos)+1

    new_dicionario = {
        'id': id,
        'nome': nome,
        'preço': preco,
        'estoque': estoque
    }
    lista_produtos.append(new_dicionario)


def removendo(lista):
    for remover in lista_produtos:



while True:
    opcao = input('1-adicionar, 2-listar: ')
    if opcao =='1':
        adicionar(lista_produtos)

    elif opcao =='2':
        id_produto = input
        listar(lista_produtos)




























# lista_produtos.append(dicionario_de_produtos)

# def adicionando_no_dicionario():
#     nome = input('nome do produto: ')
#     preco = float(input('valor do produto: '))
#     estoque = float(input('quantidade em estoque: '))

#     novo_dicionario = {
#         'nome': nome,
#         'preço': preco,
#         'estoque': estoque
#     }
#     lista_produtos.append(novo_dicionario)

#     print(f'produtos adicionados: nome: {nome} | preço: {preco}| estoque: {estoque}')

#     for c in lista_produtos:
#         print(c)

# def remover_produto():
#     produtro_encotrado = False

#     nome_remover =  input('qual produto deseja remover: ')

#     for c in lista_produtos:
#         if nome_remover == c['nome']:
#             produtro_encotrado = True   
#             lista_produtos.remove(c)
#             break
    
#     if not produtro_encotrado:
#         print('produto não encontrado')


# def atualizar_lista():
#     nome_atualizar = input('qual o nome do produto para atualizar: ')
#     achou = None

#     for c in lista_produtos:
#         if nome_atualizar == c['nome']:
#             achou = c
#             break

#     if achou:
#         att_preco = float(input(f'novo preço para atualizar: preço de: {achou['preço']}, por:  '))
#         att_estoque = float(input(f'novo estoque para atualizar: estoque: {achou['estoque']}, por: '))

#         achou['preço'] = att_preco
#         achou['estoque'] = att_estoque

#         print(f'atualizado com sucesso: {achou} ')

#     else:
#         print('produto não se encontra no sistema')




# def listar():
#     if len(lista_produtos) > 0:
#         for c in lista_produtos:
#             print(c)
#     else:
#         print('lista vazia no momento')





# while True:
#     print(40 * '-=')
#     menu = input('1- adicionar produtos, 2- remover, 3-atualizar 4-listar 5- sair: ')

#     if menu =='5':
#         print('fim')
#         break

#     elif menu =='1':
#         adicionando_no_dicionario()

#     elif menu =='2':
#         remover_produto()

#     elif menu =='3':
#         atualizar_lista()

#     elif menu == '4':
#         listar()


       




