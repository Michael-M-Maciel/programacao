def soma():
    num1 = float(input('qual o primeiro numero:'))
    num2 = float(input('qual o segundo numero:'))
    return num1 + num2

def subtrair():
    num1 = float(input('qual o primeiro numero:'))
    num2 = float(input('qual o segundo numero:'))
    return num1 - num2

def multiplicar():
    num1 = float(input('qual o primeiro numero:'))
    num2 = float(input('qual o segundo numero:'))
    return num1 * num2

def dividir():
    num1 = float(input('qual o primeiro numero:'))
    num2 = float(input('qual o segundo numero:'))
    if num2 == 0:
        return 'erro de divisor por zero'
    else:
        return num1 / num2



