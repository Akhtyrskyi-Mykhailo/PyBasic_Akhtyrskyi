class Animal:
    """
    Класс описывает животных и содержит следующие свойства:
    name - название, movement_speed- скорость передвижения.
    """

    def __init__(self, name, movement_speed):
        self.name = name
        self.movement_speed = movement_speed


class Bird(Animal):
    """
    Класс Bird наследует класс Animal и добавляет свойство wingspan - размах крыльев.
    """

    def __init__(self, name, movement_speed, wingspan):
        super().__init__(name, movement_speed)
        self.wingspan = wingspan


class Poultry(Bird):
    """
    Класс Poultry наследует класс Bird и добавляет свойство weight - вес.
    """

    def __init__(self, name, movement_speed, wingspan, weight):
        super().__init__(name, movement_speed, wingspan)
        self.weight = weight

    def __str__(self):
        return f'{self.name} - домашняя птица со скоростью передвижения {self.movement_speed} км/ч,' \
               f' размахом крыльев {self.wingspan} см. и весом {self.weight} кг.'


class WildBirds(Bird):
    """
    Класс WildBirds наследует класс Bird и добавляет свойство habitat - местом обитания
    """

    def __init__(self, name, movement_speed, wingspan, habitat):
        super().__init__(name, movement_speed, wingspan)
        self.habitat = habitat

    def __str__(self):
        return f'{self.name} - дикая птица со скоростью передвижения {self.movement_speed} км/ч,' \
               f' размахом крыльев {self.wingspan} см. и местом обитания {self.habitat}.'


class Reptile(Animal):
    """
    Класс Reptile наследует класс Animal и добавляет свойство mode_of_movement - способ передвижения.
    """

    def __init__(self, name, movement_speed, mode_of_movement):
        super().__init__(name, movement_speed)
        self.mode_of_movement = mode_of_movement


class Snake(Reptile):
    """
    Класс Snake  наследует класс Reptile и добавляет свойство length - длина.
    """

    def __init__(self, name, movement_speed, mode_of_movement, length):
        super().__init__(name, movement_speed, mode_of_movement)
        self.length = length

    def __str__(self):
        return f'{self.name} - змея со скоростью передвижения {self.movement_speed} км/ч,' \
               f' способом передвижения {self.mode_of_movement} и длиной {self.length} см.'


class Lizard(Reptile):
    """
    Класс Lizard  наследует класс Reptile и добавляет свойство length - длина.
    """

    def __init__(self, name, movement_speed, mode_of_movement, length):
        super().__init__(name, movement_speed, mode_of_movement)
        self.length = length

    def __str__(self):
        return f'{self.name} - ящерица со скоростью передвижения {self.movement_speed} км/ч,' \
               f' способом передвижения {self.mode_of_movement} и длиной {self.length} см.'


class Mammal(Animal):
    """
    Класс Mammal  наследует класс Animal и добавляет свойства wool - шерсть, claws - когти
    """

    def __init__(self, name, movement_speed, wool, claws):
        super().__init__(name, movement_speed)
        self.wool = wool
        self.claws = claws


class Predators(Mammal):
    """
    Класс Predators  наследует класс Mammal и добавляет свойства teet- клыки
    """

    def __init__(self, name, movement_speed, wool, claws, teeth):
        super().__init__(name, movement_speed, wool, claws)
        self.teeth = teeth


class Herbivore(Mammal):
    """
    Класс Herbivore  наследует класс Mammal и добавляет свойства food_type- тип пищи
    """

    def __init__(self, name, movement_speed, wool, claws, food_type):
        super().__init__(name, movement_speed, wool, claws)
        self.food_type = food_type


class Bear(Predators):
    """
    Класс Bear наследует класс Predators и добавляет свойства color- цвет
    """

    def __init__(self, name, movement_speed, wool, claws, teeth, color):
        super().__init__(name, movement_speed, wool, claws, teeth)
        self.color = color

    def __str__(self):
        return f"{self.name} - цвет: {self.color}, шерсть: {self.wool}, когти: {self.claws}, зубы: {self.teeth}," \
               f" скорость передвижения: {self.movement_speed} км/ч"


class Deer(Herbivore):
    """
    Класс Deer наследует класс Herbivore и добавляет свойства antler- рога
    """

    def __init__(self, name, movement_speed, wool, claws, food_type, antler):
        super().__init__(name, movement_speed, wool, claws, food_type)
        self.antler = antler

    def __str__(self):
        return f"{self.name} - рога: {self.antler}, шерсть: {self.wool}, когти: {self.claws}, " \
               f"тип пищи: {self.food_type}, скорость передвижения: {self.movement_speed} км/ч"


eagle = WildBirds("Орел", 60, 200, "горы")
print(eagle)
chicken = Poultry("Курица", 5, 20, 4)
print(chicken)
cobra = Snake("Кобра", 5, "ползком", 150)
print(cobra)
gecko = Lizard("Гекон", 10, "бегом", 30)
print(gecko)
polar_bear = Bear("Полярный медведь", 40, "густая", "есть", "есть", "белый")
print(polar_bear)
moose = Deer("Лань", 35, "короткая", "нет", "растения", "есть")
print(moose)
