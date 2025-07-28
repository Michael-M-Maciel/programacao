# while True:
#     try:
#         num = int(input('digite um numero inteiro: '))

#         if num % 2 == 0:
#             print('par')
#         else:
#             print('impar')       
            
#     except:
#         print('o valor que foi informado não foi um numero inteiro')   


# while True:
#     try:
#         horario = float(input('que horas são agora: '))

#         if horario <12:
#             print(f'bom dia sao: {horario} horas da manhã')
#         elif horario <18:
#             print(f'boa tarde são: {horario} horas da tadrde')
#         else:
#             print(f'boa noite são: {horario} horas da noite')
#     except:
#         print('digite um valor numerico')


nome = input('digite seu primeiro nome: ')

if len(nome) <= 4:
    print("seu nome é curto")
elif len(nome) <= 6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')

