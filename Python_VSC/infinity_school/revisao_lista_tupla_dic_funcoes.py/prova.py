import os

'''[PYIA-A08]
 Importe o módulo 'os' e use a função 'listdir' para listar todos os arquivos e pastas presentes no diretório onde o script Python está sendo executado.
A função 'listdir' retornará uma lista contendo os nomes dos arquivos e pastas. Após obter essa lista, exiba cada item da lista individualmente na saída do console.'''

meus_documentos_pyhton = os.listdir()

print('meus documentos encontrados')
for documentos in meus_documentos_pyhton:
    print(documentos)

