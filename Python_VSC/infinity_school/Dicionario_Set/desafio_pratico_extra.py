emprestimos = [
    {
        'nome': 'michael',
        'livro': 'harry',
        'dias': 3
    }
]

while True:
    print('emprestimo de livros')
    print('digite [C]cadastro e [S]air')
    opcao = input('escolha a opção acima: ').upper()

    if opcao =='S':
        print('saindo')
        break
    elif opcao =='C':
        nome = input('nome da pessoa: ')
        livro = input('nome do livro: ')
        dias = int(input('dias de emprestimo: '))

        emprestimo = {
            'nome': nome,
            'livro': livro,
            'dias': dias
        }
        emprestimos.append(emprestimo)

    else:
        print('repita, opção invalida')

print(f'a quantidade de emprestimo foi {len(emprestimos)}')

maior_prazo = 0
nome_pessoa =''

for c in emprestimos:
    if maior_prazo < c['dias']:
        maior_prazo = c['dias']
        nome_pessoa = c['nome']
        
    if c['dias'] >= 7:
        print('emprestimo com mais de 6 dias')
        print(f'cliente {c['nome']} \n com o livro {c['livro']}')

print(f'maior emprestimo foi de {nome_pessoa} com o prazo de {maior_prazo}dias')













# maior_prazo = 0
# nome_pessoa =''

# for c in emprestimos:
#     print(c)

#     if c['dias'] > maior_prazo:
#         maior_prazo = c['dias']
#         nome_pessoa = c['nome']

#     if c['dias'] > 7:
#         print('emprestimo com mais de 6 dias')
#         print(f'nome: {c['nome']}\n livro:{c['livro']}')

# print(f'maior emprestimo foi: {nome_pessoa} de {maior_prazo} dias')


    