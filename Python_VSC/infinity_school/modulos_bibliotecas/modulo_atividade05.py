

'''Desenvolva um programa que permita ao usuário
converter entre diferentes unidades de medida, como
metros para pés, quilogramas para libras, ou Celsius
para Fahrenheit. Use módulos que contenham funções
de conversão.'''

def metros_para_pes(valor_metros):
    conversao_pes = valor_metros * 3.28
    return f'{valor_metros} metros convertidos para pés são: {conversao_pes} pés'


def kilos_para_libra(kilograma):
    convertendo_para_libra = kilograma * 2.2046
    return f'{kilograma}Kg converitdo para libras é: {convertendo_para_libra:.2f} libras'

def graus_para_fahreneheit(graus_celsius):
    convertendo_para_f = (graus_celsius * 1.8) + 32
    return f'{graus_celsius} Cº convertido em Fahrenheit são: {convertendo_para_f} Fº'