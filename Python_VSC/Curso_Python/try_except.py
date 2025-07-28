numero = input('vou dobra o numero que vc digitar: ')

try:
    numero_float = float(numero)
    print(f'o dobro de {numero} é {numero_float* 2:.2f}')
except:
     print('isso não é um numero')



