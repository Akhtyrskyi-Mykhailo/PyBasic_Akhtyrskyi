print('Задание №1')
my_string = '0123456789'
for i in my_string:
    for j in my_string:
        print(int(i + j), end=',')
print()

print('Задание №2')
height = int(input('Введите высоту треугольника: '))
print('A')
for i in range(1, height + 1):
    for j in range(height - i):
        print(' ', end=' ')
    for z in range(2 * i - 1):
        if z == 0 or z == 2 * i - 2:
            print('*', end=' ')
        else:
            if i == height:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()
print()
print('B')
for i in range(1, height + 1):
    for j in range(height * 2 - i * 2):
        print(' ', end='')
    for z in range(2 * i - 1):
        print('*', end=' ')
    print()
print()
print('C')
for i in range(1, height + 1):
    for j in range(height * 2 - i * 2):
        print(' ', end='')
    for z in range(2 * i - 1):
        print('*', end=' ')
    print()
for i in range(height - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(2 * (height - i - 1) - 1):
        if j == 0 or j == 2 * (height - i - 1) - 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()
print('D')
for i in range(1, height + 1):
    for j in range(height * 2 - i * 2):
        print(' ', end='')
    for z in range(2 * i - 1):
        print('*', end=' ')
    print()
for i in range(height - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(2 * (height - i - 1) - 1):
        if j == 0 or j == 2 * (height - i - 1) - 2 or j == (height - i - 1) - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()