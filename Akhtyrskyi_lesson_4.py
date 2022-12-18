print('Задание № 1')
action = input("Выберите действие('+', '-', '*', '/', '**'): ")
x = float(input("x = "))
if action in ('+', '-', '*', '/'):
    y = float(input("y = "))
    if action == '+':
        print(f'{x} + {y} = {x + y}')
    elif action == '-':
        print(f'{x} - {y} = {x - y}')
    elif action == '*':
        print(f'{x} * {y} = {x * y}')
    elif action == '/':
        if y != 0:
            print(f'{x} / {y} = {x / y}')
        else:
            print("Деление на ноль не возможно")
if action == '**':
    y = int(input("В какую степень возвести: "))
    print(f'{x} в {y} степени = {x ** y}')
print()

print('Задание № 2')
number = int(input('Введите число:  '))
for i in range(1, number+1):
    if i**2 <= number:
        print(i**2, end=' ')
print()
print()
print('Задание № 3')
number = int(input('Введите число:  '))
for i in range(2, number):
    if number % i == 0:
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