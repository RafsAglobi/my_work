import math


class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        # if len(sides) != self.sides_count:
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if isinstance(i, int) and 0 <= i <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__ * (2 / math.pi)

    def get_square(self):
        return (self.__len__ ** 2) / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __height(self):  # h = 2/a √p(p-a)(p-b)(p-c)
        sp = self.__len__ / 2
        h = (2 ** (sp(sp - self.__sides[0])(sp - self.__sides[1])(sp - self.__sides[2]))
             ) / 2 * sp
        return h

    def get_square(self):  # S = √(р (р — а)(р — b)(p — c))
        sp = self.__len__ / 2
        s = math.sqrt((sp(sp - self.__sides[0])(sp - self.__sides[1])(sp - self.__sides[2])))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = self.sides_count * sides
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())