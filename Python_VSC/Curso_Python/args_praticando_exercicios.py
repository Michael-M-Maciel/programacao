# def somar(*argrs):
#     return sum(argrs)

# print(somar(5, 10, 15))

# def mostrar_nomes(*args):
#     for c in args:
#         print(c)

# todos_nomes = mostrar_nomes('micahel', 'aline', 'ari', 'zé')



# def maior_valor(*numeros):
#     return max(numeros)

# print(maior_valor(1, 3, 8, 4))

# def quantos_arguentos(*valores):
#     return len(valores)

# print(quantos_arguentos(20, 8, 5),'valores')

# def multiplicar(*args):
#     controlador = 1
#     for c in args:
#         controlador *= c
#     return controlador

# print(multiplicar(1, 2, 3, 4, 5))
# print(multiplicar(1 * 2 * 3 * 4 * 5))

# def juntar_palavras(*palava):
#     return ' '.join(palava)

# print(juntar_palavras('michael', 'é', 'legal'))

# def soma_pares(*numero):
#     soma = 0
#     for c in numero:
#         if c % 2 == 0:
#             soma += c
#     return soma

# print(soma_pares(1, 2, 3, 4, 5, 6))

# def contar_nomes_grandes(*nomes):
#     contador = 0
#     nomes_grandes =[]
#     for c in nomes:
#         if len(c.strip()) >= 5:
#             contador += 1
#             nomes_grandes.append(c.strip())
#     return f'{contador} nomes tem mais de 5 letras,{nomes_grandes}'

# print(contar_nomes_grandes('michael', 'max', 'francisco'))
      

# def maiuculas(*nomes):
#     for c in nomes:
#         print(c.upper())
    
# maiuculas('michael', 'é','amigo')

# def media_total(*valores):
#     return sum(valores) / 3

# print(media_total(5, 10, 15))

# def tem_negativos_valores(*valores):
#     for c in valores:
#         if c < 0:
#            return True
#     return False
      
    
# print(tem_negativos_valores(5, 3, -2, 7))
# print(tem_negativos_valores(5, 3, 2, 7))
# print(tem_negativos_valores(1, 2, 3))


def juntar(*palavras):
    return '-'.join(palavras)
    
print(juntar('banana', 'abacaxi', 'melancia'))