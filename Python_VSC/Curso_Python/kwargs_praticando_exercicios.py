# def praticando(**kwargs):
#     for chave, valor in kwargs.items():
#         print (f'{chave} : {valor}')


# praticando(nome='Michael', sobrenome='Maciel', idade=37)
    

# def nomes(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave} : {valor}')

# nomes(nome='michael', sobrenome='maciel')

# def exibir_dados(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave}:{valor}')

# exibir_dados(nome='michael', sobreno='maciel')


# def tem_email(**kwargs):
#     return'email' in kwargs

# print(tem_email(nome='michael', email='michaelmaicel2@hotmail.com'))
# print(tem_email(nome='michael'))



# def cumprimento(**kwargs):
#     nome = kwargs.get('nome', 'usuario')
#     saudacao = kwargs.get('saudacao', 'olá')
#     print(f'{saudacao}, {nome}') 

# cumprimento(saudacao='bom dia', nome='maria')

# def greadins(**kwargs):
#     cumprimento = kwargs.get('saudacao', 'good night')
#     nome = kwargs.get('pessoa', 'usuario')
#     print(f'{cumprimento}, {nome}')

# greadins(saudacao='boa noite', pessoa='max')

# def greeting(name, **kwargs):
#     if 'message' in kwargs:
#         print(f'{kwargs['message']}, {name}')
#     else:
#         print(f'Hi! {name}')


# greeting('Michael')
# greeting('Max', message='GOD blesse you my friend')

# def login(user,**kwargs):
#     stats = kwargs.get('stats')
#     if stats is True:
#         print(f'usuario {user} logado')
#     elif stats is False:
#         print(f'usuario {user} negado')
#     else:
#         print(f'stats de {user} desconhecido')

# login('michael', stats=True)
# login('max', stas=False)
# login('emanuel')

# def ficha_aluno(nome, **kwargs):
#     curso = kwargs.get('curso', 'tipo curso')
#     nota = kwargs.get('nota', float )
#     cidade = kwargs.get('cidade', 'cidade_nome')
#     if curso and nota and cidade and kwargs:
#         print(f'{nome} do curso {kwargs['curso']}, mora em {kwargs['cidade']} e sua nota foi {kwargs['nota']}')
#     else:
#         print(f'ola {nome}')

# ficha_aluno('Michael', curso='Python', nota=10, cidade='Maceio')
# ficha_aluno('michael')

def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(chave, valor)

minha_funcao('curriculo', 'desenvolvedor', nome='michael', idade=25)