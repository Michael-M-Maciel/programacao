'''Você possui dados de vendas trimestrais de uma
empresa em uma lista. Cada trimestre é representado
como uma lista de números, onde cada número
representa o valor de vendas de um mês (janeiro a
março, abril a junho, julho a setembro e outubro a
dezembro).
Você deve realizar as seguintes tarefas:
Calcule a média de vendas por trimestre.


parte 2:
Encontre o trimestre com a maior soma de vendas.
Encontre o trimestre com a menor soma de vendas.
Calcule o total de vendas no ano inteiro.
- Construa seus dados fictícios 
'''
primeiro_semestre = []

lista_anual = [

    [10, 20, 30],#(Jan, Fev, Mar)
    [40, 50, 60],#(Abr, Mai, Jun)
    [70, 80, 90],#(Jul, Ago, Set)
    [100, 110, 120]#(Out, Nov, Dez)

]


lista = []
def total_vendas(lista):
    for c in lista:
        



def media_semestre(lista):
    contador = 1
    for c in lista:
        media = sum(c) / len(c)
        print(f' a media do trimetre {contador}: foi: {media}')
        contador +=1
        

media_semestre(lista_anual)
total_vendas(lista_anual)



    
