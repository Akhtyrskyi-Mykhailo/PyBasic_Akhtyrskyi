from Akhtyrskyi_lessons_10 import *
import pprint

print('Задание №1')
file = input('Введите название файла: ')
replacement_words = input('Введите слова через пробел: ')
cenzor_text(file, replacement_words)
print('Задание №2')
x = count_words(file)
pprint.pprint(x)
