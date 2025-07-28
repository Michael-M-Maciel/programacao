'''ATIVIDADE PRÁTICA 1

Crie uma função chamada calcular_imc(peso, altura) que calcule e retorne o IMC de uma pessoa.
Depois, crie outra função chamada classificar_imc(imc) que, com base no IMC calculado, retorne a categoria da pessoa.
Por fim, crie um programa que peça ao usuário o peso e a altura, calcule o IMC e mostre o resultado com a classificação.'''


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificaca0_imc(imc):
    if imc < 18.5:
        return 'abaixo do peso'
    elif imc < 25:
        return 'peso normal'
    elif imc < 30:
        return 'sobrepeso'
    elif imc < 35:
        return 'obesidade grau 1'
    elif imc < 40:
        return'obesidade grau 2'
    else:
        return'obesidade grau 3 (obesidade morbida)'

while True:

    print("Calculo do IMC")
    
    peso = float(input("qual seu peso: "))
    altura = float(input('qual sua altura: '))
    imc = calcular_imc(peso, altura)
    

    print(f'seu IMC é {imc:.2f}')
    print(f'sua classificação é {classificaca0_imc(imc)}')


