lista =[]

while True:
    valor = int(input("digite um valor: "))
    if valor not in lista:
        lista.append(valor)
        continuar = input('deseja continuar [s/n]')
        if continuar in 'Nn':
            break

print('a lista contem',len(lista),'numeros')
lista.sort(reverse= True)
print('os valores em ormde decrescente', lista)
if 5 not in lista:
    print('o valor 5 não foi encontrado na lista')
else:
    print(' 5 esta na lista')