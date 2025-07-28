nome = input('digite seu nome: ')
telefone = input('digite seu numero de contato: ')
email = input('digite seu e-mail de contato: ')


contato = {
    'nome': nome,
    'telefone': telefone,
    'email': email
}

for c in contato.items():
    print(c)


print(30 * '-=')
print(f'o nome adicionado é {contato['nome']}')
print(f'o telefone adicionado é {contato['telefone']}')
print(f'o e-mail adicionado é {contato['email']}')