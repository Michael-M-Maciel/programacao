'''ATIVIDADE PRÁTICA 1
Dada uma lista de números, crie uma nova lista contendo
apenas os números pares.'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# for c in lista_numeros:
#     if c % 2 == 0:
#         lista_pares.append(c)

# print(lista_pares)

lista_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
lista_impares = list(filter(lambda x: x % 2 == 1, lista_numeros))
print(lista_pares)
print(lista_impares)