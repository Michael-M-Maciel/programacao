# lista = [1, 1, 2, 2, 3, 4,]

# lista_2 = set(lista)
# lista_2.intersection
# lista_3 = list(lista_2)

# print(lista)
# print(lista_3)


lista = [1, 1, 2, 2, 3]
lista_b = [1, 2, 3, 4, 5, 6]


set_lista = set(lista) # trasnformando  lista em set, pois não aceita repetição
set_lista_b = set(lista_b)

new_listab =(list(set_lista_b)) # transformando o set em  lista
new_lista = (list(set_lista))


print(f'lista sem duplicata {new_lista}')   
print(f'lista completa {lista_b}')

