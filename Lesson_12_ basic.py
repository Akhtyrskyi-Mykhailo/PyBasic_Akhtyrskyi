from Akhtyrskyi_lesson_12 import *
import os

file = input('Введите имя файла для рецензирования: ')
while not os.path.isfile(f'{file}.txt'):
    file = input('Файла с таким иненем не найдено. Введите корректное имя файла: ')
replacement_words = input('Введите слова через пробел, которые нужно заменить: ')
filename_to_save = input('Введите имя файла, в который сохранить результат: ')
cenzor_text(file, replacement_words, filename_to_save)
save_in_json_file(file_information(file, count_changed_words(file, replacement_words), filename_to_save))
save_in_csv_file(file_information(file, count_changed_words(file, replacement_words), filename_to_save))
