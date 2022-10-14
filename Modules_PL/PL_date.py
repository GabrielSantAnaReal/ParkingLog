"""
Módulo responsável por pega data e hora atuais e formatar conforme necessidade.
Usado para o registro de entrada e/ou saída e para nomeação do arquivo de registro.
"""

import datetime


def registerdatetime(): # Pega a data e a hora atuais
    actualdate = datetime.date.today()
    actualtime = datetime.datetime.now()

    actualdate_string = actualdate.strftime("%d/%m/%Y")
    actualtime_string = actualtime.strftime("%H:%M:%S")
    dateandtime_string = (f'{actualtime_string}-{actualdate_string}')

    return dateandtime_string


def PLdate_filename():
    actualdate = datetime.date.today()
    actualdate_string = actualdate.strftime("%Y%m%d")
    return actualdate_string

