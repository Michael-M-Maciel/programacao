# def saida_imediata():
#     print("vou sair")
#     return('saindo')
#     print('nunca acontecera')

# print(saida_imediata())





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