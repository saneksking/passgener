import clases
from smartprinter.printers import Printer

printer = Printer
cls = clases.PasswordGen()

try:
    while 1:
        printer.smart.echo('Программа для создания сложных паролей!', show=True, char='*')
        printer.smart.echo('От SaneksKing', show=True, char='*')
        printer.smart.echo('', show=True, char='*')
        menu = int(input('1: Сгенерировать пароль\n2: Сменить язык\n3: Выход\n: '))
        if menu == 1:
            cls.RandomPass()
            printer.smart.echo('Пароль сгенерирован!', show=True, char='*')
            cont = input('Нажмите Enter для продолжения или -1 для выхода!: ')
            if cont == '-1':
                printer.smart.echo('Программа завершена!', show=True, char='*')
                break
            else:
                continue
        elif menu == 2:
            printer.smart.echo('Program for creating complex passwords!', show=True, char='*')
            printer.smart.echo('From SaneksKing', show=True, char='*')
            menu1 = int(input('1: Generate password\n2: Change language\n3: Exit\n: '))
            if menu1 == 1:
                printer.smart.echo('Password generated!', show=True, char='*')
                cont = input('Press Enter to continue or -1 to exit!: ')
                if cont == '-1':
                    printer.smart.echo('Program completed!', show=True, char='*')
                    break
                else:
                    continue
            elif menu1 == 2:
                continue
            elif menu1 == 3:
                printer.smart.echo('Program completed!', show=True, char='*')
        elif menu == 3:
            printer.smart.echo('Программа завершена!', show=True, char='*')
            break
except ValueError:
    printer.smart.echo('Вы ввели не число/You didn\'t enter a number!'
                       ' Программа завершилась/Program ended!', show=True, char='*')
