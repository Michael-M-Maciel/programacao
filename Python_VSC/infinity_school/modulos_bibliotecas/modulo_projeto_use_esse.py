'''1-Crie um programa que permita aos usuários:
Adicionar novos livros à biblioteca, com informações como título,
autor e número de cópias disponíveis. *******************************

Listar todos os livros disponíveis na biblioteca.****************************

Permitir aos usuários fazer empréstimos de livros, reduzindo o ************************
número de cópias disponíveis quando um livro é emprestado.

2-Permitir aos usuários devolver livros, aumentando o número de **********************
cópias disponíveis quando um livro é devolvido.

Verificar a disponibilidade de um livro específico na biblioteca.************************

Mostrar a lista de livros emprestados a um usuário específico.*************************'''


lista_de_emprestimo =[]

# lista de dicionario aonde serão adicionados mais livros
biblioteca =[ 
    {'nome do livro': 'z',
    'autor do livro': 'c',
    'numero de copias': 1,
    },

    {'nome do livro': 'x',
    'autor do livro': 'ss',
    'numero de copias': 2,
    }

    ]


# função com dicionario que irá receber os valores por argumento
def adicionar_novos_livros(livro_add, autor_add, num_cop):
    
    dicionario_novos_livros = {
        'nome do livro': livro_add,
        'autor do livro': autor_add,
        'numero de copias': num_cop,
    }

    biblioteca.append(dicionario_novos_livros) # adicionando o dicionário na lista [biblioteca]




def usuario_fazendo_emprestimo(qual_livro):

    livro_encontrado = None # variável para  guardar o livro quando encontrado usando for, sendo assim será verdadeiro se tiver livro , se não será false.

    for livro in biblioteca: # for para procurar se o nome do livro exista na lista de dicionario, se sim variavel livro_encontrado recebera todo o dicionario com o nome do livro.
        if qual_livro == livro['nome do livro']:
            livro_encontrado = livro
            break

    if livro_encontrado: # ja que livro foi encontrado e é verdadeiro seguimos com a execução do if

        if livro_encontrado['numero de copias'] > 0:
            livro_encontrado['numero de copias'] -= 1
            nome_usuario_emprestimo = input('Nome do usuario que pegou o livro empresatado: ')
            print(f'lista de emprestimo atualizada: livro: {livro_encontrado['nome do livro']} foi emprestado para o usuário: {nome_usuario_emprestimo} ')
            #criar um dicionário para adiciona-lo na lista de emprestimo.

            dicionario_de_emprestimo ={  # criar um dicionado exlusivo para lista te emprestimo
                'nome do usuario': nome_usuario_emprestimo,
                'nome do livro': livro_encontrado['nome do livro']
            }

            lista_de_emprestimo.append(dicionario_de_emprestimo) # adicionando dicionario em lista de emprestimo

        else:# livro encontrado ou temos na biblioteca mas quando numero de copias for 0 ou seja todos livros ja emprestados executa o else
            print(f' todos livro: {livro_encontrado['nome do livro']} estão emprestados no momento')

    else:# quando o livro solicitado para para emprestimo não existir em nossa biblioteca , executa o else
        print('não temos esse livro em nossa biblioteca')
    



# função para adicionar +1 ao numero de copia ao devolver livro e remover usuario e livro que estavam na lista de emprestados
def usuario_devolvendo(livro_devolucao, usuario_entregando):
    livro_de_devolvendo = False 

    for livros in biblioteca: # percorre  toda a lista e verifica se o livro que esta sendo devolvido existe em nossa biblioteca se sim adcionas +1 ao numero de copias e atribiu true na variavel que era false.
        if  livro_devolucao == livros['nome do livro']:
            livros['numero de copias'] +=1
            livro_de_devolvendo = True
            break

        if not livro_de_devolvendo: # se o livro não existe em nossa bliblioteca executa esse if
            print('esse livro não faz parte da nossa biblioteca')
            return

    emprestimo_remover = None # inicai sem valor algum e vai receber valor se a checagem for verdadeira pelo for.


    for pendente in lista_de_emprestimo: #usando for, para checar se a pessoa e livro estão na lista de emprestimo se sim atribui um valor verdadeiro dentro da variável emprestimo_para_remover.
        if livro_devolucao == pendente['nome do livro'] and usuario_entregando == pendente['nome do usuario']:
            emprestimo_remover = pendente
            break
        

    if emprestimo_remover:
        print(f'devolução do livro: {livro_devolucao} feita com sucesso pelo cliente: {usuario_entregando}')
        lista_de_emprestimo.remove(emprestimo_remover) # usamos a nossa variavel que agora tem valor, como é verdadeiro possibilita a lista remover o dicionario com os dados do empréstomo.
        
    else:
        print(f'não existe registro de emprestimo para livro: {livro_devolucao}, até mais e obrigado')    # se o if for falso executa o else.



# função para verificar se um livro esta disponivel ou nao
def disponibilidade(livro_desejado):
    livro_encontrado = None # variavel para receber o valor de todo dicionaro se a checagem no for == verdadeira.

    for livro in biblioteca: # fro para vorrer a lista de livro e tentar achar se o nome do livro solicitado esta na lista e se o numero de copia ainda esta disponivel
        if livro_desejado == livro['nome do livro'] and livro['numero de copias'] > 0:
            livro_encontrado = livro
            break

    if livro_encontrado: # se tudo foi checada e verdadeiro executa  o if se estiver disponivel , se nao executa o else se o numero de copias estiver zerado
        print(f'sim livro está disponivel: {livro_encontrado}')
    else:
        print('livro indisponivel no momento, todos alugados!!!')




def listando_emprestados():# função que mostra a lista de livro e usuario quando algum  usuario pegou um livro emprestado
    
    if len(lista_de_emprestimo) > 0:
        for c in lista_de_emprestimo:
            print(f'lista de livro emprestados: {c}')
            break
    else:
        print('lista vazia no momento')
    
