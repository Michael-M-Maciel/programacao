'''[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados.
   Cada dado deve gerar um número aleatório entre 1 e 6.
   A função deve somar os resultados desses dois lançamentos e retornar o valor total.'''
from random import randint

def lancar_dados():
    dados_um = randint(1, 6)
    dados_dois = randint(1, 6)    
    print(f'dados_um = {dados_um} e dados_dois= {dados_dois}, a soma dos dois dados é: {dados_um + dados_dois}')


lancar_dados()

