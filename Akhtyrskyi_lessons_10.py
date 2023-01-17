def cenzor_text(filename: str, words: str):
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
    rez_file = open("rez_file.txt", "w")
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
    :return:
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
