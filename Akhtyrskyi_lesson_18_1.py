class Transport:
    """
    Класс Transport описывает транспортное средство и содержит следующие свойства:
    number - номер, number_of_wheels - количество колес, engine_power - мощность двигателя,
    max_speed - максимальная скорость.
    """

    def __init__(self, number, number_of_wheels, engine_power, max_speed):
        self.__number = number
        self.__number_of_wheels = number_of_wheels
        self.__engine_power = engine_power
        self.__max_speed = max_speed

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса Transport, включающее значения всех его свойств.
        :return:
        """
        return f"Number: {self.__number}, Number of Wheels: {self.__number_of_wheels}," \
               f" Engine Power: {self.__engine_power}, Max Speed: {self.__max_speed}"

    def set_number(self, number):
        """
        Метод устанавливает значение свойства number.
        :param number:
        :return:
        """
        self.__number = number

    def get_number_of_wheels(self):
        """
        Метод возвращают значения свойствa number_of_wheels
        :return:
        """
        return self.__number_of_wheels

    def get_engine_power(self):
        """
        Метод возвращают значения свойствa engine_power
        :return:
        """
        return self.__engine_power

    def get_max_speed(self):
        """
        Метод возвращают значения свойствa max_speed
        :return:
        """
        return self.__max_speed


class Bicycle(Transport):
    """
    Класс Bicycle наследует класс Transport и добавляет свойство mass - массу велосипеда.
    """

    def __init__(self, number, number_of_wheels, engine_power, max_speed, mass):
        super().__init__(number, number_of_wheels, engine_power, max_speed)
        self.__mass = mass

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса Bicycle,
        включающее значения всех его свойств, а также массу.
        :return:
        """
        return f"{super().__str__()}, Mass: {self.__mass}"


class Car(Transport):
    """
    Класс наследует класс Transport и добавляет свойство body_type - тип кузова.
    """

    def __init__(self, number, number_of_wheels, engine_power, max_speed, body_type):
        super().__init__(number, number_of_wheels, engine_power, max_speed)
        self.__body_type = body_type

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса Car,
        включающее значения всех его свойств, а также тип кузова.
        :return:
        """
        return f"{super().__str__()}, Body Type: {self.__body_type}"


class Bus(Transport):
    """
    Класс наследует класс Transport и добавляет свойство num_passengers - количество пассажиров.
    """

    def __init__(self, number, number_of_wheels, engine_power, max_speed, num_passengers):
        super().__init__(number, number_of_wheels, engine_power, max_speed)
        self.__num_passengers = num_passengers

    def __str__(self):
        """
        Метод возвращает строковое представление объекта класса Bus,
        включающее значения всех его свойств, а также количество пассажиров
        :return:
        """
        return f"{super().__str__()}, Number of Passengers: {self.__num_passengers}"


class Truck(Car):
    """
    Класс наследует класс Car и добавляет свойство carrying_capacity - грузоподъемность.
    """

    def __init__(self, number, number_of_wheels, engine_power, max_speed, body_type, carrying_capacity):
        super().__init__(number, number_of_wheels, engine_power, max_speed, body_type)
        self.__carrying_capacity = carrying_capacity

    def __str__(self):
        """
        Метод  возвращает строковое представление объекта класса Truck,
        включающее значения всех его свойств, а также грузоподъемность.
        :return:
        """
        return f"{super().__str__()}, Carrying Capacity: {self.__carrying_capacity}"


bike = Bicycle("АН1236", 2, 1, 10, 15)
print(bike)
car = Car("ВВ4356", 4, 100, 200, "sedan")
print(car)
bus = Bus("ХА7089", 6, 200, 120, 50)
print(bus)
truck = Truck("АН101112", 8, 500, 80, "flatbed", 5000)
print(truck)
