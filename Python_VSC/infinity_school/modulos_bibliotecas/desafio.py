'''1-Crie um programa que permita aos usuários:
Adicionar novos livros à biblioteca, com informações como título,
autor e número de cópias disponíveis.
Listar todos os livros disponíveis na biblioteca.
Permitir aos usuários fazer empréstimos de livros, reduzindo o
número de cópias disponíveis quando um livro é emprestado.

2-Permitir aos usuários devolver livros, aumentando o número de
cópias disponíveis quando um livro é devolvido.
Verificar a disponibilidade de um livro específico na biblioteca.
Mostrar a lista de livros emprestados a um usuário específico.'''



lista_de_emprestimo = []

# lista já criada com 2 livros e sera aonde recebera mais ao ser adiconados
lista_de_livros = [{                
        'nome do livro': 'z',
        'nome do autor': 'JK',
        'disponibilidade': 'disponivel',
        'numero de copias': 1,
        'livro alugado por': None,        # 'livro alugado por':'0'       
    },
     {
        'nome do livro': 'titanic',
        'nome do autor': 'Cameron Dias',
        'disponibilidade': 'disponivel',
        'numero de copias': 5,
        'livro alugado por': None,      
    }]



# vai filtrar a lista de pessoas que pegaram livros emprestado , se a lista estiver == 0 sera vazia se nã0, vai mostrar a pessoa e o livro que pegou
def filtro_emprestimo_pessoa(nome_do_meliante):
        if len(lista_de_emprestimo) == 0:
            print('nenhum livro foi emprestado')
            return

        lista_cliente = []

        for c in lista_de_emprestimo:   
            if nome_do_meliante == c['nome da pessoa']:
                lista_cliente.append(c['livro'])
        
        if lista_cliente:
            print(f'livro emprestado para: {nome_do_meliante}')
            for n in lista_cliente:
                print(f' livro: {n}')
        else:
            print(f'nenhume emprestimo encontrado para o cliente: {nome_do_meliante}')


                

    
#função que adicona mais livro a lista de livros.
def livros():
    nome_livro = input('Titulo do livro: ')
    autor = input('nome do escritor do autor: ')
    disponibilidade = 'disponivel'
    numero_copias = 3
    cliente_que_alugou = '0'

    biblioteca = {
        'nome do livro': nome_livro,
        'nome do autor': autor,
        'disponibilidade': disponibilidade,
        'numero de copias': numero_copias, 
        'livro alugado por': cliente_que_alugou       
    }
    lista_de_livros.append(biblioteca)



def pegar_emprestado(livro_emprestado):
    
    livro_encontrado = None

    for c in lista_de_livros:
        if livro_emprestado == c['nome do livro']: # checa se o nome do livro e se o numero de copias é igual a 0.
            livro_encontrado = c
            break

    if livro_encontrado:

        if livro_encontrado['numero de copias'] > 0:
            livro_encontrado['numero de copias'] -=1
            nome_pessoa = input('qual o nome da pessoa do emprestimo: ')
            print(f' emprestimo feito: nome do cliente: {nome_pessoa} | {livro_encontrado}')
            
            registro_de_emprestimo = {
                'nome da pessoa': nome_pessoa,
                'livro': livro_encontrado['nome do livro']
            }
            lista_de_emprestimo.append(registro_de_emprestimo)
        else:
            print(f'todas copias do livro {livro_encontrado['nome do livro']} esão indisponiveis no momento')

    else:
        print('não temos esse livro em nossa biblioteca')    

        
      
       
# faz uma checagem na lista de dicionario usando for confirma se o nome do livro esta dentro do dicionario se sim rertorna +1 para numero de copia.
def devolver_livro(livro_devolvido, pessoa):

    livro_encontrado = False #guarda na variável se  o livro foi encontrado

    for c in lista_de_livros:# for, para verificar se o livro faz parte da lista de livros, se faz, adiciona +1 no numero de copias pois está sendo a devolução de um livro e atribui True a variavel livro_encontrado
        if livro_devolvido == c['nome do livro'] :
            c['numero de copias'] += 1
            print(f'livro devolvido com sucesso, estoque atualizado: livro empresatado com sucesso, {c['nome do livro']} | {c['nome do autor']} | {c['disponibilidade']} | {c['numero de copias']} | {c['livro alugado por']} ')
            livro_encontrado = True
            break

    if not livro_encontrado: # se não foi encontrado exibe a saída
         print('livro não faz parte da nossa biblioteca')
         return
    
    emprestimo_para_remover = None # inicai sem valor algum e vai receber valor se a checagem for verdadeira pelo for.

    for remover in lista_de_emprestimo: #usando for, para checar se a pessoa e livro estão na lista de emprestimo se sim atribui um valor verdadeiro dentro da variável emprestimo_para_remover.
        if pessoa == remover['nome da pessoa'] and livro_devolvido == remover['livro']:
            emprestimo_para_remover = remover
            break

    if emprestimo_para_remover:# usamos a nossa varial que agora tem valor, como é verdadeiro possibilita a lista remover o dicionario com os dados do empréstomo.
        lista_de_emprestimo.remove(emprestimo_para_remover)
        print(f' devolução feita com sucesso para: {pessoa}')
        
    else:
        print(f' não foi encontrado registro de emprestimo para: {livro_devolvido}') # sse o if for falso executa o else.
    


         

def adicionando_livros():
    livro_novo = input('nome do livreo que deseja adiconar na biblioteca: ')
    autor_novo = input('nome do escritor do autor: ')
    disponibilidade_novo = 'disponivel'
    numero_copias_novo = int(input('quantas copias serão adicionadas: '))
    cliente_que_alugou = '0'

    new_dicionario = {
        'nome do livro': livro_novo,
        'nome do autor': autor_novo,
        'disponibilidade': disponibilidade_novo,
        'numero de copias': numero_copias_novo, 
        'livro alugado por': cliente_que_alugou        
    }
    lista_de_livros.append(new_dicionario)

    for c in lista_de_livros:
        if livro_novo == c['nome do livro']:
            print(f'livro adicionado com sucesso: {c['nome do livro']} | {c['nome do autor']} | {c['disponibilidade']} | {c['numero de copias']} | {c['livro alugado por']} ')

    
def ver_se_livro_esta_disponivel(nome):
    livro_encontrado = None

    for c in lista_de_livros:
        if nome == c['nome do livro']:
            livro_encontrado = c
            break
    
    if livro_encontrado:

        if livro_encontrado['numero de copias'] > 0:
            print(f'livro{livro_encontrado['nome do livro']} encontras e disponpivel no momento com {livro_encontrado["numero de copias"]} copias')
        else:
            print(f'todas copias de:{livro_encontrado['nome do livro']} estão indiposniveis no momento')

    else:
        print('esse livro não faz parte da nossa biblioteca, desculpe!')



while True:
    print(60 * '-=')
    print('Bibliote Tech World')
    acao = input('1- exibir catálago de livros, 2- fazer aluguel de livro, 3- devolver livro, 4-adicionar livros,  5-disponibilidade ,[s]air: ' )
    print(60 * '-=')

    if acao =='s':
        print('foi um prazer servir o Sr com nossa Bibliote, volte sempre e otimo dia!')
        break

    elif acao =='1':
        opcao = input('1- deseja mostrar lista completa de livro ou 2- fitrar por lista de pessoas que alugaram livros: ')

        if opcao =='1':
            for c in lista_de_livros:
                print(c)

        elif opcao=='2':
            seu_nome = input('qual o nome: ')
            filtro_emprestimo_pessoa(seu_nome)
        
    elif acao =='2':
        nome_livro = input('qual livro disponivel quer emprestado: ')
        pegar_emprestado(nome_livro)

    elif acao =='3':
        devolucao_livro = input('qual livro esta devolvendo de emprestimo: ')
        cliente = input('qual o nome do cliente que esta devolvendo: ')
        devolver_livro(devolucao_livro, cliente)

    elif acao =='4':
        adicionando_livros()

    elif acao =='5':
        ver_nome_livro_disponivel = input('nome do livro para verificar a disponibilidade: ')
        ver_se_livro_esta_disponivel(ver_nome_livro_disponivel)
        
