from functools import reduce

# def eh_par(numero):
#     if numero % 2 == 0:
#         return "é par"
#     return "é impar"

# print(eh_par(3))

# def apresentacao(nome, idade, cidade='desconhecida'):
#     return f'olá me chamo {nome}, tenho {idade} anos e minha cidade é muito: {cidade}'


# print(apresentacao('Jukinha', 30,))

# def contar_palavras(*args):
#     return f'foram ditas {len(args)} palavras'

# print(contar_palavras('gato', 'cachorro'))


# def mensagem_boa_vindas(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'bem vindo {chave}:{valor}, sua matricula no {chave}:{valor} foi confirmada.')
        

# impar_par = lambda x:'par' if  x % 2 == 0 else 'impar' 

# print(impar_par(3))



##map
# nome = ['sapo', 'macaco', 'burro','navio']

# maiusculo = list(map(lambda x: x.upper(), nome))
# print(maiusculo)


##filter
# numero = [-1, -8, 5, 7, 3]

# positivos = list(filter(lambda x: x > 0, numero))

# print(positivos)


## reduce
numeros = [1, 2, 3, 4]

def soma(a , b):
    return a * b

total = reduce(soma, numeros)
print(total)
