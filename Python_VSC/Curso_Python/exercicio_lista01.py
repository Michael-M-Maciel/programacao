
lista = []
while True:
    print('escolha uma opção😎 : ')
    opcao = input('[a]dicinar [r]emover [l]istar: ')
    if opcao =='a':
        Valor = input('Valor: ')
        lista.append(Valor)

    elif opcao =='r':
        indice = int(input('qual indice deseja remover: '))
        lista.pop(indice)

    elif opcao =='l':
        if len(lista) == 0:
            print('não temo o que mostrar')
        for c, valor in enumerate(lista):
             print(c, valor)
      
    