# # Задание № 1
#
#
print('Задание № 2')
number = int(input('Введите число:  '))
for i in range(1, number+1):
    if i**2 <= number:
        print(i**2, end=' ')
print()
print('Задание № 3')
number = int(input('Введите число:  '))
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
        if count == 3:
            print(f'{number} не является простым числом')
            break
else:
    print(f'{number} является простым числом')
print()
print('Задание № 4')
mushrooms = int(input('Введите количество грибов:  '))
if mushrooms % 10 == 1:
    ending = ''
elif mushrooms % 10 == 2 or mushrooms % 10 == 3 or mushrooms % 10 == 4:
    ending = 'а'
else:
    ending = 'ов'
print(f'Маша нашла в лесу {mushrooms} гриб{ending}')