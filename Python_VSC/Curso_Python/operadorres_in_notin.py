# in , not in 
# nome = 'michael'

# print('l' in nome)
# print('z' in nome)
# print('ç' not in nome)
# print('mic' in nome)
# print(10 * '-')

nome = input('digite o nome: ')
encontrar = input('digite o que quer encronar no nome: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nãó esta em {nome}')