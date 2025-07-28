'''1. print vs. return (A Diferença Crucial)
print(): É uma função que exibe um valor no console.
 É útil para depuração e para mostrar informações ao usuário final.
 A função em si não "entrega" nada para o seu código, apenas mostra na tela.

return: É uma instrução que envia um valor de volta para a linha de código que chamou a função.
Esse valor pode ser armazenado em uma variável, usado em uma expressão matemática, passado para outra função, etc.'''





# def somar_com_print(numero1, numero2):
#     resultado = numero1 + numero2
#     print(f'o resultado (mostrado dentro da função) é {resultado}')

# print('Chamando a função com print:')
# resultado_obtido = somar_com_print(5, 3)
# print(' ')
# print(f"o valor que a minha variavel 'resultado_obtido' recebeu foi: {resultado_obtido}" )



# def somar_com_return(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado  # Entrega o valor da variável 'resultado'

# print("\nChamando a função com return:")
# resultado_obtido = somar_com_return(5, 3) # O valor retornado (8) é colocado aqui
# print(f"O valor que a minha variável 'resultado_obtido' recebeu foi: {resultado_obtido}")

# # Agora podemos USAR esse resultado!
# print(f"Podemos usar o resultado em outro cálculo: {resultado_obtido} * 2 = {resultado_obtido * 2}")



# def exemplo_saida_imediata():
#     print("Isso será executado.")
#     return "Saindo da função!"
#     print("Isso NUNCA será executado.")

# print(exemplo_saida_imediata())


# def calculo_preco_final(preco_bruto, percentual_desconto):
#     valor_desconto = preco_bruto *(percentual_desconto / 100)
#     preco_final = preco_bruto - valor_desconto
#     return preco_final
    
# valor_a_pagar = calculo_preco_final(100, 15)
# print(f'o valor a pagar é {valor_a_pagar}')



# def converter_celsius_para_fahrenheit(temperatura_celsius):
#     fahrenheit = (temperatura_celsius * 9/5) + 32
#     return fahrenheit

# resultado = converter_celsius_para_fahrenheit(38)
# print(f'a temperatude de Cº para Fº foi {resultado}Fº')

# def formatar_titulo(texto):
#     texto_maiusculo = texto.upper()
#     linha = '-' * len(texto_maiusculo)

#     titulo_formatado = f'{texto_maiusculo}\n{linha}'
#     return titulo_formatado

# meu_titulo = formatar_titulo('titulo')
# print(meu_titulo)


# def idade(idade):
#     if idade >= 18:
#         return True
#     else:
#         return False
    
# pode_entrar_festa = idade(18)
# não_pode_entrar_festa = idade(17)

# print(f'a pesseoa com mais de 17 anos pode entrar na festa? {pode_entrar_festa}')
# print(f'a pesseoa com menos de 18 anos pode entrar na festa? {não_pode_entrar_festa}')

# def dar_o_numero_dez():
#     return 10

# numero_dez = dar_o_numero_dez()
# print(numero_dez)

# def somar_um(numero):
#     resultador = numero + 1
#     return resultador

# calculo = somar_um(10)
# print(calculo)


# def frase_ponto(frase):
#     com_ponto = frase +'.'
#     return com_ponto

# frase_final = frase_ponto('bom dia')
# print(frase_final)