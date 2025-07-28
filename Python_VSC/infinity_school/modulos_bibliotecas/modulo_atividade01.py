

'''Crie um programa que será uma calculadora.
Nesta calculadora você deverá ter um módulo para as
operações matemáticas, o arquivo principal deverá
conter apenas um menu de escolha para o usuário
(soma, subtração, multiplicação e divisão).'''


def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return 'erro de divisão por 0'
    else:
        return num1 / num2
