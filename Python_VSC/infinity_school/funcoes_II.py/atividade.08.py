# def calculo(x, y, operador):
#     operacao = {
#         '+': lambda x, y: x + y,
#         '+': lambda x, y: x - y,
#         '+': lambda x, y: x * y,
#         '+': lambda x, y: x / y  if y != 0  else 'erro de divisao por zero'
#     }
#     if operador in operacao:
#         return operacao[operador](x, y)
    

def calculadora():
    def calculo(x, y, operador):
        operacao = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y  if y != 0  else 'erro de divisao por zero'
        }
        if operador in operacao:
            return operacao[operador](x, y)

    while True:    
        print(20 * '*','CALCULADORA',20 * '*')

        num1 = float(input('valor do primeiro numero: '))
        num2 = float(input('valor do primeiro numero: '))

        print('Selecione a operação: [+] Somar, [-] subtrair, [*] multiplicar [/] dividir e [s]air: ')
        opcao = input('qual será a opção: ')
        if opcao =='s':
            print('FIM')
            break
        elif opcao =='+':
            print(calculo(num1,num2,'+'))

        elif opcao =='-':
            print(calculo(num1, num2,'-'))

        elif opcao =='*':
             print(calculo(num1, num2,'*'))

        elif opcao =='/':
           print(calculo(num1, num2,'/'))

calculadora()

    
      
        

