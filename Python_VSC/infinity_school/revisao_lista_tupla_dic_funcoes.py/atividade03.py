'''Crie um conjunto com nomes de cores. Implemente uma
função que retorne as cores que têm mais de quatro
letras.'''


conjunto = {'azul', 'amarelo', 'verde', 'preto','vermelho', 'roxo', 'cinza'}

def listando_cores():
    for c in conjunto:
        if len(c) > 4:

            print(f'{c}', end=', ' )
     
listando_cores()