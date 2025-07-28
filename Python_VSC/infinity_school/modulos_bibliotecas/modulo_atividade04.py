from random import randint

'''Desenvolva um jogo de adivinhação em que o programa
escolhe um número aleatório e desafia o jogador a
adivinhá-lo. Forneça dicas ao jogador, indicando se o
número é maior ou menor do que a adivinhação atual.'''

            


def jogo_da_adivinhação():      
        
        jogo_escolhendo_o_numero = randint(1, 10)

        while True:
            print(40 * '-=')
            try: 

                qual_numero_vc_quer = int(input('digite o numero entre(1 até 10) para adivinhar: '))

                if qual_numero_vc_quer > 10:
                    print('tente novamente um numero de 1 ate 10')      
                                                            
                elif jogo_escolhendo_o_numero == qual_numero_vc_quer:
                    print(f'parabens voçe ganhou!!!, numero foi: {jogo_escolhendo_o_numero} e seu palpite foi:{qual_numero_vc_quer}')

                    break
                elif qual_numero_vc_quer > jogo_escolhendo_o_numero:
                    print('ERROU, tente um numero menor na proxima tentativa.')

                else:
                    print('ERROU, tente um numero maior na proxima tentativa')

            except ValueError:
                print('tente usar um numero')
                                                        
             

           


