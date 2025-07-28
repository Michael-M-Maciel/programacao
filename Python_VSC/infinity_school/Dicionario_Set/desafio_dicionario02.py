alunos = []

while True:
    nome = input('Digite o nome do aluno ou 0 para sair: ')

    if nome == '0':
        break

    idade = int(input('Digite a idade do aluno: '))
    matematica = float(input('Digite a nota de matemática: '))
    historia = float(input('Digite a nota de história: '))
    ciencias = float(input('Digite a nota de ciencias: '))

    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': (matematica, historia, ciencias)
    }
    alunos.append(aluno)   

melhor_aluno = None
melhor_media = None

for aluno in alunos:
    print( 30 *'-')
    print(f'Nome: {aluno['nome']}')
    print(f'Idade: {aluno['idade']}')
    print(f'Matemática: {aluno['notas'][0]}')
    print(f'História: {aluno['notas'][1]}')
    print(f'Ciências: {aluno['notas'][2]}')

    media = sum(aluno['notas'])/len(aluno['notas'])
    print(f'A média do aluno foi: {media:.2f}')

    if melhor_media is None or melhor_media < media:
        melhor_aluno = aluno['nome']
        melhor_media = media


print( 30* '**')
print(f'O melhor aluno foi {melhor_aluno} com a média {melhor_media:.2f}')


