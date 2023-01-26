def cenzor_text(filename: str, words: str, save_file: str):
    """
    На вход функция получает имя файла и слова для замены (через пробел),
    В результате работы создается файл rez_file.txt, в котором слова
    заменены шаблоном(звездочками)
    :param filename:
    :param words:
    :return:
    """

    import re
    text = open(f'{filename}.txt', "r")
    text_lines = text.readlines()

    list_words = words.split()

    rez_file = open(f"{save_file}.txt", "w")
    for line in text_lines:
        for w in list_words:
            word = r'\b' + w + r'\b'
            line = re.sub(word, len(w) * '*', line, count=0, flags=re.IGNORECASE)
        rez_file.writelines(line)


def count_changed_words(filename: str, chenged_words: str) -> dict:
    """
    На вход функция получает имя файла и слова, которые были в нем заменены.
    Функция возвращает словарь, содержащий в качестве ключей слова,которые были заменены,
    а в качестве значений их количество.
    :param filename:
    :return: total -> dict
    """
    file = open(f'{filename}.txt', "r")
    text = file.read()
    text_list = text.lower().split()
    edited_text_list = [word.strip('.,!?()') for word in text_list]
    list_chenged_words = chenged_words.split()
    count_words = {}
    for word in list_chenged_words:
        count_words[word] = edited_text_list.count(word)

    return count_words



def file_information(file_name: str, dict_count: dict, save_filename: str) -> dict:
    """
    На вход функция получает:
    - имя файла, словарь с количеством измененных слов и имя файла, в который был записан измененный текст.
    Функция возвращает словарь, где ключ - имя файла, значение - словарь с количеством измененных слов;
    и имя файла, в который был записан измененный текст.
    :param file_name:
    :param dict_count:
    :param save_filename:
    :return: inf_file: -> dict
    """
    dict_file_information = {}
    dict_file_information[f'{file_name}.txt'] = dict_count
    dict_file_information['filename_with_changes'] = f'{save_filename}.txt'
    return dict_file_information


def save_in_json_file(information_dict: dict):
    """
    На вход функция получает словарь с информацией о фaйле.
    В результате работы в файл stat.json, дописывается информация о новом цензурируемом файле.

    :param information_dict: -> dict
    :return:
    """
    import json
    import os

    if not os.path.isfile('stat.json'):            # проверяем существует ли файл stat.json
        with open("stat.json", "w") as file:       # если нет, то  создаем  файл stat.json и
            file.write("[]")                       # "создаем" в нем пустой список
    with open('stat.json', 'r') as read_file:      # открываем файл stat.json
        statistic_list = json.load(read_file)
        statistic_list.append(information_dict)    # добавляем в список словарь с данными: {имя файла: {информация}}
    with open('stat.json', 'w') as write_file:
        json.dump(statistic_list, write_file)      # записываем новые данные в stat.json


def save_in_csv_file(information_dict: dict):
    """
    На вход функция получает словарь с информацией о фaйле.
    В результате работы в файл stat.csv, дописывается информация о новом цензурируемом файле.
    :param information_dict:
    :return:
    """

    import csv
    import os

    if not os.path.isfile('stat.csv'):
        with open('stat.csv', "w", encoding='cp1251', newline='') as header:
            writer = csv.writer(header, delimiter=';')
            writer.writerow(('filename', 'word', 'count', 'filename with changes'))

    with open('stat.csv', "a", encoding='cp1251', newline='') as filename:
        writer = csv.writer(filename, delimiter=';')
        writer.writerow((f'{list(information_dict.keys())[0]}', '', '', f'{information_dict["filename_with_changes"]}'))

    for key, value in information_dict[list(information_dict.keys())[0]].items():
        with open('stat.csv', 'a', encoding='cp1251', newline='') as word_count:
            writer = csv.writer(word_count, delimiter=';')
            writer.writerow((' ', key, value, ' '))
