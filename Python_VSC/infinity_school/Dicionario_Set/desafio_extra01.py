'''ATIVIDADE PRÁTICA EXTRA 1

Crie um programa que cadastre nomes de pessoas em uma lista.

O programa deve:

- Perguntar ao usuário se deseja cadastrar um novo nome.

- Os nomes devem ser armazenados em uma estrutura de dados (listas, tuplas, sets ou dicionários)

- O programa deve continuar pedindo novos nomes enquanto até o usuário decidir não continuar.

- Ao final, exibir todos os nomes cadastrados.
'''

lista =[]
print('CADASTRO PESSOAL')

while True:
    print(40 * '-=')

    cadastro = input('deseja fazer seu cadastro agora [S]im ou [N]ão:') 
    if cadastro =='n':
        print('Saindo do cadastro, até logo.')
        break

    elif cadastro =='s':
        print(40 * '-=')
        print('bem vindo!! vamos inicar seu cadastro a seguir.')
        nome = input('digite seu nome: ')
        idade = int(input('digite sua idade: '))
        profissao = input('qual sua profissão: ')

        dicionario = {
            'nome': nome,
            'idade': idade,
            'profissao': profissao
        }
        lista.append(dicionario)
        
for pessoa in lista:
    print(40* '-=')
    print(f'Nome: {pessoa['nome']}')
    print(f'Idade: {pessoa['idade']}')
    print(f'Profissão: {pessoa['profissao']}')


        

    
    

     

   
