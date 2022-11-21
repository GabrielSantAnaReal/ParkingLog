"""
Programa principal, onde o usuário seleciona os menus e é encaminhados para
outros sub-menus conforme necessidade.
O código faz o seguinte passo a passo:
1) Configura como nome de arquivo de registro a data atual;
2) Verifica se existe arquivo de registro de diretório;
3) Dá as opções ao usuários e conforme selecionado, retorna a informação ou
o sub-menu necessário.
"""


import Modules_PL.PL_register as Module_REGISTER
import Modules_PL.PL_date as Module_DATE
import Modules_PL.PL_interface as Module_UI
import Modules_PL.PL_list as Module_LIST
import Modules_PL.PL_OS as Module_OS
from time import sleep

Module_OS.path_OS()

datefilename = Module_DATE.PLdate_filename()
#TO-DO: pegar data antes de cada execução
#filename = '20220901.txt' #teste, substituir por data do dia
filename = datefilename + '.txt'
if not Module_REGISTER.arquivo_existe(filename):
    Module_REGISTER.arquivo_criar(filename)

while True:
    Module_UI.ui_menu('Parking Log APLHA',40)
    opt = int(input('Digite a opção desejada: '))

    if opt == 1:
        # Registra entradas
        print()
        while True:
            Module_UI.ui_options('Cadastro de entrada de veículos',40)
            textplate = str(input('Digite a placa ("SAIR" para sair): '))
            if textplate.upper() == 'SAIR':
                break
            else:
                Module_REGISTER.reg_entrada(filename, textplate)
    
    elif opt == 2:
        # Registra saídas
        #TO-DO: Melhorar saídas: se a placa existir, sugerir preencher dados
        while True:
            print()
            Module_UI.ui_options('Registro de saída de veículos',40)
            textplate = str(input('Digite a placa ("SAIR" para sair): '))
            if textplate.upper() == 'SAIR':
                break
            else:
                if Module_REGISTER.plateexist(filename, textplate) == True:
                    
                    #NÃO ESTÁ FUNCIONANDO
                    exittime_now = Module_DATE.registerdatetime()
                    Module_REGISTER.readplate(filename, textplate, exittime_now)
                    
                else:
                    print('Registro de saída não foi feito!')
                    sleep(0.8)
    
    elif opt == 3:
        # Ver todos os cadastros do dia
        print()
        Module_REGISTER.arquivo_ler(filename)
        pressenter = str(input('Pressione ENTER para voltar ao menu'))
        print()

    elif opt == 4:
        # Ver somente entradas
        print()
        Module_REGISTER.arquivo_ler_entrada(filename)
        pressenter = str(input('Pressione ENTER para voltar ao menu'))
        print()

    elif opt == 5:
        # Ver somente saídas
        print()
        Module_REGISTER.arquivo_ler_saida(filename)
        pressenter = str(input('Pressione ENTER para voltar ao menu'))
        print()

    elif opt == 6:
        # Cadastros de outro dia
        print() 
        Module_LIST.vercadastros()

    elif opt == 7:
        # Apaga algum registro específico do dia
        print()
        print('ATENÇÃO: Esse menu apaga registros de forma permanente!')
        print('PROSSIGA COM CUIDADO!')
        sleep(1)
        print()
        Module_REGISTER.eraseplate(filename)
        print()

    elif opt == 8:
        print('Saindo...')
        break

    else:
        print('Opção inválida! Tente novamente!')
        sleep(1.1)
