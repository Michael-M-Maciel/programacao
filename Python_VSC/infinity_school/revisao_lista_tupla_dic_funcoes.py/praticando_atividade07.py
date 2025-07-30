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

lista_anual = [

    [50, 20, 30],#(Jan, Fev, Mar)
    [70, 80, 90],#(Abr, Mai, Jun)
    [10, 20, 30],#(Jul, Ago, Set)
    [30, 40, 50]#(Out, Nov, Dez)

]

lista_soma_cada_trimestre = [] #criando lista para receber a soma de cada trimestre

#função calculando a média dos trimestres:
def media_trimestres(lista_do_ano):

    for indice, valor_trimestre in enumerate(lista_do_ano, start=1): # usando método (enumerate), me retorna índice em uma variavel , e percorre a lista usando outra variável.
        print(f'{indice}º trimestre teve média de: {sum(valor_trimestre) / len(valor_trimestre):.2f}-R$') # saída


# função para mostrar o lucro do ano
def vendas_do_ano(lucro_do_ano):
    for lucro in lucro_do_ano: # percorre cada indice da lista(lista_anual).
        lista_soma_cada_trimestre.append(sum(lucro))  # adiciona a soma de cada indice da lista(lista_anual) dentro da lista(total_cada_trimestre) da noss função.
    print(f'lucro total do ano foi de: {sum(lista_soma_cada_trimestre):.2f}-R$') # formatamos o print com a soma dos valores totais de cada trimestre que colocamos dentro da lista da nossa função



# função para achar trimestre que mais vendeu     
def trimestre_com_maior_venda(mais_vendeu):

    tri_melhor_valor = 0 #criamos uma variavel com valor 0, para no for comparar com os valor da lista que possui a soma dos semestres, caso o valor seja maior, nossa variavel recebe o novo valor que é maior que 0 e a comparação segue e sempre que houver um valor maior a variavel recebe um novo valor maior
    numero_trimestre = 0 # valor do nosso contador é 0 e vai receber o valor  da variavel contadora de indice(= trimestre) usada com enumerate.
    for trimestre ,maior_venda in enumerate(mais_vendeu, start= 1): #métoddo (enumerate) para obter indice estabelico para cada valor iniciado por 1= (start=1), sendo assim (trimestre = numero_trimestre) e trimestre de maior valor =(maior_venda = tri_melhor_valor)
        if maior_venda > tri_melhor_valor:
            tri_melhor_valor = maior_venda         
            numero_trimestre = trimestre
    print(f'O {numero_trimestre}º trimestre teve o maior lucro: {tri_melhor_valor:.2f}-R$') # saida

 

# função paraa achar o trimestre que menos vendeu
def trimestre_com_menor_venda(menos_vendeu):# mesma logica da função  trimestre_com_maior venda
    tri_menor_valor = menos_vendeu[0]
    numero_trimestre = 0

    for trimestre, menor_venda in enumerate(menos_vendeu, start= 1):
        if menor_venda < tri_menor_valor:
            tri_menor_valor = menor_venda
            numero_trimestre = trimestre
    print(f'O {numero_trimestre}º trimestre teve o menor lucro: {tri_menor_valor:.2f}-R$')
            

#saida de casa função   
media_trimestres(lista_do_ano = lista_anual)
vendas_do_ano(lucro_do_ano = lista_anual)
trimestre_com_maior_venda(mais_vendeu = lista_soma_cada_trimestre)
trimestre_com_menor_venda(menos_vendeu = lista_soma_cada_trimestre)
