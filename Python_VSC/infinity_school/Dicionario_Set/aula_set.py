# meu_set = {'infity', 'School' }
# print(meu_set)
# print(type(meu_set))

# frutas = {'maçã', 10, True, 'jaca',  'copo', 'banana'}
# objeto = {'caneta', 'caderno', 'copo'}

# frutas.add('jaboticaba')
# frutas.update(objeto)
# print('maçã' in frutas)
# for c in frutas:
#     print(c)

# objeto.remove('caneta')
# print(objeto)
# objeto.discard('copo')
# print(objeto)

# print(frutas.intersection(objeto))
# frutas.intersection_update(objeto)
# print(frutas)
# print(frutas.union(objeto))

# frutas = set() # jeito de se criar um set vazio
# frutas.add('manga')
# frutas.add('goiaba')
# frutas.add('jaca')
# frutas.add('mamão')

# print(frutas)

# print('jaca' in frutas) # verifica de jaca esta dentro do set frutas 


# frutas_amarelas = {'banana', 'jaca', 'acerola', 'melão'}
# frutas_vermelhas = {'morango', 'acerola', 'framboesa',  'pitanga'}

#frutas_vermelhas.remove('acerola')
# print(frutas_vermelhas)

# frutas_vermelhas.intersection_update(frutas_amarelas)
# print(frutas_vermelhas)

# lista_01 = [1, 2, 2 , 3, 4]
# lista_02 = [2, 3, 3, 4, 5, 6]

# set_01 = set(lista_01)
# set_02 = set(lista_02)
# set_plus = set_01 | set_02
# print(set_plus)