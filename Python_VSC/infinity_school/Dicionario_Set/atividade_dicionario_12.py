'''Crie um programa que simule um sistema de votação. O
programa deve permitir que os eleitores escolham entre
opções de eleitores e conte os votos para cada opção.
Use um dicionário para armazenar os resultados da

votação, onde as chaves são as opções e os valores são o
número de votos para cada opção. O programa deve
permitir que os eleitores votem, encerre a votação e exiba
os resultados finais. Use While True e pare o programa
somente se o usuário digitar o número 0 e exiba os

resultados finais.  '''




eleicao = {
    'flamengo':  0,
    'palmeiras': 0,
    'fluminense':0
}

while True:
    print('opções para votar')
    print('=================================')

    for c in eleicao:
        print(c)

    opcao = input('escolha o time qual vai votar ou 0 para sair: ').lower()   
    
    if opcao == '0':
        break
    elif opcao in eleicao:
        eleicao[opcao] += 1

for time, votos in eleicao.items():
    print(f'{time} teve {votos} votos')


