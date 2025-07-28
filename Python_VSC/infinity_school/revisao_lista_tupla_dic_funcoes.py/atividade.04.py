'''Crie uma função que receba uma lista de strings e
retorne uma nova lista contendo apenas as strings
palíndromos.'''


lista_nomes =['michael', 'ana', 'joão', ' max', 'aila', 'asa', 'isa' ]

lista_de_palindromo = []



def palindromo_lista():
    for c in lista_nomes:
        if c == c[::-1]:
            lista_de_palindromo.append(c)
    print(f'é palíndromo: = {lista_de_palindromo}')
         

palindromo_lista()