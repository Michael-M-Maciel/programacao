import math

def quadrado(lado_do_quadrado):
    perimetro = 4 * lado_do_quadrado
    area = lado_do_quadrado ** 2
    return f'a área do quadrado é = {area:.2f} e o perímetro ={perimetro:.2f}'


def retangulo(base_ret, altura_ret):
    area = base_ret * altura_ret
    perimetro = 2 * (base_ret + altura_ret)
    return f'a área do retângulo é: {area:.2f} e o perimetro: {perimetro:.2f}'


def circulo(raio_circulo):
    area = math.pi * (raio_circulo ** 2)
    perimetro = 2 * math.pi * raio_circulo
    return f' a área do circulo é: {area:.2f} e o perímetro é: {perimetro:.2f}'

    
def calculo_area_e_perimetro():
    while True:
        print(40* '-=')
        opcao =input('definição de áreae perimetro: 1-quadrado, 2-retângulo, 3-circulo e 4-sair: ')
        
        if opcao =='4':
            break

        elif opcao =='1':
            lado = float(input('qual o lado do quadrado: '))            
            print(quadrado(lado))

        elif opcao =='2':
            base = float(input('qual a base do retângulo: '))
            altura = float(input('qual a altura do retângulo: '))
            print(retangulo(base, altura))

        elif opcao =='3':
            raio = float(input('digite o raio do circulo: '))
            print(circulo(raio))
        else:
            print('opção invalida, tente novamente')
