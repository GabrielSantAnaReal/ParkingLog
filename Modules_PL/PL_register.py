"""
Módulo responsável pela verificação dos arquivos de registro, além das funções
de leitura, gravação e criação dos respectivos arquivos.
"""

from time import sleep
import Modules_PL.PL_date


# Verifica e cria arquivos
def arquivo_existe(filename):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
        filetxt.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivo_criar(filename):
    try:
        filetxt = open(filename, 'wt+', encoding='UTF-8')
        filetxt.close()
    except:
        print('Erro ao criar arquivo de registro!')
    else:
        print(f'Arquivo de registro [{filename}] criado com sucesso!')


###############################################################################
# Lê arquivos
def arquivo_ler(filename):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        for linha in filetxt:
            dadovehicle = linha.split(';')
            dadovehicle[1] = dadovehicle[1].replace('\n', '')
            print(f'{dadovehicle[0]}/{dadovehicle[5]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}/{dadovehicle[4]}\n')
        filetxt.close()


def arquivo_ler_entrada(filename):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        for linha in filetxt:
            dadovehicle = linha.split(';')
            dadovehicle[1] = dadovehicle[1].replace('\n', '')
            if dadovehicle[0] == 'ENTRADA':
                print(f'{dadovehicle[0]}/{dadovehicle[5]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}/{dadovehicle[4]}\n')
        filetxt.close()


def arquivo_ler_saida(filename):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        for linha in filetxt:
            dadovehicle = linha.split(';')
            dadovehicle[1] = dadovehicle[1].replace('\n', '')
            if dadovehicle[0] == 'SAIDA':
                print(f'{dadovehicle[0]}/{dadovehicle[5]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}/{dadovehicle[4]}\n')
        filetxt.close()


###############################################################################
# Registra entradas e saídas
def reg_entrada(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
    dateandtime='DESCONHECIDO'):
    plate = plate.upper() #Converte a placa digitada para CAPS LOCK
    brand = str(input('Marca do veículo: '))
    brand_upper = brand.upper()
    model = str(input('Modelo: '))
    model_upper = model.upper()
    color = str(input('Cor: ')).upper()
    dateandtime = Modules_PL.PL_date.registerdatetime()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'ENTRADA;{plate};{brand_upper};{model_upper};{color};{dateandtime}\n')


def reg_saida(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
    dateandtime='DESCONHECIDO'):
    plate = plate.upper()
    brand = str(input('Marca do veículo: '))
    brand_upper = brand.upper()
    model = str(input('Modelo: '))
    model_upper = model.upper()
    color = str(input('Cor: ')).upper()
    dateandtime=Modules_PL.PL_date.registerdatetime()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'SAIDA;{plate};{brand_upper};{model_upper};{color};{dateandtime}\n')


def reg_saida_reuse(filename, plate, brand, model, color, dateandtime):
    plate = plate.upper()
    brand_upper = brand.upper()
    model_upper = model.upper()
    color_upper = color.upper()
    dateandtime=Modules_PL.PL_date.registerdatetime()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'SAIDA;{plate};{brand_upper};{model_upper};{color_upper};{dateandtime}\n')


########
###############################################################################
