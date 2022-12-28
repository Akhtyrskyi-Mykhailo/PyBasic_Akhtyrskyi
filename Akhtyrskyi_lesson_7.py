from random import randint

my_list_1 = [randint(1, 100) for i in range(int(input('Введите количество элементов списка №1:  ')))]
my_list_2 = [randint(80, 120) for i in range(int(input('Введите количество элементов списка №2:  ')))]
print(f'my_list_1 = {my_list_1}')
print(f'my_list_2 = {my_list_2}')

print('Задание №3(вариант 1)')
my_result_1 = [my_list_1[i] for i in range(0, len(my_list_1), 2)] + [my_list_2[j] for j in range(1, len(my_list_2), 2)]
print(f'my_result = {my_result_1}')

print('Задание №3(вариант 2)')
my_result_2 = []
my_result_2.extend(my_list_1[::2])
my_result_2.extend(my_list_2[1::2])
print(f'my_result = {my_result_2}')

print('Задание №3(вариант 3)')
my_result_3 = my_list_1[::2] + my_list_2[1::2]
print(f'my_result = {my_result_3}')

print('Задание №4(вариант 1)')
new_list_1 = [my_list_1[i] for i in range(1, len(my_list_1))]
new_list_1.append(my_list_1[0])
print(f'new_list_1 = {new_list_1}')

print('Задание №4(вариант 2)')
new_list_2 = []
new_list_2.extend(my_list_1[1::])
new_list_2.append(my_list_1[0])
print(f'new_list_2 = {new_list_2}')

print('Задание №4 (вариант 3)')
new_list_3 = my_list_1[1:] + [my_list_1[0]]
print(f'new_list_3 = {new_list_3}')

print('Задание №5')
my_list = [11, 'r', 25, 23, 'A']
print(f'my_list = {my_list}')
x = my_list.pop(0)
my_list.append(x)
print(f'my_list = {my_list}')

print('Задание №6')
string = "43 больше чем 34 но меньше чем 56"
print(string)
str_list = string.split()
count = 0
for i in str_list:
    if i.isdigit():
        count += int(i)
print(count)

print('Задание №7')
my_str_7 = 'My long string'
print(my_str_7)
l_limit, r_limit = 'o', 'g'
sub_str = my_str_7[my_str_7.find(l_limit) + 1: my_str_7.rfind(r_limit)]
print(sub_str)

print('Задание №8')
my_str_8 = 'd8d7683h4'
print(my_str_8)
list_8 = []
if len(my_str_8) % 2 != 0:
    my_str_8 = my_str_8 + '_'
for i in range(0, len(my_str_8), 2):
    list_8.append(my_str_8[i:i + 2])
print(list_8)

print('Задание №9')
my_list_9 = [3, 6, 9, 34, 43, 6, 57, 44, 7]
print(my_list_9)
counter = 0
for i in range(1, len(my_list_9) - 1):
    if my_list_9[i] > my_list_9[i - 1] + my_list_9[i + 1]:
        counter += 1
print(counter)

print('Задание №10')
my_list_10 = [11, 3, '33', 45, '2', '67', 12, 27]
print(my_list_10)
new_list_10 = []
for i in range(len(my_list_10)):
    if type(my_list_10[i]) == str:
        new_list_10.append(my_list_10[i])
print(new_list_10)

print('Задание №11')
my_str_11 = 'asdfffghhghh5662'
print(my_str_11)
my_list_11 = [i for i in my_str_11 if my_str_11.count(i) == 1]
print(my_list_11)

print('Задание №12')
str_12 = 'mc68568-c356c-3567-376'
str_12_2 = 'jd826529yf9276592828740=-'
print(str_12)
print(str_12_2)
my_list_12 = [i for i in str_12 if i in str_12_2]
print(my_list_12)

print('Задание №13')
str_13 = 'aaaasdf1'
str_13_2 = 'asdfff2'
print(str_13)
print(str_13_2)
my_list_13 = [i for i in str_13 if i in str_13_2]
new_list_13 = [j for j in my_list_13 if str_13.count(j) == 1 and str_13_2.count(j) == 1]
print(new_list_13)
