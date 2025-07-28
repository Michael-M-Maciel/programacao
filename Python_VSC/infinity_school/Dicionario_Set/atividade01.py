# frutas = {'banana', 'uva', 'laranja', 'morango'}
# print(frutas)

# print('banana'in frutas)
# print('manga' in frutas)

# frutas_vermelhas = {'morango', 'cereja', 'framboesa'}
# frutas_vermelhas.remove('cereja') #discard tb 
# print(frutas_vermelhas)

# conjunto_a = {10, 20, 30}
# conjunto_b = {30, 40, 50, 60, 70}

#print(conjunto_a.union(conjunto_b))
# print(conjunto_a.intersection_update(conjunto_b))
# print(conjunto_a)
# uniao_dos_conjuntos = conjunto_a | conjunto_b
# print(uniao_dos_conjuntos)
# soma_conjutos = sum(uniao_dos_conjuntos)
# print(soma_conjutos)

# conjunto = set()

# conjunto.add

# praticando

#ex01:

# frutas = set()
# frutas.add('banana')
# frutas.add('maçã')
# frutas.add('uva')
# frutas.add('laranja')
# frutas.add('morango')
# print(frutas)

#usando for

# frutas = set()

# for c in range(5):
#     fruta = input('digite 5 frutas: ')
#     frutas.add(fruta)
# print(frutas)

#02:

# frutas = {'banana', 'manga', 'jaca', 'limão'}
# print('banana' in frutas)

#ex03:

# frutas_vermelhas = {'morango', 'cereja', 'framboesa'}
# print(frutas_vermelhas)


#ex04:

# frutas_vermelhas = {'morango', 'cereja', 'framboesa'}
# frutas_vermelhas.discard('cereja')
# frutas_vermelhas.remove('cereja')
# print(frutas_vermelhas)

#ex05:

# conjunto_a = {1, 2, 3, 4}
# conjunto_b = {2, 3, 4, 5, 6, 7}

# print(conjunto_a | conjunto_b) # união dos conjuntos

#ex06:

# conjunto_a = {1, 2, 3, 4}
# conjunto_b = {2, 3, 4, 5, 6, 7}

# print(conjunto_a.intersection (conjunto_b))

#ex07

# lista_a = [10, 20, 30] #crias as listas
# lista_b = [40, 50, 60]

# conjunto_a = set(lista_a) # converte para conjunto
# conjunto_b = set(lista_b)

# uniao = print(conjunto_a | conjunto_b) #união dos sets


#ex08:

# pessoa = {'Nome: Michael',
#           'Idade: 37'
#           }

# print(pessoa)


#ex09:

# dic = {'Nome' : 'Michael',
#        'Idade': 37, 
#        'Cidade': 'Maceio'       
#        }

# # print(dic)

# for c in dic.items():
#     print(c)

# for chave, valor in dic.items():  
#     print(f'{chave}, {valor}')

#ex10:
#adicionando chave e valor no dicionario

# dicionario = { 'ana': 'ana@email.com',
#     'carlos': 'carlos@email.com',
#     'beatriz': 'bia@email.com'
#               }

# chave = input('digite valor para chave: ')
# valor = input('digite o valor: ')

# dicionario[chave] = valor

# print(dicionario)

#ex11:

