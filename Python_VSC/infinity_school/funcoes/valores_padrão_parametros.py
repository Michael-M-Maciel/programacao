# def soma(x, y, z=0):
#     if z:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)

# soma(1, 2, 3)

# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)

        
# soma(100, 200)
# soma(1, 2)
# soma(1, 2, 8) # nesse cazo z recebe valor então não é nulo e se executa o if


# def apresentacao():
#     print('meu nome é Michael')
#     print('Estou aprendendo funções em Pyhton!')

# apresentacao()

#argumentos nomenais
def descrever_pet(tipo_animal, nome_do_animal):
    print(f'eu tenho {tipo_animal}')
    print(f'o nome dele é {nome_do_animal}')

descrever_pet(tipo_animal='cachorro', nome_do_animal='pluto')
descrever_pet(nome_do_animal='pluto', tipo_animal='cachorro')
print('---')
descrever_pet('papagaio','xuxa')