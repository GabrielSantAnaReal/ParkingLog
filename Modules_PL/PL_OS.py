"""
Este módulo serve para identificar qual o sistema operacional do usuário
e com base nessa informação, verifica se é o primeiro acesso do usuário.
Para isso, verifica se existe um arquivo que diz em qual diretório estão
as "logs" (ou registros) de dias anteriores.
Em caso negativo, a pasta é criado de acordo com a instrução do usuário
e então volta-se ao programa principal
"""

import platform
import os
from Modules_PL import PL_pathfile
from time import sleep


firstaccess_msg1 = 'Identificamos que este é o seu primeiro acesso!'
firstaccess_msg2 = 'Por favor, selecione o local onde as logs ficarão salvas!'


def path_OS():
    os_user = platform.system() #Detecta o sistema operacional
    
    if os_user == 'Linux':
        username_OS_exp = os.path.expanduser('~')
        #Extrai o nome de usuário e seu diretório /home
        
        path_logdir = username_OS_exp + '/.parkinglog'
        if not os.path.exists(path_logdir):
            os.makedirs(path_logdir)
        os.chdir(path_logdir) #Muda o diretório para a pasta do arquivo de registro
        if not PL_pathfile.existfile_dir('PLdirlogs.txt'):
            print()
            PL_pathfile.createfile_dir('PLdirlogs.txt')
            print(firstaccess_msg1.center(60))
            print(firstaccess_msg2.center(60))
            sleep(2)
            filepath_user = PL_pathfile.firstaccess_linux()
            #Ativa módulo que busca as pastas e mostra para o usuário selecionar

            filepath_to_write = open(username_OS_exp + '/.parkinglog/PLdirlogs.txt', 'at')
            filepath_to_write.write(filepath_user)
            filepath_to_write.close()
            print()
        filedir_var = PL_pathfile.readfile_dir(username_OS_exp + '/.parkinglog/PLdirlogs.txt')
        filedir_final = filedir_var.replace('\n','')
        os.chdir(filedir_final)
    
    elif os_user == 'Windows':
        print()
        username_OS_win = 'C:/Users/' + os.getlogin() + '/Documents'
        #Junta o nome de usuário com o caminho para o respectivo diretório de documentos

        pathtolog_dir = username_OS_win + '/.parkinglog'
        #Junta o camihno com a pasta "/.parkinglog"
        
        if not os.path.exists(pathtolog_dir):
            os.makedirs(pathtolog_dir)
        os.chdir(pathtolog_dir) #Muda o diretório para a pasta do arquivo de registro
        if not PL_pathfile.existfile_dir('PLdirlogs.txt'):
            print()
            PL_pathfile.createfile_dir('PLdirlogs.txt')
            print(firstaccess_msg1.center(60))
            print(firstaccess_msg2.center(60))
            sleep(2)
            filepath_dir = PL_pathfile.firstaccess_windows()
            #Ativa módulo que busca as pastas e mostra para o usuário selecionar

            filepath_write = open(username_OS_win + '/.parkinglog/PLdirlogs.txt', 'at')
            filepath_write.write(filepath_dir)
            filepath_write.close()
            print()
        file_dir = PL_pathfile.readfile_dir(username_OS_win + '/.parkinglog/PLdirlogs.txt')
        file_dir_final = file_dir.replace('\n','')
        os.chdir(file_dir_final)
    
    else:
        print('OS não suportado')

