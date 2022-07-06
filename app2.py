import random
import string


class PassGen:
    @staticmethod
    def generate(length):
        symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'
        password = ''.join(random.choices(symbols, k=length))
        return password


def main():
    print('--- Программа для генерации паролей ---')
    try:
        pass_length = abs(int(input('Длинна пароля: ')))
    except ValueError as e:
        print(e)
        pass_length = 0

    password = PassGen.generate(pass_length)
    print(password)
    print('--- FINISH ---')


if __name__ == '__main__':
    main()
