# x, y , *resto = 1, 2, 3, 4
# print(x,y, resto)



# def soma(x, y):
#     return x + y

# def soma(*args): # args retorna uma tupla
#     print(args)

# soma(1, 2, 3, 4, 5)


# def soma(*args): # args retorna uma tupa
#     total = 0
#     for c in args:       
#         total += c        
#     return(total)
          
# soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)
# print(soma_1_2_3)

# numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# outra_soma = soma(*numeros)
# print(outra_soma)

# print(sum(numeros))

# def multiplicar(a, b, *args):
#     return a , b, args

# print(multiplicar('michael','max','ana', 'paula'))



def operacoes_basicas(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao

# A função retorna uma tupla (um tipo de coleção de dados em Python)
resultado_tupla = operacoes_basicas(10, 2)
print(f"A função retornou uma tupla: {resultado_tupla}")
print(f"O primeiro item da tupla é: {resultado_tupla[0]}") # Acessando o primeiro item

# A forma mais comum é "desempacotar" os resultados em variáveis separadas
s, sub, m = operacoes_basicas(10, 2)
print(f"\nResultados desempacotados:")
print(f"Soma: {s}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {m}")