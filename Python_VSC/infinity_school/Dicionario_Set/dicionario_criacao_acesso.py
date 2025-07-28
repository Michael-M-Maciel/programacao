contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3344-3871'},
    'melaine2@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'},
}


# nome = contatos['giovanna@gmail.com']['nome']
# print(nome)

for chave, valor in contatos.items():
    print(chave, valor)