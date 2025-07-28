from modulo_atividade05 import(metros_para_pes, kilos_para_libra, graus_para_fahreneheit)

'''Desenvolva um programa que permita ao usuário
converter entre diferentes unidades de medida, como
metros para pés, quilogramas para libras, ou Celsius
para Fahrenheit. Use módulos que contenham funções
de conversão.'''

while True:
    
    print(45 * '-=')
    opcao = input('1-converter[metros / pes], 2-converter [kg / libras], 3- converter [Cº / Fº] e [s]air: ')
    if opcao =='s':
        print('saindo..')
        break

    elif opcao =='1':
        metros = float(input('digite a unidade em metro que deseja converter em pés: '))
        print(metros_para_pes(metros))
        

    elif opcao =='2':
        kilos = float(input('digite a unidade em Kg que deseja converter em libras: '))
        print(kilos_para_libra(kilos))
    elif opcao =='3':
        celcius = float(input('digite a medida em Cº que deseja converter em Fº: '))
        print(graus_para_fahreneheit(celcius))
    else:
        print('opção invalida!')


        
   
        

