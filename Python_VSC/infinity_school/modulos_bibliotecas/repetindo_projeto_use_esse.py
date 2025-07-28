from modulo_projeto_use_esse    import (lista_de_emprestimo, biblioteca, adicionar_novos_livros, usuario_fazendo_emprestimo, usuario_devolvendo, disponibilidade, listando_emprestados)

while True:
    print(40 * '-=')
    #menu com as funcionalidade
    opcoes = input('[1]-adicionar livros, [2]-listar livros, [3]-fazer emprestimo de livro, [4]-devolução de livro, [5]-disponibilidade, [6]lista de emprestados: ')

    if opcoes =='1':
        # argumentos para função [def adiconar_novos_livros]   
        nome_do_livro = input('digite o nome do livro: ')
        autor_do_livro = input('digite o autor do livro: ')
        numero_de_copias =  int(input('digite o numero de cópias: '))
        adicionar_novos_livros(nome_do_livro, autor_do_livro, numero_de_copias) # função sendo chamada e passando os argumentos

    elif opcoes == '2':
        print(40 * '-=')
        print('lista completa de livros: ')
        for listar in biblioteca: # saída com for, para listar um dicionário abaixo do outro
            print(listar)

    elif opcoes =='3':
        nome_livro_para_emprestimo = input('digite o nome do livro para emprestimo: ')# argumento para ser usado na função
        usuario_fazendo_emprestimo(nome_livro_para_emprestimo) # chamando a função com argumento

    elif opcoes=='4':
        devolucao_do_livro = input('digite o nome do livro que está devolvendo: ') #argumentos para a função
        nome_usuario_devolucao =  input('nome do usuário que pegou emprestado o livro: ')
        # pessoa_devolvendo = input('nome da pessoa que alugou o livro: ')
        usuario_devolvendo(devolucao_do_livro, nome_usuario_devolucao) #chamando função e passsando os argumentos

    elif opcoes =='5':
        vendo_livro_disponivel =  input('qual livro deseja ver a disponibilidade: ')# argumento para ser usado na função
        disponibilidade(vendo_livro_disponivel) # chamando a função com argumento

    elif opcoes=='6':
        listando_emprestados() # mosra a lista de emprestados com nome do livro e quem pegou emprestado