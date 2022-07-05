from MAPA.lib.interface import *
from time import sleep
from MAPA.lib.functions import *

def main():
    books = []
    while True:
        answer = menu(['Inserir um novo cadastro', 'Mostrar todos os cadastros', 'Encerrar'])
        if answer == 1:
            header('NOVO CADASTRO')
            insert(books)
        elif answer == 2:
            header('TODOS OS CADASTROS')
            show(books)
        elif answer == 3:
            header('Saindo do sistema... Até logo!')
            sleep(3)
            break
        else:
            print('\n\033[31mErro! Digite uma opção válida!\033[m\n')
        sleep(1)
main()