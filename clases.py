import random
import string
from smartprinter.printers import Printer
printer = Printer()


class PasswordGen:
    def __init__(self):
        self.symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'

    def RandomPass(self):
        while 1:
            try:
                printer.smart.echo('', show=True, char='*')
                x = ''.join(random.choices(self.symbols, k=int(input('Введите длинну пароля/Enter password length: '))))
                printer.smart.echo('', show=True, char='*')
                print(x)
                printer.smart.echo('', show=True, char='*')
            except ValueError:
                printer.smart.echo('', show=True, char='*')
                print('Вы ввели не число/You didn\'t enter a number!')
