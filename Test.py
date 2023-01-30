information_dict = {'file': {'ah': 1, 'bh': 2, 'ch': 3}, 'save_name': 'save.txt'}

import csv
import os

if not os.path.isfile('stat.csv'):
    with open('stat.csv', "w", encoding='cp1251',  newline='') as f1:
        writer = csv.writer(f1, delimiter=';')
        writer.writerow(('filename', 'word', 'count', 'save_name'))

with open('stat.csv', "a", encoding='cp1251',  newline='') as f2:
    writer = csv.writer(f2, delimiter=';')
    writer.writerow((f'{list(information_dict.keys())[0]}', '', '', f'{information_dict["save_name"]}'))

for key, value in information_dict[list(information_dict.keys())[0]].items():
    with open('stat.csv', 'a', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((' ', key, value, ' '))
