
# lista = list()
# lista_pares = list()
# lista_impares = list()


# while True:
#     lista.append(int(input('digite um numero: ')))
#     continuar = input('deseja continuar: ')
#     if continuar in 'Nn':
#         print('fim')
#         break

# for c, i in enumerate(lista):
#     if i % 2 == 0:
#         lista_pares.append(i)
#     elif i % 2 == 1:
#         lista_impares.append(i)


# print(f'lista de numeros completa = {lista}')
# print(f'lista de numeros pares = {lista_pares}')
# print(f'lista de numeros impares = {lista_impares}')
    



lista = []
lista_pares = []
lista_impares = []


while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
   
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    continuar = input('deseja continuar: ')
    if continuar in 'Nn':
        print('fim')
        break

print(f'lista de numeros completa = {lista}')
print(f'lista de numeros pares = {lista_pares}')
print(f'lista de numeros impares = {lista_impares}')
    
