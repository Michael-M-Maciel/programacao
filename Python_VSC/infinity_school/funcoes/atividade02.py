# def horario():
#     while True:
#         hora = float(input('diga o horario: '))
#         if hora == 25:
#             print('fim')
#             break
#         elif hora <= 11.59:
#             print(f'bom dia!!, são {hora}h da manhã')
#         elif hora <= 18.59:
#             print(f'boa tarde,são {hora}h da tarde')
#         elif hora <= 23.59:
#             print(f'boa noite, são {hora}h da noite')
#         else:
#             print('opção invalida tente novamente')

# horario()

def horario(hora):
    if hora < 12:
        return f' Bom dia!, são {hora}h da manhã'
    elif hora < 19:
        return f' boa tarde, são {hora}h da tarde'
    elif hora < 24:
        return f' boa noite, são {hora}h da noite'
    else:
        return ' opção invalida'
    
print(horario(5))
print(horario(12))
print(horario(19))
print(horario(25))
