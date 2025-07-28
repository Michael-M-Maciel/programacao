'''ATIVIDADE PRÁTICA 2

Crie um programa que permita ao usuário cadastrar produtos.
Cada produto deve ter:
- Nome
- Preço
O programa deve permitir o cadastro de quantos produtos o usuário quiser, e ao final, exibir uma lista com todos os produtos cadastrados.
OBS:
- Cada produto deve ser armazenado como um dicionário dentro de uma lista.
- Crie duas funções obrigatórias:
a) cadastrar_produto : para adicionar um produto

b) exibir_produtos : para mostrar todos os produtos'''



def cadastro_produtos(lista):
    nome = input('nome produto: ')
    valor = float(input('valor do produto: '))
    dicionario = {
        'nome':nome,
        'valor':valor
    }
    lista.append(dicionario)

def exibir_produtod(lista):
    print('produtos cadastrados')
    for c in lista:
        print(f'{c['nome']} - {c['valor']:.2f}R$')
    
lista = []

while True:
    cadastro_produtos(lista)
    print('deseja continuar ? [sim] ou ]-[n]ão: ')
    continuar = input('responda sim ou nao: ')
    if continuar =='n':
        print('saindo')
        break

exibir_produtod(lista)