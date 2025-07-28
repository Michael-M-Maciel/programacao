def soma():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    somar = num1 + num2
    print(f'a soma entre os numeros é = {somar}')

def subtracao():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    subtrair = num1 - num2
    print(f'a subtração entre os numeros é = {subtrair}')

def multiplicacao():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    multiplicar = num1 * num2
    print(f'a multiplicação entre os numeros é = {multiplicar}')

def divisao():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    dividir = num1 + num2
    print(f'a divisao entre os numeros é = {dividir}')


while True:
    print(10* '-=','calculadora',10*'-=')
    print('escolha +[somar], -[subtrair], *[multiplicar], /[dividir] e [s]air')
    opcao = input(' qual calculo desejar executar: ')

    if opcao =='s':
        print('sair')
        break

    elif opcao =='-':
        subtracao()

    elif opcao =='*':
        multiplicacao()

    elif opcao =='/':
        divisao()

    else:
        print('opção invalida')


            
      