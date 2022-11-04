"""
Módulo com funções previamente configuradas para formatar texto que será exibido
nos menus, para economizar código e melhorar a leitura do programa principal.
"""

def ui_lines(n=40):
    print('-'*n)


def ui_text(txt, n=40):
    print(txt.center(n))


def ui_menu(txt, n=40):
    ui_lines(n)
    ui_text(txt,n)
    ui_lines(n)
    print('''Opções:
        1 - Cadastrar entrada veículos
        2 - Registrar saída de veículos
        3 - Ver cadastros do dia
        4 - Ver cadastros de outro dia
        5 - Apagar cadastros
        6 - Sair do sistema''')
    print('-'*n)


def ui_options(txt, n=40):
    ui_lines(n)
    ui_text(txt.center(n))
    ui_lines(n)
