"""
Módulo equivalente a opção 4 do menu principal, mas foi colocado em módulo 
à parte para deixar o código do programa principal mais limpo.
"""

import Modules_PL.PL_register as Module_REGISTER
from time import sleep
import os


def vercadastros():
    print('Dias cadastrados:')
    for x in os.listdir():
        if x.endswith(".txt"):
            dayfile = x[6:8] + '/' + x[4:6] + '/' + x[0:4]
            print(dayfile.replace('.txt',''))
    print()
    sleep(0.3)

    while  True:
        print('Para sair, digite SAIR')
        otherday = str(input('Digite o dia desejado (dd/mm/aaaa): ')).replace('/', '')
        if otherday.upper() == 'SAIR':
            break
        else:
            filename_otherday = otherday[4:8] + otherday[2:4] + otherday[0:2] + '.txt'
            print()
            Module_REGISTER.arquivo_ler(filename_otherday)
            pressenter = str(input('Pressione ENTER para voltar ao menu'))
            print()
