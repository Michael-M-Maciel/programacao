
lista_de_tarefas = []


def criar_tarefa():
    id = len(lista_de_tarefas)+1
    tarefa = input('qual nome da tarefa: ')
    descricao = input('qualfa a descrição da tarefa: ')
    prioridade = input('alta , media ou baixa: ')
    status = 'pendente'

    dicionario_tarefas = {
        'id': id,
        'tarefa': tarefa,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': status       

    }
    lista_de_tarefas.append(dicionario_tarefas)



def listar_tarefa():
     print('')
     opcao = input('quel listar todas tarefas [s/n]: ')
    
     if opcao =='s':
         if len(lista_de_tarefas) == 0:
            print('a lista ainda está vazia, adicione alguma tarefa.')
         else:
            for c in lista_de_tarefas:
             print(c)
               
     elif opcao =='n':
         print('')
         id_tarefa = int(input("qual id da tarefa que deseja: "))
         for c in lista_de_tarefas:
             if id_tarefa == c['id']:
                 print(c)
     else:
         print('opção invalida') 
         


def concluir():
    qual_id_concluir = int(input('qual id da tarefa que deseja concluir: '))

    for c in lista_de_tarefas:
        if  qual_id_concluir == c['id']:
            c['status'] = 'concluido'
            print(f'{c['id']} | {c['tarefa']} | {c['descricao']} | {c['prioridade']} | {c['status']}')


def prioridade():
    print('')
    escolha_prioridade = input('qual prioridade de tarefa quer listar: [alta], [media] ou  [alta]: ')
    for c in lista_de_tarefas:
        if escolha_prioridade == c['prioridade']:
            print(c)


def excluir_tarefa():
    qual_id = int(input('qual id da tarefa que deseja excluir: '))
    for c in lista_de_tarefas:
        if qual_id == c['id']:
            print(f'tarefa excluida : {c['id']} | {c['tarefa']} | {c['descricao']} | {c['prioridade']} | {c['status']} ')
            lista_de_tarefas.remove(c)
            return


def tarefas_menu():
    while True:
        print('')
        menu = input('[1]-adicionar tarefa, [2]-listar tarefa, [3]-concluir, [4]-filtrar prioridade, [5]- excluir tarefa e [6]-sair :  ')
        
        if menu =='6':
            print('finalizando...')
            break
        
        elif menu =='1':
            criar_tarefa()

        elif menu =='2':
            listar_tarefa()

        elif menu =='3':
            concluir()

        elif menu =='4':
            prioridade()

        elif menu =='5':
            excluir_tarefa()
