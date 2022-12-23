from random import randint

my_list_1 = [randint(80, 120) for i in range(int(input('Введите количество элементов списка №1:  ')))]
my_list_2 = [randint(80, 120) for i in range(int(input('Введите количество элементов списка №2:  ')))]
num_index = int(input('Введите  индекс элемента в списке:  '))
element = int(input('Введите  значение:  '))
print(f'my_list_1 = {my_list_1}')
print(f'my_list_2 = {my_list_2}')


def task_1(list_a):
    for i in list_a:
        if i > 100:
            print(i, end=' ')
    print()


def task_2(list_b):
    my_results = []
    for i in list_b:
        if i > 100:
            my_results.append(i)
    print(my_results)


def task_3(list_c):
    if len(list_c) < 2:
        list_c.append(0)
    else:
        list_c.append(list_c[-1] + list_c[-2])
    print(list_c)


def task_4(list_d, k):
    for i in range(k, len(list_d) - 1):
        list_d[i] = list_d[i + 1]
    list_d.pop()
    print(list_d)


def task_5(list_e, k, C):
    for i in range(len(list_e) - 1, k, -1):
        list_e[i] = list_e[i - 1]
    list_e[k] = C
    print(list_e)


def task_6(list_1, list_2):
    print(f'В строках {len([i for i in (list_1 + list_2) if (list_1 + list_2).count(i) == 1])} уникальных элемента')


print('Задание № 1')
task_1(my_list_1)
print('Задание № 2')
task_2(my_list_1)
print('Задание № 3')
task_3(my_list_1)
print('Задание № 4')
task_4(my_list_1, num_index)
print('Задание № 5')
task_5(my_list_1, num_index, element)
print('Задание № 6')
task_6(my_list_1, my_list_2)
