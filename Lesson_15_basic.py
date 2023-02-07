from Akhtyrskyi_lesson_15 import *

firstname = input('Ввидите имя: ').capitalize()
lastname = input('Введите фамилию: ').capitalize()
age = int(input('Введите возраст: '))
e_mail = input('Введите e-mail: ')
people_lang = input('Иностранные языки: ').split()
coding_lang = input('Языки програмирования: ').split()
person = Employee(firstname, lastname, age, e_mail, people_lang, coding_lang)
person.file_write()
print(person)