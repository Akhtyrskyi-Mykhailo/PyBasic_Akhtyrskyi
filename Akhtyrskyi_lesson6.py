from random import randint

my_list_1 = [randint(80, 120) for i in range(int(input('Введите количество элементов списка №1:  ')))]
my_list_2 = [randint(80, 120) for i in range(int(input('Введите количество элементов списка №2:  ')))]
num_index = int(input('Введите  индекс элемента в списке:  '))
element = int(input('Введите  значение:  '))
print(f'my_list_1 = {my_list_1}')
print(f'my_list_2 = {my_list_2}')


def task_1(list):
    list_1 = list.copy()
    for i in list_1:
        if i > 100:
            print(i, end=' ')
    print()


def task_2(list):
    list_2 = list.copy()
    my_results = []
    for i in list_2:
        if i > 100:
            my_results.append(i)
    print(my_results)


def task_3(list):
    list_3 = list.copy()
    if len(list_3) < 2:
        list_3.append(0)
    else:
        list_3.append(list_3[-1] + list_3[-2])
    print(list_3)


def task_4(list, k):
    list_4 = list.copy()
    for i in range(k, len(list_4) - 1):
        list_4[i] = list_4[i + 1]
    list_4.pop()
    print(list_4)


def task_5(list, k, C):
    list_5 = list.copy()
    list_5.append('x')
    for i in range(len(list_5) - 1, k, -1):
        list_5[i] = list_5[i - 1]
    list_5[k] = C
    print(list_5)


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
