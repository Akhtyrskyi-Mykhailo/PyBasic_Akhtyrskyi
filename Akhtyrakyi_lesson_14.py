def task_1():
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for i in values_to_devide:
        for j in divide_values:
            try:
                print(i / j)
            except TypeError:
                print('Не можна комбінувати ці типи даних')
            except ZeroDivisionError:
                print('Ділити на нуль не можна!')


def task_2():
    divide_values = [2, 0, None, "1", True, False, [], {}]
    values_to_devide = [10, "1", None, True, False, [], 0, {}]
    for i in values_to_devide:
        for j in divide_values:
            try:
                print(i / j)
            except Exception:
                print('Щось пішло не так')
            else:
                print('Ділення пройшло успішно!')


def task_3():
    try:
        list_of_integers = [0, 1, 2, 3, 4, 5]
        user_index = int(input('Введите индекс элемента: '))
        print(list_of_integers[user_index])
    except ValueError:
        print("Потрібно ввести ціле число!")
    except IndexError:
        print("Такого індексу не існує")


def task_4():
    try:
        person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
        user_key = input('Введите название ключа: ')
        print(person_data[user_key])
    except KeyError:
        print("Такого ключа не існує")
    finally:
        print("Чекаю наступного ключа!")


task_1()
task_2()
task_3()
task_4()
