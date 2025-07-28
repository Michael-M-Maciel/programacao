lista = ['michael', 'zé', 'max', 'joao']

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)
# print(next(lista_enumerada))

lista_enumerada = enumerate(lista)

for nome in lista_enumerada:
    print(nome)

# for nome in enumerate(lista):
#     print(nome)

# lista = list(enumerate(lista))
# print(lista)

# for item in lista_enumerada:
#     indice, nome = item
#     print(item)

# for indice, nome in lista_enumerada:
#     print(indice, nome)