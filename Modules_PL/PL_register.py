"""
Módulo responsável pela verificação dos arquivos de registro, além das funções
de leitura, gravação e criação dos respectivos arquivos.
"""

from datetime import datetime
from datetime import timedelta
import Modules_PL.PL_date
#import PL_date #usado para teste


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


def arquivo_ler(filename):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        for linha in filetxt:
            dadovehicle = linha.split(';')
            dadovehicle[1] = dadovehicle[1].replace('\n', '')
            print(f'{dadovehicle[0]}/{dadovehicle[4]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}\n')
            #TO-DO: separar data e hora, e calcular tempo que ficou dentro do estacionamento
    #finally:
        filetxt.close()


 #criar variantes de arquivo_ler para:
 #ler somente entradas
 #ler somente saídas
 #depois, vincular ao menu principal!


def reg_entrada(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
    dateandtime=Modules_PL.PL_date.registerdatetime()):
#def reg_entrada(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
#    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
#    dateandtime=PL_date.registerdatetime()): #usado para teste
    plate.upper()
    brand = str(input('Marca do veículo: '))
    brand_upper = brand.upper()
    model = str(input('Modelo: '))
    model_upper = model.upper()
    color = str(input('Cor: ')).upper()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'ENTRADA;{plate};{brand_upper}/{model_upper};{color};{dateandtime}\n')


def reg_saida(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
    dateandtime=Modules_PL.PL_date.registerdatetime()):
#def reg_saida(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
#    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
#    dateandtime=PL_date.registerdatetime()): #usado para teste
    plate.upper()
    brand = str(input('Marca do veículo: '))
    brand_upper = brand.upper()
    model = str(input('Modelo: '))
    model_upper = model.upper()
    color = str(input('Cor: ')).upper()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'SAIDA;{plate};{brand_upper}/{model_upper};{color};{dateandtime}\n')


#Terminar (diminuir?)
def readplate(filename, plate, exittime):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!') #retirar?
    else:
        for linha in filetxt:
            dadovehicle = linha.split(';')
            if dadovehicle[0] == 'ENTRADA':
                if dadovehicle[1] == plate:
                    entracedatetime = dadovehicle[4].replace('\n', '')
                    entracetime_datetime = datetime.strptime(entracedatetime, "%H:%M:%S-%d/%m/%Y")
                    #print(entracetime_datetime) #teste
                    exittime_datetime = datetime.strptime(exittime, "%H:%M:%S-%d/%m/%Y")
                    diftime = exittime_datetime - entracetime_datetime
                    print(f'Tempo estacionado: {diftime} (hh:mm:ss)') #tempo que ficou estacionado #TESTE
                    
                    #diftime_str = str(diftime)
                    #diftime_str = diftime_str.split(':')
                    #diftime_hour = int(diftime_str[0]) #Pega o campo da hora
                    #diftime_min = int(diftime_str[1]) #Pega o campo dos minutos
                    #Para usar em caso de cálculo de valores de estacionamento
                    ''' if diftime_hour == 0:
                        print('Valor por hora ?') #TERMINAR
                    elif diftime_hour > 0:
                        diftime_hour_value = diftime_hour * 10 #(Valor a ser cobrado por hora, por exemplo) #TESTE
                        print(diftime_hour_value) #TESTE '''
        filetxt.close()
        return diftime


def plateexist(filename, plate, exittime=Modules_PL.PL_date.registerdatetime()):
#def plateexist(filename, plate, exittime=PL_date.registerdatetime()):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        platestatus = False
        for linha in filetxt:
            dadovehicle = linha.split(';')
            if dadovehicle[0] == 'ENTRADA':
                if dadovehicle[1] == plate:
                    platestatus = True
                    readplate(filename,plate,exittime)
        if platestatus == False:
            print('Placa não encontrada!')
            optuser = str(input('Deseja registrar a saída assim mesmo? (Sim/Não): '))
            if optuser.lower().strip()[0] == 's':
                platestatus = True
            elif optuser.lower().strip()[0] == 'n':
                platestatus = False
    finally:
        filetxt.close()
        return platestatus


def eraseplate_openwrite(filename, plate, status): # EM DESENVOLVIMENTO
    teste = status + ';' + plate
    with open(filename, 'r') as epr: #ep stands for "eraseplate"
        lines = epr.readlines()
    with open(filename, 'w') as epw:
        for line in lines:
            if line.find(teste) == -1: #teste é uma varivável de teste
                epw.write(line)


def eraseplate(filename): # EM DESENVOLVIMENTO
    print('Função para apagar registro')
    erase_opt = str(input('Deseja apagar uma "Entrada" ou "Saída"?')).strip().upper()[0]
    if erase_opt == 'E':
        plate_opt = str(input('Placa para apagar entrada: '))
        #se tiver saída registrada, bloquear
        eraseplate_openwrite(filename, plate_opt, 'ENTRADA')
    elif erase_opt == 'S':
        plate_opt = str(input('Placa para apagar saída: '))
        #Só apagar entradas de até 10 minutos atrás! #TO-DO
        eraseplate_openwrite(filename, plate_opt, 'SAIDA')
    else:
        print('Digite opção válida!')


#funcionou testando dentro do módulo:
'''
if plateexist('20220901.txt', 'ABC1234', '20:40:00-06/09/2022') == True: #TESTE
    print('True')
else:
    print('False')
'''