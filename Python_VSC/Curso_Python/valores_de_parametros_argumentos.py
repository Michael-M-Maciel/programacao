# def soma(x, y, z=0):
#     if z:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)

# soma(1, 2, 3)

# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)

        
# soma(100, 200)
# soma(1, 2)
# soma(1, 2, 8) # nesse cazo z recebe valor então não é nulo e se executa o if


# def apresentacao():
#     print('meu nome é Michael')
#     print('Estou aprendendo funções em Pyhton!')

# apresentacao()

#argumentos nomenais
# def descrever_pet(tipo_animal, nome_do_animal):
#     print(f'eu tenho {tipo_animal}')
#     print(f'o nome dele é {nome_do_animal}')

# descrever_pet(tipo_animal='cachorro', nome_do_animal='pluto')
# descrever_pet(nome_do_animal='pluto', tipo_animal='cachorro')
# print('---')
# descrever_pet('papagaio','xuxa')

#ex02:
# def criar_email(nome_usuario, provedor='gmail.com'):
#     print(f'login {nome_usuario}@{provedor}')

# criar_email('michael.Dev')
# criar_email('michael.Python','Hotmail.com')
# criar_email(provedor='outlook.com', nome_usuario='michael.Infinity')



#parâmentos com valores padrão (Default)

# def descrever_cidade(cidade, pais='Brasil'):
#     print(f'{cidade} fica no {pais}')

# descrever_cidade('maceió') # ao não declarar o argumento ao parâmetro {pais}, automaticamente recece o valor atribuido no parâmetro inicialmente
# descrever_cidade('Lisboa', 'Portugal')



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