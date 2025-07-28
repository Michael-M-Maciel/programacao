print('Exercicio')

nome = input('digite seu nome: ')
idade = input('qual sua idade: ')   

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'sua nome invertido é {nome[::-1]} ')
    if ' ' in nome:
        print('seu nome tem espaço')
    else:
        print('seu nome não contem espaço')

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}') #primeira letra
    print(f'a ultima leta do seu nome é {nome[-1]}')  #ultima letra
else:
    print('voçê deixou  campos vazios')