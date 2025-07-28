lista = []

# num =input("escreva um numero: ")
# for c in num:
#     if c =='(':
#         lista.append('(')
#     elif c ==')':
#         if len(lista) > 0:
#             lista.pop()
#         else:
#             lista.append(')')
#             break

# if len(lista) == 0:
#     print('expressao correta')
# else:
#     print('expresse errada')


num = input('digite o numero: ')
for c in num:
    if c =='(':
        lista.append('(')
    elif c ==')':
       if len(lista)> 0:
           lista.pop()
       else:
           lista.append(')')
           break
       
if len(lista) == 0:
    print("expressão correta")
else:
    print('expressao errado')


