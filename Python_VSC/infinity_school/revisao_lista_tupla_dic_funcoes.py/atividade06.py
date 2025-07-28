'''Receba uma lista de números
 e use funções agregadoras
para contar quantos valores são ímpares
 e quantos são pares.'''


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

def par_impar(lista):
    par = []
    impar = []
    for c in lista:
        if c % 2 == 0:
            par.append(c)
        
        else:
            impar.append(c)
    
    print(f'lista de números pares : {par}')
    print(f'lista de números ímpares: {impar}')
        
    
par_impar(lista_numeros)
