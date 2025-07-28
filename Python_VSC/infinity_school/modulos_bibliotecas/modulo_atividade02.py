'''Crie um módulo chamado manipulacao_strings que
contenha funções para realizar operações com strings,
como inverter uma string, contar o número de palavras

em uma string e verificar se uma string é um
palíndromo (lê-se igual de trás para frente). Crie
um programa principal que importe o módulo e use
essas funções com strings fornecidas pelo usuário.'''


def inventer_string(x):
    print (f'a palavra {x} invertida é: {x[::-1]}')



def contando(string):
    contandor = 0
    for c in string:
      contandor += 1
    print(f'a palavra {string}, tem {contandor} letras')



def palindromo():
    palavra_igual = input('vamos checar se a palavra digitade é um palíndromo: ').lower() .replace(' ','')
    palavra2 = palavra_igual[::-1]
    if palavra_igual == palavra2:
        print(f'é  um palíndromo: {palavra_igual} = {palavra2}')
    else:
        print(f'não é um palíndromo: {palavra_igual} = {palavra2}')



def manipulacao_strings():
    while True:
        print(30 * '-=')
        opcao = input('1- inverter string, 2-contador de palavras, 3-palíndromo e 4-sair: ')

        if opcao =='4':
            print('fim')
            break
        
        elif opcao == '1':
            palavra_invertida = input('digite a plavra que deve ser invertidade: ')
            inventer_string(palavra_invertida)

        elif opcao =='2':
            palavra_contar = input('deseje contar os numeros de letrar de qual palavra: ')
            contando(palavra_contar)

        elif opcao =='3':
            palindromo()

        else:
            print('opção invalida, tente novamente.')



