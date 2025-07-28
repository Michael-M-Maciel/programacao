'''ATIVIDADE PRÁTICA 1
Dada uma lista de números, crie uma nova lista contendo
apenas os números pares.'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []

for c in lista_numeros:
    if c % 2 == 0:
        lista_pares.append(c)

print(lista_pares)

