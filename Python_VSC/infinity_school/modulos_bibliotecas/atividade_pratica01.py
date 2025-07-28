import modulos


while True:
    opcao = input('soma [+], subtrai[-], multiplicar[*], dividir[/] e [s]air: ')

    if opcao in 'Ss':
        print('saindo' )
        break

    elif opcao == '+':
        print(modulos.soma())

    elif opcao =='-':
        print(modulos.subtrair())

    elif opcao =='*':
        print(modulos.multiplicar())
        
    else:
        print(modulos.dividir())