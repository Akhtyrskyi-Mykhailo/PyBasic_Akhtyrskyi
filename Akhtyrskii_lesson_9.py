def task_1(list_1: list) -> list:
    """
    Функция возвращает новый список, в котором содержаться
    элементы из my_list по следующему правилу:
    Если строка стоит на нечетном месте в my_list, то ее заменить на перевернутую строку.
    Если на четном - оставить без изменения
    :param list_1:
    :return: new_list_1
    """
    new_list_1 = list_1.copy()
    for i in range(1, len(new_list_1), 2):
        new_list_1[i] = new_list_1[i][::-1]
    return new_list_1


def task_2(list_2: list) -> list:
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list, у которых первый символ - буква "a"
    :param list_2:
    :return: new_list_2
     """
    new_list_2 = [i for i in list_2 if i[0] == 'a']
    return new_list_2


def task_3(list_3: list) -> list:
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list, в которых есть символ - буква "a" на любом месте.
    :param list_3:
    :return: new_list_3
    """
    new_list_3 = [i for i in list_3 if 'a' in i]
    return new_list_3


def task_4(list_4: list) -> list:
    """
    Функция возвращает новый список, в котором содержаться только строки из my_list
    :param list_4:
    :return: new_list_4
    """
    new_list_4 = [i for i in list_4 if isinstance(i, str)]
    return new_list_4


def task_5(string_5: str) -> list:
    """
    Функция возвращает новый список, в котором содержаться те символы из my_str,
    которые встречаются в строке только один раз
    :param string_5:
    :return: new_list_5
    """
    new_list_5 = [i for i in string_5 if string_5.count(i) == 1]
    return new_list_5


def task_6(string_6_1: str, string_6_2: str) -> list:
    """
    Функция возвращает список, в который помещены те символы,
    которые есть в обеих строках хотя бы раз
    :param string_6_1:
    :param string_6_2:
    :return: new_list_6
    """
    new_list_6 = [i for i in set(string_6_1 + string_6_2) if i in string_6_1 and i in string_6_2]
    return new_list_6


def task_7(string_7_1: str, string_7_2: str) -> list:
    """
    Функция возвращает список, в который помещены те символы, которые есть в обеих строках,
    но в каждой только по одному разу.
    :param string_7_1:
    :param string_7_2:
    :return: new_list_7
    """

    new_list_7 = [i for i in set(string_7_1 + string_7_2) if string_7_1.count(i) == 1 and string_7_2.count(i) == 1
                  and i in string_7_1 and i in string_7_2]
    return new_list_7


def task_8(name: list, domain: list) -> str:
    """
    Функция для генерирования e-mail в формате:
    фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
    :param name:
    :param domain:
    :return: e_mail
    """
    from random import randint, choice
    letters = 'abcdefghijklmnopqrstuvwxyz'
    a = [choice(letters) for i in range(randint(5, 7))]
    e_mail = f"{choice(name)}.{randint(100, 999)}@{''.join(a)}.{choice(domain)}"
    return e_mail
