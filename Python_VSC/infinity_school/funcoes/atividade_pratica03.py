'''ATIVIDADE PRÁTICA 3
Crie um programa que permita ao usuário converter temperaturas entre:
1) Celsius para Fahrenheit
2) Fahrenheit para Celsius
3) Celsius para Kelvin
O programa deve exibir um menu de opções, o usuário escolhe a conversão e informa a temperatura.
Funções obrigatórias:
- celsius para fahrenheit
- fahrenheit para celsius
- celsius para kelvin
(Opcional: criar uma função para exibir o menu e outra para validar escolha)'''

def temp_celcius_f(temp_c):
    return (temp_c * 1.8) + 32
   

def temp_fahrenheit_c(temp_f):
    return (temp_f - 32) / 1.8

def temp_celcius_k(temp_c):
    return temp_c + 273.15
    
def menu():
    print(10* '*','MENU',10*'*')
    print('[1] Temperatura Cº para Fº: ')
    print('[2] Temperatura Fº para Cº: ')
    print('[1] Temperatura Cº para Kº: ')
    opcao = input('escolha entre [1], [2] e [3]:')



