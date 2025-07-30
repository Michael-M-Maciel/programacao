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
# primeiro_semestre = []

lista_anual = [

    [15, 20, 30],#(Jan, Fev, Mar)
    [70, 80, 90],#(Abr, Mai, Jun)
    [10, 20, 30],#(Jul, Ago, Set)
    [30, 40, 50]#(Out, Nov, Dez)

]



lista_maior_venda = []


def media_semestres(lista_ano):
    for indice, semestre in enumerate(lista_ano, start=1): # primeira variavel começa em 1 e vai ser nosso indice.
        print(f'media do {indice}º trimestre foi de {sum(semestre) / len(semestre):.2f}-R$')

         
    # for c in lista_anual:  ##OPÇÃO 2
    #     contador = 1
    #     print(f'media do {contador}º trimestre foi de: {sum(c) / len(c)}')
    #     contador += 1


def total_ano(listando_totol_ano):
    for soma in listando_totol_ano:
        lista_maior_venda.append(sum(soma)) # adiciona na lista a soma dos valor da lista pelo indice . ex soma dos valores da lista[0], lista[1] e etc...
        

def trimestre_mais_vendeu(lista_venda):
    maior = lista_venda[0] # atribuimos o primeir valor da lista(lista_maior_venda) a nossa variavel para iniciar a comparão de valores no if do for.
    trimestre_mais_vendeu = 1

    for indice, maior_valor in enumerate(lista_venda, start= 1): # usamos enumerate para usar indice como valor do nosso trimestre.
        if maior_valor > maior: # comparando os valores percorridos pelo for na lista.
            maior = maior_valor  # atribuindo novo valor em (maior) caso if seja verdadeiro
            trimestre_mais_vendeu = indice # indice é aumentado a cada repetição da verificação do for e vai ser o numemro do noss trimestre ao finalizar .
    print(f'O {trimestre_mais_vendeu}º trimestre teve melhor lucro: {maior:.2f}-R$')

    ##opcao 2:
    # trimestre_que_mais_vendeu = 0 # variavel que vai receber contador para descobrir o trimestre que mais vendeu.
    # maior_lucro = 0  # variavel que vai armazenar o maior  valor achado

    # for maior in lista_venda: # for que vai na lista (lista_maior_venda) que tem  a soma total de cada trimestre
    #     if maior > maior_lucro: # fazendo a comparação se o valor da lista que está sendo percorrido pele for com  a variavel(maior)é maior que a nossa variavel contadora(maior_lucro) que é 0
    #         maior_lucro = maior  # se maior > que maior lucro. (maior_lucro) deixa de ser 0 e vai armazenar o maior valor encontrado percorrrido na lista.
    #         trimestre_que_mais_vendeu += 1 # contador que vai ate aonde o valor vai ser o vencedor e vai ser nosse trimestre vencedor.
    # print(f'o {trimestre_que_mais_vendeu}º trimestre foi o que mais teve lucro: {maior_lucro} R$ nesse ano')
   

def trimestre_menos_vendeu(lista): # mesma logica da função trimestre_mais_vendeu
    menor = lista[0]
    trimestre_menos = 1

    for indice, menos in enumerate(lista, start=1):
        if menos < menor:
            menor = menos
            trimestre_menos = indice
    print(f'O {trimestre_menos}º trimestre teve o menor lucro: {menor:.2f}-R$')

   
media_semestres(lista_anual)
total_ano(lista_anual)
print(f'o lucro do ano foi de: {sum(lista_maior_venda):.2f}R$')
print(lista_maior_venda)
trimestre_mais_vendeu(lista_maior_venda)
trimestre_menos_vendeu(lista_maior_venda)

