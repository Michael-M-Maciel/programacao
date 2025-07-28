'''PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos.
 Esta função deve comparar os três números e identificar qual deles é o maior. Para isso,
 utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.'''


def maio_numero(a, b, c):
    maio_numero = None
    if a >= b and a >= c: # caso ''a'' seja igual b ou c , como a recebeu o valor primeiro, o valor de ''a'' será considerado o maior nesse caso
       maio_numero = a
       return f'o maior numero foi "a" {maio_numero}'
    elif b >= a and b >= c: # caso ''b'' seja igual c , como a recebeu o valor primeiro, o valor de ''b'' será considerado o maior nesse caso
       maio_numero = b
       return f'o maior numero foi "b" {maio_numero}'
    else:
        maio_numero = c
        return f'o maior numero foi "c" {maio_numero}'
    

print(maio_numero(10, 1 , 10))
