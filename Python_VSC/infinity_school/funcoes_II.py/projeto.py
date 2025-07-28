#1- função de criar as tarefas
#2- função menu com as ações
#3- função  para listar as tarefas no menu
#4- função para mostrar a lista de tarefa pelo 'ID'
#5 - função para mudar o status para concluido
#6 - função para remover a tarefa pelo seu iD
#7 - função para filtrar por categoria

lista_de_tarefas = []


def por_categoria():
    categoria_tarefa = input('que prioridade quer ver:')
    for c in lista_de_tarefas :
        if categoria_tarefa == c['categoria']:
            print(f'{c['iD']} | {c['tarefa']} | {c['descrição']} | {c['categoria']} | {c['status']}')
        else:
            print('categoria errada')
       

def removendo_tarefa():
    id_remover_tarefa = int(input(' qual iD da tarefa que deseja remover: '))
    for c in lista_de_tarefas:
        if id_remover_tarefa == c['iD']:
            print(f'tarefa foi removida: {c}')
            lista_de_tarefas.remove(c)
        


def concluir_tarefas():
    print(' ')
    id_da_tarefa = int(input('qual iD da tarefa desejada: '))


    for c in lista_de_tarefas:
        if id_da_tarefa == c['iD']:
            c['status'] = '✅ Concluido(a)'
            print(f'{c['iD']} | {c['tarefa']} | {c['descrição']} | {c['categoria']} | {c['status']}')


def listar_por_id():
    id_tarefa = int(input('qual id da tarefa desejada: '))
    for c in lista_de_tarefas:
        if id_tarefa == c['iD']:
            print(f'{c['iD']} | {c['tarefa']} | {c['descrição']} | {c['categoria']} | {c['status']}')
            break




def criar_tarefas():
    print(' ')
    id = len(lista_de_tarefas) + 1
    tarefa = input('nome da tarefa: ')
    descricao = input('descreva a tarefa desejada: ')
    categoria = input('categoria alta , media ou baixa: ')
    status = 'Pendente'


    dicionario_de_tarefas = {
        'iD': id,
        'tarefa': tarefa,
        'descrição': descricao,
        'categoria': categoria,
        'status': status
    }


    lista_de_tarefas.append(dicionario_de_tarefas)



def menu_de_tarefas():
    while True:
        print(' ')
        print('📝MENU de Tarefas📝')
        print('selecione:  1️⃣ adicionar, 2️⃣ listar tarefas,3️⃣ concluir, 4️⃣ remover tarefas e 5️⃣ filtro prioridae e  6️⃣ sair🔚 ')
        opcao = input('o que deseja fazer: ')


        if opcao == '6':
            print('finalizando')
            break


        elif opcao =='1':
            criar_tarefas()


        elif opcao =='2':
            print('deseja mostrar lista completa: [s]im ou [n]ão')
            opcao = input('sim ou não: ')

            if len(lista_de_tarefas) == 0:
                print('Sua lista de tarefas está vazia')

            elif opcao =='s':
                for c in lista_de_tarefas:
                    print(c)  
                   
            elif opcao == 'n':
                listar_por_id()
            else:
                print('opçcao invalida')


        elif opcao =='3':
            concluir_tarefas()


        elif opcao =='4':
            removendo_tarefa()
        elif opcao =='5':
            por_categoria()
        else:
            print('opção invalida, tente novamente')


menu_de_tarefas()