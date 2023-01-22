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


def count_words(filename: str) -> dict:
    """
    На вход функция получает имя файла, функция возвращает словарь,
    содержащий в качестве ключей слова из текстового файла, а в качестве значений их количество.
    :param filename:
    :return: total -> dict
    """
    file = open(f'{filename}.txt', "r")
    text = file.read()
    text = text.lower()
    text_list = text.split()
    reg_text_list = [word.strip('.,!?()') for word in text_list]
    unique_words = set(reg_text_list)
    total = {}
    for w in unique_words:
        total[w] = reg_text_list.count(w)
    return total


def statistics(filename: str, changed_words: str, dict_word: dict, save_name: str):
    """
    На вход функция получает:
    -имя файла;
    -слова, которые были заменены;
    -словарь, содержащий в качестве ключей слова из текстового файла, а в качестве значений их количество;
    -имя файла, в который был записан измененный текст.
    В результате работы создается файл stat.json(формат данных JSON) со статисткой(обновляемый) в виде:
    -название файла;
    -список слов, которые были заменены;
    -сколько раз каждое слово встретилось в тексте;
    -имя файла, в который был записан измененный текст.
    :param filename:
    :param dict_word:
    :return:
    """
    import json
    import os
    file_infonation = {}
    file_infonation['count_words'] = dict_word
    file_infonation['changed_words'] = changed_words.split()
    file_infonation['filename_with_changes'] = f'{save_name}.txt'
    with open("stat.json", "a") as file:
        if os.stat("stat.json").st_size == 0:
            file.write("{}")
    with open('stat.json', 'r') as read_file:
        stat_dict = json.load(read_file)
        stat_dict[f'{filename}.txt'] = file_infonation
    with open('stat.json', 'w') as write_file:
        json.dump(stat_dict, write_file)
