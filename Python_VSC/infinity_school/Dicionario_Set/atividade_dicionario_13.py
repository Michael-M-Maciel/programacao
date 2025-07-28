aluno = []

while True:

    nome = input('qual o nome do aluno: ')

    if nome =='0':
        break

    idade = int(input('qual a idade do aluno: '))
    portugues = float(input('qual a nota de portugues: '))
    matematica = float(input('qual a nota de matematica: '))
    ciencias = float(input('qual a nota de ciencias: '))

    alunos = {
        'nome': nome,
        'idade': idade,
        'notas':(portugues, matematica, ciencias)

    }

    aluno.append(alunos)
    print(aluno)
melhor_aluno = None
melhor_media = None

for alunos in aluno:
    print('------------------')
    print(f'Nome: {alunos['nome']}')
    print(f'idade:{alunos['idade']}')
    print(f'nota de portugues: {alunos['notas'][0]}')
    print(f'nota de matematica {alunos['notas'][1]}')
    print(f'nota de ciencias  {alunos['notas'][2]}')

    media = sum(alunos['notas']) / len(alunos['notas'])
    print(f'a media do aluno foi {media}')

    if melhor_media is None or melhor_media < media:
        melhor_aluno = alunos['nome']
        melhor_media = media

print(f'o melhor aluno foi {melhor_aluno} com a média {melhor_media}')
