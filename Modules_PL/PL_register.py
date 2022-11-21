"""
Módulo responsável pela verificação dos arquivos de registro, além das funções
de leitura, gravação e criação dos respectivos arquivos.
"""

from datetime import datetime
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
            print(f'{dadovehicle[0]}/{dadovehicle[4]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}\n')
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
                print(f'{dadovehicle[0]}/{dadovehicle[4]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}\n')
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
                print(f'{dadovehicle[0]}/{dadovehicle[4]}/{dadovehicle[1]}/{dadovehicle[2]}/{dadovehicle[3]}\n')
        filetxt.close()


###############################################################################
# Registra entradas e saídas
def reg_entrada(filename, plate='DESCONHECIDO', brand_upper='DESCONHECIDO',
    model_upper='DESCONHECIDO', color='DESCONHECIDO', 
    dateandtime='DESCONHECIDO'):
    plate = plate.upper()
    brand = str(input('Marca do veículo: '))
    brand_upper = brand.upper()
    model = str(input('Modelo: '))
    model_upper = model.upper()
    color = str(input('Cor: ')).upper()
    dateandtime = Modules_PL.PL_date.registerdatetime()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'ENTRADA;{plate};{brand_upper}/{model_upper};{color};{dateandtime}\n')


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
    filetxt.write(f'SAIDA;{plate};{brand_upper}/{model_upper};{color};{dateandtime}\n')


def reg_saida_reuse(filename, plate, brand, model, color, dateandtime):
    plate = plate.upper()
    brand_upper = brand.upper()
    model_upper = model.upper()
    color_upper = color.upper()
    dateandtime=Modules_PL.PL_date.registerdatetime()
    print()
    filetxt = open(filename, 'at')
    filetxt.write(f'SAIDA;{plate};{brand_upper}/{model_upper};{color_upper};{dateandtime}\n')


###############################################################################
# Mostra quanto tempo ficou estacionado
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
                    exittime_datetime = datetime.strptime(exittime, "%H:%M:%S-%d/%m/%Y")
                    diftime = exittime_datetime - entracetime_datetime
                    print(f'Tempo estacionado: {diftime} (hh:mm:ss)') #tempo que ficou estacionado
                    #Adicionar dados do veículo e sugerir reaproveitar

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
        #return diftime


###############################################################################
# Verifica se a placa já tem registro
def plateexist(filename, plate):
    try:
        filetxt = open(filename, 'rt', encoding='UTF-8')
    except:
        print('Erro ao ler o arquivo! Verifique se ele existe!')
    else:
        platestatus = False
        for linha in filetxt:
            dadovehicle = linha.split(';')
            if dadovehicle[0] == 'ENTRADA':
                if dadovehicle[1] == plate.upper():
                    platestatus = True
                    print()
                    print('Placa encontrada! As informações serão reaproveitadas!')
                    print(f'Placa: {dadovehicle[1]}, Marca/Modelo: {dadovehicle[2]}, Cor: {dadovehicle[3]}')
                    print('Se estiver tudo certo, pressione ENTER')
                    user_input = str(input('Se alguma informações estiver incorreta, digite "não": ')).upper().strip()
                    if user_input == 'N':
                        print('Registro manual das informações: ')
                        reg_saida(filename, plate)
                    else:
                        marca_modelo = dadovehicle[2].split('/')
                        reg_saida_reuse(filename, plate, marca_modelo[0], marca_modelo[1],
                        dadovehicle[3], Modules_PL.PL_date.registerdatetime())
                    
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


###############################################################################
# Apaga registro de alguma placa
def eraseplate_openwrite(filename, plate, status):
    try:
        info_vehicle = status + ';' + plate
        with open(filename, 'r') as epr: #ep stands for "eraseplate"
            lines = epr.readlines()
        with open(filename, 'w') as epw:
            for line in lines:
                if line.find(info_vehicle) == -1:
                    epw.write(line)
    except:
        print('Algo deu errado! Tente novamente!')


def eraseplate(filename):
    print('Função para apagar registro')
    erase_opt = str(input('Deseja apagar uma "Entrada" ou "Saída"? ("FIM" para parar): '))
    if erase_opt.strip().upper()[0] == 'E':
        plate_opt = str(input('Placa para apagar entrada: ')).upper().strip()
        #Se tiver saída registrada, bloquear
        eraseplate_openwrite(filename, plate_opt, 'ENTRADA')
    elif erase_opt.strip().upper()[0] == 'S':
        plate_opt = str(input('Placa para apagar saída: ')).upper().strip()
        #Só apagar entradas de até 10 minutos atrás! #TO-DO
        eraseplate_openwrite(filename, plate_opt, 'SAIDA')
    elif erase_opt.strip().upper()[0] == 'F':
        erase_opt = 'sair'
        return erase_opt
    else:
        print('Digite opção válida!')
