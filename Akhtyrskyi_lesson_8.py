print('Задание №1')
persons = [{"name": "John", "age": 15}, {"name": "Bil", "age": 55}, {"name": "Valeria", "age": 25},
           {"name": "Mike", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Nadegda", "age": 35}]

print("a)")
ages = [i["age"] for i in persons]
names = [i["name"] for i in persons if i["age"] == min(ages)]
print(names)

print("б)")
len_names = [len(i["name"]) for i in persons]
long_name = [i["name"] for i in persons if len(i["name"]) == max(len_names)]
print(long_name)

print("в)")
ades = [i["age"] for i in persons]
average_age = sum(ades) / len(persons)
print(average_age)

print('Задание №2')
my_dict_1 = {"name": "John", "age": 15, "surname": "Ivanov", "Date of Birth": "02.04.1985", "adress": "Shevchenko St."}
my_dict_2 = {"name": "Bill", "age": 25, "surname": "Petrov", "profession": "doctor", "Place of Birth": "Ukraine"}

print("a)")
list_unique_keys = [i for i in my_dict_1 if i in my_dict_2]
print(list_unique_keys)

print("б)")
list_unique_keys_2 = list(set(my_dict_1) - set(my_dict_2))
print(list_unique_keys_2)

print("б_2)")
list_unique_keys_3 = [i for i in my_dict_1 if i not in my_dict_2]
print(list_unique_keys_3)

print("в)")
my_dict_3 = dict((i, my_dict_1[i]) for i in my_dict_1 if i not in my_dict_2)
print(my_dict_3)

print("в_2)")
my_dict_3_2 = {}
for i in my_dict_1.keys() - my_dict_2.keys():
    my_dict_3_2[i] = my_dict_1[i]
print(my_dict_3_2)

print("г)")
my_dict_4 = {}
for i in my_dict_1:
    if i in my_dict_2:
        my_dict_4.update([(i, [my_dict_1[i], my_dict_2[i]])])
    else:
        my_dict_4.update([(i, my_dict_1[i])])
for j in my_dict_2:
    if j not in my_dict_1:
        my_dict_4.update([(j, my_dict_2[j])])
print(my_dict_4)

print("г_2)")
dikt_rez = {}
for d in my_dict_1, my_dict_2:
    dict_keys = dikt_rez.keys()
    for d_key, d_value in d.items():
        if d_key in dict_keys:
            dikt_rez[d_key] = [dikt_rez[d_key], d_value]
        else:
            dikt_rez[d_key] = d_value
print(dikt_rez)