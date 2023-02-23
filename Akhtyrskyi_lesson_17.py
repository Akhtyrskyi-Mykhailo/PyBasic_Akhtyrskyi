class Person:
    """
    Класс, создающий человека с четырьмя свойствами: first_name, last_name, age и profession
    """
    __first_name = str()
    __last_name = str()
    __age = int()
    __profession = str()

    @property
    def first_name(self):
        return self.__first_name.capitalize()

    @property
    def last_name(self):
        return self.__last_name.capitalize()

    @property
    def age(self):
        return self.__age

    @property
    def profession(self):
        return self.__profession

    def __set_age(self, age: int):
        """

        :param age:
        :return:
        """
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0

    def __init__(self, first_name, last_name, age, profession):
        """
         Инициализирует объект Person с заданными именем, фамилией, возрастом и профессией.
        :param first_name:
        :param last_name:
        :param age:
        :param profession:
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__set_age(age)
        self.__profession = profession

    def __str__(self):
        """
        возвращает строковое представление объекта Person.
        :return:
        """
        return f"{self.first_name} {self.last_name}, {self.age}, {self.profession}"

class Family:
    """
    Kласс, представляющий семью с четырьмя свойствами: адрес проживания, мать, отец и дети.
    """
    def __init__(self, address, mother, father, children=None):
        """
        Инициализирует объект семьи с заданным адресом, матерью, отцом и детьми.
        :param address:
        :param mother:
        :param father:
        :param children:
        """
        self.__address = address
        self.__mother = mother
        self.__father = father
        self.__children = [] if children is None else children

    def add_child(self, child):
        """
        Добавляет объект Person в список  элементов.
        :param child:
        :return:
        """
        self.__children.append(child)

    def __str__(self):
        """
        Возвращает строковое представление объекта Family, включая адрес,
        имена родителей и список имен детей, разделенных запятыми.
        :return:
        """
        children_names = ", ".join([child.first_name for child in self.__children])
        return f"Family living at {self.__address}. Parents: {self.__mother.first_name}, {self.__father.first_name}." \
               f" Children: {children_names}"


mother = Person("maria", "Bondar", 48, "Teacher")
print(mother)
father = Person("vladimir", "Bondar", 50, "Engineer")
print(father)
child1 = Person("alice", "Bondar", 17, "Student")
print(child1)
child2 = Person("nikolay", "Bondar", 3, "Toddler")


family1 = Family("71 Shevchenko St", mother, father, [child1, child2])
print(family1)
