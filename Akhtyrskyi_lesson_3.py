print('Задание № 1')
n , k = int(input('Введите количество школьников:  ')), int(input('Введите количество яблок:  '))
print(f'{k // n} яблок достанется каждому школьнику')
print(f'{k % n} яблок останется в корзинке')
print()
print()
print('Задание № 2')
class_1 = int(input('Введите количество учеников в первом классе:  '))
class_2 = int(input('Введите количество учеников во втором классе:  '))
class_3 = int(input('Введите количество учеников в третьем классе:  '))
print(f'Всего нужно закупить {(class_1 + 1) // 2 + (class_2 + 1) // 2 + (class_3 + 1) // 2} парт(ы).')
print()
print()
print('Задание № 3')
num = int(input('Введите трехзначное число:  '))
print((num % 10) * 100 + ((num % 100) // 10) * 10 + (num // 100))
print()
print()
print('Задание № 4')
sek = int(input('Введите количество секунд прошедших от начала суток:  '))
print(f'{sek // 3600}:{(sek % 3600) // 60}:{(sek % 3600) % 60}')