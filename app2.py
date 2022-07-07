import random
import string
from smartprinter.printers import Printer
printer = Printer()

class PassGen:
    @staticmethod
    def generate(length):
        symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'
        password = ''.join(random.choices(symbols, k=length))
        return password


class Menu:
    @staticmethod
    def switch_lang():
        try:
            lang = input('Какой язык вы хотите выбрать? rus or eng: ')
            if lang == 'rus' or lang == 'Rus' or lang == 'RUS':
                Menu.rus_menu()
            elif lang == 'eng' or lang == 'Eng' or lang == 'ENG':
                pass
    @staticmethod
    def rus_menu():
        try:
            while 1:
                printer.smart.echo('Программа для создания сложных паролей!', show=True, char='*')
                printer.smart.echo('От SaneksKing', show=True, char='*')
                printer.smart.echo('', show=True, char='*')
                menu = int(input('1: Сгенерировать пароль\n2: Сменить язык\n3: Выход\n: '))
                if menu == 1:
                    pass_length = abs(int(input('Длинна пароля: ')))
                    if pass_length:
                        password = PassGen.generate(pass_length)
                        print(password)
                        printer.smart.echo('Пароль сгенерирован!', show=True, char='*')
                        cont = input('Нажмите Enter для продолжения или -1 для выхода!: ')
                        if cont == '-1':
                            break
                        else:
                            continue
                    else:
                        print('Вы ввели не число!')
                        continue

                elif menu == 2:


def main():
    pass


if __name__ == '__main__':
    main()
