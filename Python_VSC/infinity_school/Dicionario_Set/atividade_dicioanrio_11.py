dicionario = {'nome': 'michael',
              'cidade': 'marrocos',
              'faculdade': 'unifg'}

checar = ['nome', 'profissão']
tudo_no_dicionario = True


for c in checar:
    print(f'checando a chave {c}')
    if c not in dicionario:
        print(f'a chave {c}, não aparece do dicionario')
        tudo_no_dicionario = False
        break

print('\n conclusão')
if tudo_no_dicionario == True:
    print('tudo estar no dicionario')
else:
    print('pelo menos uma chave não estar no dicionario')
