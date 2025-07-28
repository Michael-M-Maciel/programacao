temp = []
principal = []
mai = men = 0


while True:
    temp.append(input('nome: '))
    temp.append(input('peso: '))

    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1] 

    principal.append(temp[:])
    temp.clear()
    opcao = input('sair [s/n]: ')
    if opcao =='s':
        break

print(40 * '*')
print(principal)
print(f'foram adicionado {len(principal)} pessoas')
print(f'o maior peso foi {mai}kg. peso de', end=' ')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'o menor peso foi de: {men}kg. peso de ', end=' ')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()



