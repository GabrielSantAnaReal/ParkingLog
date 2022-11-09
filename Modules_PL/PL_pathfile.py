"""
Módulo responsável por diversas funções relacionadas a crianção, leitura e
gravação de diversos arquivos. Neste módulo só são feitas as gravações e
leituras do arquivo de registro de diretório.
"""

import os

#Primeiro acesso Linux
def firstaccess_linux():
    dir_path = '/home'
    while True:
        print(f'Diretório atual: {dir_path}')
        filesdir = os.listdir(dir_path)
        for n in range (0, len(os.listdir(dir_path))):
            print(f'{n} - {filesdir[n]}')
        optstr = str(input('Qual diretório você deseja salvar? ("Pare" para parar): '))
        if optstr.isnumeric() == True:
            opt = int(optstr)
        if optstr.upper().strip() == 'PARE':
            break
        elif opt > len(os.listdir(dir_path))-1:
            print('Erro! Digite um número válido!')
        else:
            optint = int(opt)
            dir_path = dir_path + '/' + filesdir[optint]
            print(dir_path)
        print()
    return dir_path


#Primeiro acesso Windows
def firstaccess_windows():
    dir_path = 'C:/'
    while True:
        print(dir_path)
        filesdir = os.listdir(dir_path)
        for n in range (0, len(os.listdir(dir_path))):
            print(f'{n} - {filesdir[n]}')
        optstr = str(input('Qual diretório você deseja salvar? ("Pare" para parar): '))
        if optstr.isnumeric() == True:
            opt = int(optstr)
        if optstr.upper().strip() == 'PARE':
            break
        elif opt > len(os.listdir(dir_path))-1:
            print('Erro! Digite um número válido!')
        else:
            optint = int(opt)
            dir_path = dir_path + '/' + filesdir[optint]
            print(dir_path)
        print()
    return dir_path


#Funções de leitura, criação e gravação de arquivos
def existfile_dir(filepath): # Verifica se o arquivo de registro existe
    try:
        filedir = open(filepath, 'rt', encoding='UTF-8')
        filedir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile_dir(filepath): # Cria o arquivo de registro conforme solicitado
    try:
        filedir= open(filepath, 'wt+', encoding='UTF-8')
        filedir.close()
    except:
        print('Erro ao criar arquivo de registro!')
    '''else:
        print(f'Arquivo de registro [{filepath}] criado com sucesso!')''' #Manter?


def readfile_dir(filepath): # Lê o arquivo de registro
    file_count = 1
    try:
        filedir = open(filepath, 'rt', encoding='UTF-8')
    except:
        file_count = 0
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        if file_count == 1:
            for linha in filedir:
                return linha
        filedir.close()
