# def dizer_oi():
#     print('oi, tudo bem ?')


# def dizer_nome(nome): # passando um parâmetro
#     print(f'oi {nome}, tudo bem ?')

# dizer_oi()
# dizer_nome('michael')

# def numeros():
#     cont = 0
#     for c in range(1,6):
#         cont += 1
#         print(cont, end=' ')

# numeros()

# def valor_de_pi(num):
#     print(f'o valor de pi é {num}')

# valor_de_pi(3.14)

# def dobro_do_numero(num):
#     return num * 2

# print(dobro_do_numero(5))

# def letras_maiuscula(palavra):
#     return palavra.upper()
    
# print(letras_maiuscula('infinity'))

# def soma(a,b):
#     return a + b

# print(soma(5, 5))

def nome_hora(nome, hora):
    if hora < 12:
        return f' bom dia {nome}, são {hora}h da manhã '
    elif hora < 19:
        return f'boa tarde {nome}, são {hora}h da tarde '
    else:
        return f' boa noite {nome}, são {hora}h da noite'
    
print(nome_hora('joao', 10))
print(nome_hora('joao', 17))
print(nome_hora('joao', 20))
