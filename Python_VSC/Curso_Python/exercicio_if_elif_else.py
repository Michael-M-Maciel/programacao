primeiro_valor = input('digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ' )

if primeiro_valor > segundo_valor:
    print(f'  {primeiro_valor =} é maior que {segundo_valor =}')
elif primeiro_valor < segundo_valor:
    print(f'o  {primeiro_valor =} é menor que {segundo_valor =}')
else:
    print(f'{primeiro_valor =} é igual o {segundo_valor =}')
