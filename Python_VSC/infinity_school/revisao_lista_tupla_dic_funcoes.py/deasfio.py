'''DESAFIO PRÁTICO

Analise de Produção anual

Você tem um conjunto de dados que contém informações sobre a
produção anual de diferentes culturas em diversas fazendas ao

longo de vários anos. O objetivo é realizar

uma análise simples desses dados usando apenas as funções

agregadoras.

Tarefas: Encontre o ano em que a produção total foi máxima e o
ano em que foi mínima. Identifique a cultura que teve a maior
produção total e a cultura com a menor produção total ao longo
dos anos. Encontre a fazenda que obteve a produção máxima em
um determinado ano e a fazenda com a produção mínima no
mesmo ano.

- Construa seus próprios dados fictícios.'''

# Lista de dicionários contendo os dados de produção anual.
# Vamos supor que a 'producao' está em toneladas.
dados_producao = [
    # --- Dados de 2023 ---
    {'ano': 2023, 'fazenda': 'Fazenda Sol Nascente', 'cultura': 'Soja', 'producao': 12000},
    {'ano': 2023, 'fazenda': 'Fazenda Sol Nascente', 'cultura': 'Milho', 'producao': 8000},
    {'ano': 2023, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Soja', 'producao': 15000},
    {'ano': 2023, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Café', 'producao': 4000},
    # --- Dados de 2024 ---
    {'ano': 2024, 'fazenda': 'Fazenda Sol Nascente', 'cultura': 'Soja', 'producao': 11000},
    {'ano': 2024, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Soja', 'producao': 16000},
    {'ano': 2024, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Café', 'producao': 3500}, # <-- Produção bem baixa
    # --- Dados de 2025 ---
    {'ano': 2025, 'fazenda': 'Fazenda Sol Nascente', 'cultura': 'Milho', 'producao': 9500},
    {'ano': 2025, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Soja', 'producao': 18000}, # <-- Produção bem alta
    {'ano': 2025, 'fazenda': 'Fazenda Terra Forte', 'cultura': 'Café', 'producao': 4200},
]


#1. Análise por Ano:
#Qual foi o ano com a maior soma de produção (juntando todas as fazendas e culturas)?
#Qual foi o ano com a menor soma de produção?
#Identificar a cultura com maior produção total e a cultura com menor produção total."
#ncontre a fazenda com maior produção em um determinado ano
#Encontre a fazenda com menor produção no mesmo ano





lista_anos = [] # lista para receber os anos dos dados
dicionario_ano_valor = {} # criamos dicionadrio para receber ano: soma produção (por ano)
lista_cultura =[]
dicionario_cultura = {}


def culturas_maior_menor():
    menor_valor = None
    maior_valor = None
    nome_maior = ''
    nome_menor = ''

    for c, valor in dicionario_cultura.items():
        if  maior_valor == None or valor > maior_valor:
            maior_valor = valor
            nome_maior = c

    for j, dados in dicionario_cultura.items():
        if menor_valor == None or dados < menor_valor:
            menor_valor = dados
            nome_menor = j
    print(f'A cultura de {nome_maior} foi aque teve maior prododução: {maior_valor} toneladas')
    print(f'A cultura de {nome_menor} foi aque teve menor prododução: {menor_valor} toneladas')

    

def culturas():
    for cultura in dados_producao:
        if cultura['cultura'] not in lista_cultura:
            lista_cultura.append(cultura['cultura'])
    #print(lista_cultura)

def somando_culturas():
    for c in lista_cultura:
        soma = 0
        for j in dados_producao:
            if j['cultura'] == c:
                soma += j['producao']
        dicionario_cultura[c] = soma
    print(f'produção tota de cultura foi {dicionario_cultura}')

    

def listando_anos():
    for c in dados_producao:
        if c['ano'] not in lista_anos:
            lista_anos.append(c['ano'])
    #print(lista_anos)


def melhor_pior_producao():
    for ano  in lista_anos:
        soma = 0
        for item in dados_producao:
            if item['ano'] == ano:
                soma += item['producao']
                dicionario_ano_valor[ano] = soma
    #print(dicionario_ano_valor)

    maior = None
    ano_vencedor = None

    for  vencedor  in dicionario_ano_valor:
        if maior == None or dicionario_ano_valor[vencedor] > maior:
            maior = dicionario_ano_valor[vencedor]
            ano_vencedor = vencedor
    print(f'O ano {ano_vencedor} teve a melhor produção: {maior}- Toneladas')

    menor = None
    pior_ano = None

    for perdedor in dicionario_ano_valor:
        if menor == None or dicionario_ano_valor[perdedor] < menor:
            menor = dicionario_ano_valor[perdedor]
            pior_ano = perdedor
    print(f'O ano {pior_ano} teve a menor produção: {menor}- Toneladas')



listando_anos()
print(' ')
melhor_pior_producao()
print(' ')
culturas()
print(' ')
somando_culturas()
print(' ')
culturas_maior_menor()
print(' ')
