def password_check(func):
    """
    Функция проверяет правильность ввода пароля. При трех неправильных вводах функция завершает работу.
    При правильном вводе пароля секретные данные виводятся на экран.
    :param func:
    :return:
    """

    def wraper():
        count = 2
        while True:
            password = input('Введите пароль: ')
            if password == "qwerty":
                print("Пароль принят.")
                func()
                break
            else:
                if count == 0:
                    print("Пароль неверный. В доступе отказано.")
                    break
                print(f"Пароль неверный.Осталось {count} попыток.")
                count -= 1

    return wraper


@password_check
def bank_credentials():
    """
    Функция виводит данные на экран.
    :return:
    """
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("amount: 100 000 000$")


@password_check
def instagram_credentials():
    """
    Функция виводит данные на экран.
    :return:
    """
    print("username: snowden")
    print("password: cia")


bank_credentials()
instagram_credentials()
