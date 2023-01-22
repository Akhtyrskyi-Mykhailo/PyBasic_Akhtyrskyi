from Akhtyrskyi_lesson_12 import *

print('Задание №1')
file = input('Введите имя файла для рецензирования: ')
replacement_words = input('Введите слова через пробел, которые нужно заменить: ')
filename_to_save = input('Введите имя файла, в который сохранить результат: ')
cenzor_text(file, replacement_words, filename_to_save)
print('Задание №2')
statistics(file, replacement_words, count_words(file), filename_to_save)