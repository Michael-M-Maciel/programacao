nome1 = input('qual o nome do produto : ')
produto1 = float(input('qual o valor do produto: '))
nome2 = input('qual o nome do produto : ')
produto2 = float(input('qual o valor do produto: '))
nome3 = input('qual o nome do produto : ')
produto3 = float(input('qual o valor do produto:: '))
nome4 = input('qual o nome do produto : ')
produto4 = float(input('qual o valor do produto:: '))

total = sum([produto1, produto2, produto3, produto4])

print(30* '-=')
dicionario = {
    'nome1': nome1,
    'produto1': produto1,
    'nome2': nome2,
    'produto2': produto2,
    'nome3': nome3,
    'produto3': produto3,
    'nome4': nome4,
    'produto4': produto4
             }

for c in dicionario.items():
    print(c)

print(30* '-=')
print(f'o valor total custou {total} R$')