import json
import csv
class Employee:
    """
    Класс принимает  следущие параметры: firstname, lastname, agе, e_mail, people_lang, coding_lang
    Класс возвращает информации о сотруднике, и создает файлы candidates.json и candidates.csv с данными о сотруднике
    """
    firstname = str()
    lastname = str()
    age = int()
    e_mail = str()
    people_lang = list
    coding_lang = list


    def __init__(self, firstname:str, lastname:str, age:int, e_mail:str, people_lang:list, coding_lang:list):
        """
        Метод отвечает за инициализацию экземпляров класса после их создания.
        :param firstname:
        :param lastname:
        :param age:
        :param e_mail:
        :param people_lang:
        :param coding_lang:
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.e_mail = e_mail
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def __str__(self):
        """
        Метод для отображения информации о сотруднике.
        :return: -> Данные о сотруднике
        """
        return \
            (f''
              f'Name: {self.firstname}\n'
              f'Lastname: {self.lastname}\n'
              f'Age: {self.age}\n'
              f'E-mail: {self.e_mail}\n'
              f'Language: {self.people_lang}\n'
              f'Programing: {self.coding_lang}'
              f'')

    def file_write(self):
        """
        Метод записи данных сотрудника в файл(JSON/CSV).
        Создаются два файла: candidates.json и candidates.csv с  данными о сотруднике
        :return:
        """
        key = ['Name', 'Lastname', 'Age', 'E-mail', 'Languages', 'Programming languages']
        value = [self.firstname, self.lastname, self.age, self.e_mail, self.people_lang, self.coding_lang]
        self.listing = dict(zip(key, value))
        listing = self.listing

        with open('candidates.json', 'a') as file:
            json.dump(listing, file)
        with open('candidates.csv', 'at') as stat:
            writer = csv.DictWriter(stat, fieldnames=listing, delimiter=';')
            writer.writeheader()
            writer.writerow(listing)

