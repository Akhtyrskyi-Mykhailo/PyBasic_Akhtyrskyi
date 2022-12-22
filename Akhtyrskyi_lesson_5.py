print('Задание №1')
my_string = '0123456789'
for i in my_string:
    for j in my_string:
        print(int(i + j), end=',')

print()
print()
print('Задание №2')
size = int(input('Введите высоту треугольника:  '))
print('A')
for i in range(size):
    print('  ' * (size - i), '*', i * ' * *', sep='')
print()
print('B')
print(size * '  ', '*', sep='')
for i in range(size - 2):
    print((size - i - 1) * '  ', '*', ' ', (i * 2 + 1) * '  ', '*', sep='')
print((size - i - 2) * ' ', (size * 2 - 1) * ' *', sep='')
print()
print('C')
for i in range(size):
    print('  ' * (size - i), '*', i * ' * *', sep='')
for i in reversed(range(size - 2)):
    print((size - i - 1) * '  ', '*', (i * 2 + 1) * '  ', ' *', sep='')
print(size * '  ', '*', sep='')
print()
print('D')
for i in range(size):
    print('  ' * (size - i), '*', i * ' * *', sep='')
for i in reversed(range(size - 2)):
    print((size - i - 1) * '  ', '*', int((i * 2 + 1) / 2) * '  ', ' *',
          int((i * 2 + 1) / 2) * '  ', ' *', sep='')
print(size * '  ', '*', sep='')