'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''



lista = []

while True:
    print( 50 * '*')
    numeros = int(input('digite um valor: '))
    
    if numeros not in lista:
        print('numero adicionado com sucessoo...')
        lista.append(numeros)
    else:
        print('numero repetido, ja contem na lista, tente outro')
        
    continuar = input('deseja continuar [s/n]: ')
    if continuar in 'Nn':
        break
    
               
print(50 * '*')      
print('voçê digitou o valores,',sorted(lista)) # sorted() deixa em ordem crescente

        
        

    