from modulo_atividade01 import(somar, subtrair, multiplicar, dividir)

while True:    
    opcao = input('somar[+], subtrair[-], multiplicar[*], [/]dividir e [s]air: ')
    if opcao =='s':
        print('finalizando')
        break
    

    numero1 = float(input('digite numero1 : '))
    numero2 = float(input('digite numero2 : '))

    if opcao =='+':
        print(somar(numero1, numero2))

    elif opcao=='-':
        print(subtrair(numero1, numero2))

    elif opcao=='*':
        print(multiplicar(numero1, numero2))

    elif opcao=='/':
        print(dividir(numero1, numero2))

    else:
        print('opção invalida')
    
        
   
