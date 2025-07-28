'''Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números.
Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.'''

def media(a, b, c):
    return f'a media das notas é = {(a + b + c) / 3:.2f}'

print(media(7,10,5))