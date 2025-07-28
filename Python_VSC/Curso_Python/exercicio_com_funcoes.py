# def multiplicar(*args):
#     total = 1
#     for c in args:
#         total *= c
#     return total
    

# multiplicando = multiplicar(1, 2, 3, 4, 5)
# print(multiplicando)
# print(1 * 2 * 3 * 4 * 5)




def paridades(a):
    if a % 2 == 0:
        return f'numero {a} é par'
    return f'numero {a} é impar'

print(paridades(1))
print(paridades(2))
print(paridades(3))
print(paridades(4))
print(paridades(5))
