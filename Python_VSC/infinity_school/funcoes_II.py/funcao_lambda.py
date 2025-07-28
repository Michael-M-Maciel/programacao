# dobrar = lambda x, y: x + y

# print(dobrar(2, 5))




# lista_de_compras = [("maçã", 5), ("banana", 2), ("laranja", 9), ("uva", 1)]
# print(sorted(lista_de_compras))




# lista_de_compras = [("maçã", 5), ("banana", 2), ("laranja", 9), ("uva", 1)]

# Usando uma lambda como a 'chave' de ordenação
# ordenado_por_quantidade = sorted(lista_de_compras, key=lambda item: item[1])  # o sorte() organiza a lista em ordem porem o lamba organiza pelo indice no caso [1] os numeros


# par_impar = lambda x : 'par' if x % 2 == 0 else 'impar' 
# print(par_impar(2))
# print(par_impar(3))

# validando_usuario = lambda usuario: 'usuario não definido' if usuario=='' else('usuario nao pode ter menos de 4 digitos'if len(usuario) <4 else ' usuario definido com sucesso')
# print(validando_usuario('michael'))
# print(validando_usuario('max'))
# print(validando_usuario(''))

# ultimo = lambda nome: nome[-1] #seleciona a ultima letra da palavra
# print(ultimo('michael'))


# multiplicar = lambda x: x * 10
# print(multiplicar(5))

# maior_que_cem = lambda x: 'menor que 100' if x <= 99  else 'maior ou igual 100'
# print(maior_que_cem(20))
# print(maior_que_cem(100))

lista = [1, 2, 3, 4, 5]
dobrar_valor =list(map(lambda x : x * 2, lista))
print(dobrar_valor)