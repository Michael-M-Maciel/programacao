from functools import reduce

def maior_da_lista(lista):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lista)


nomes = ['eu', 'amo', 'Python','Java', 'Michael', 'Arisvaldo', 'Joséssauro']
print(maior_da_lista(nomes))

