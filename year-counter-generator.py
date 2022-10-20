import time
from datetime import datetime


def gera_ano():
    for ano in range(1, int(datetime.now().year) + 1):
        print(f'Estamos no ano {ano}')
    should_run_again()


def should_run_again():
    answer = input('Run again?(y/n) : ')
    if answer == 'y':
        gera_ano()
    if answer == 'n':
        print('Exiting Program now...Bye :)')


if __name__ == '__main__':
    gera_ano()