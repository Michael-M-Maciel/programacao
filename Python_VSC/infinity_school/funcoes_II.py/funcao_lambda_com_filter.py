# numeros = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)


# numeros = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x % 2 == 1, numeros)) # retorna tudo que for verdadeiro
# print(pares)



# nomes = ['ana', 'maria', 'joao', 'max', 'aline']
# grande = list(filter(lambda nomes : len(nomes) >= 5 , nomes))
# print(grande)


#Crie uma lista com os números de 1 a 20.
#  Use filter() e lambda para manter apenas os múltiplos de 3.
# numeros =[1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
# multiplos_3 = list(filter(lambda x: x % 3 ==0, numeros )) 
# print(multiplos_3)


#Dada a lista ['michael', 'ana', 'maria', 'zé', 'joana'],
#  use filter() para manter somente os nomes com mais de 4 letras.
# lista_nomes = ['michael', 'ana', 'maria', 'zé', 'joana']
# so_grandes = list(filter(lambda nome: len(nome) > 4, lista_nomes))
# print(so_grandes)


#Dada a lista [True, False, True, True, False],
#  use filter() para manter apenas os valores True.
# lista = [True, False, True, True, False]
# lista_true = list(filter(lambda listando: listando, lista)) #Dica: no Python, não é necessário fazer == True.
# print(lista_true)



#Exercício 4 (desafio):
#Dada uma lista de temperaturas em graus Celsius: [10, 22, 35, 18, 40, 5],
#  filtre apenas as temperaturas acima de 30 graus.
lista_celsius = [10, 22, 35, 18, 40, 5]
thirty_graus = list(filter(lambda lista_c: lista_c > 30, lista_celsius ))
print(thirty_graus)