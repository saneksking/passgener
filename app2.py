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
        while 1:
            printer.smart.echo('', show=True, char='*')
            lang = input('Какой язык вы хотите выбрать? rus or eng: ')
            if lang == 'rus' or lang == 'Rus' or lang == 'RUS':
                Menu.rus_menu()
                break
            elif lang == 'eng' or lang == 'Eng' or lang == 'ENG':
                Menu.eng_menu()
                break
            else:
                printer.smart.echo('Такого языка нет!', show=True, char='*')
                continue

    @staticmethod
    def rus_menu():
        while 1:
            try:
                printer.smart.echo('Программа для создания сложных паролей!', show=True, char='*')
                printer.smart.echo('От SaneksKing', show=True, char='*')
                printer.smart.echo('', show=True, char='*')
                menu = int(input('1: Сгенерировать пароль\n2: Сменить язык\n3: Выход\n: '))
                if menu == 1:
                    try:
                        printer.smart.echo('', show=True, char='*')
                        pass_length = abs(int(input('Длинна пароля: ')))
                        password = PassGen.generate(pass_length)
                        printer.smart.echo('', show=True, char='*')
                        print(password)
                        printer.smart.echo('', show=True, char='*')
                        printer.smart.echo('Пароль сгенерирован!', show=True, char='*')
                        printer.smart.echo('', show=True, char='*')
                        cont = input('Нажмите Enter для продолжения или -1 для выхода!: ')
                        printer.smart.echo('', show=True, char='*')
                        if cont == '-1':
                            break
                        else:
                            continue
                    except ValueError:
                        print('Вы ввели не число!')
                        continue
                elif menu == 2:
                    Menu.switch_lang()
                    printer.smart.echo('', show=True, char='*')
                    vib = input('Enter Для продолжения...')
                    if vib == '':
                        continue
                    else:
                        continue
                elif menu == 3:
                    break
                else:
                    printer.smart.echo('Неправильное число для выбора!', show=True, char='*')
                    continue

            except ValueError as e:
                printer.smart.echo(f'Ошибка {e}! Пожалуйста пытайтесь не допускать её!', show=True, char='*')
                continue

    @staticmethod
    def eng_menu():
        try:
            while 1:
                printer.smart.echo('Program for creating complex passwords!', show=True, char='*')
                printer.smart.echo('From SaneksKing', show=True, char='*')
                printer.smart.echo('', show=True, char='*')
                eng_menu = int(input('1: Generate password\n2: Change language\n3: Exit\n: '))
                if eng_menu == 1:
                    try:
                        printer.smart.echo('', show=True, char='*')
                        pass_length = abs(int(input('Password length: ')))
                        password = PassGen.generate(pass_length)
                        printer.smart.echo('', show=True, char='*')
                        print(password)
                        printer.smart.echo('', show=True, char='*')
                        printer.smart.echo('Password generated!', show=True, char='*')
                        printer.smart.echo('', show=True, char='*')
                        cont = input('Press Enter to continue or -1 to exit!: ')
                        printer.smart.echo('', show=True, char='*')
                        if cont == '-1':
                            break
                        else:
                            continue
                    except ValueError:
                        print('You didn\'t enter a number!')
                        continue
                elif eng_menu == 2:
                    Menu.switch_lang()
                    printer.smart.echo('', show=True, char='*')
                    vib = input('Enter To continue...')
                    if vib == '':
                        continue
                    else:
                        continue
                elif eng_menu == 3:
                    break
                else:
                    printer.smart.echo('You didn\'t enter a number!', show=True, char='*')
                    continue

        except ValueError as e:
            printer.smart.echo(f'Error {e}!Please try not to let it', show=True, char='*')


def main():
    pass


if __name__ == '__main__':
    main()
