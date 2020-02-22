import math


class Figure:

    def __init__(self, name, angles):
        self.name = "Класс фигуры - " + name
        self.angles = "Количество углов " + angles

    def print_area(self, a, b):
        self.a = a
        self.b = b
        area = str(self.a * self.b)
        self.area = "Площадь фигуры равна " + area
        return self.area

    def print_perimeter(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        perimeter = str(self.a + self.b + self.c)
        self.perimeter = "Периметр равен " + perimeter + '\n'
        return self.perimeter

    def add_square(self):
        squares = "Сумма площадей равна "
        return squares


class Triangle(Figure):
    def __init__(self, name, angles):
        super().__init__(name, angles)

    def print_area(self, a, b):
        super().print_area(a, b)
        h = b
        area = 1 / 2 * (a * h)
        self.area = "Площадь равна " + str(area)
        print(self.area)

    def print_perimeter(self, a, b, c):
        super().print_perimeter(a, b, c)
        print(self.perimeter)


class Rectangle(Figure):
    def __init__(self, name, angles):
        super().__init__(name, angles)

    def print_area(self, a, b):
        super().print_area(a, b)
        print(self.area)

    def print_perimeter(self, a, b, c):
        super().print_perimeter(a, b, c)
        c = 2
        perimeter = (a + b) * c
        self.perimeter = "Периметр равен " + str(perimeter) + '\n'
        print(self.perimeter)


class Square(Figure):
    def __init__(self, name, angles):
        super().__init__(name, angles)

    def print_area(self, a, b):
        super().print_area(a, b)
        self.b = a
        self.area = "Площадь равна " + str(a * self.b)
        print(self.area)

    def print_perimeter(self, a, b, c):
        super().print_perimeter(a, b, c)
        self.a = a
        self.perimeter = "Периметр равен " + str(self.a * 4)
        print(self.perimeter)


class Circle(Figure):

    def __init__(self, name, angles):
        super().__init__(name, angles)

    def print_area(self, a, b):
        super().print_area(a, b)
        self.radius = a
        area = math.pi * self.radius ** 2
        self.area = "Площадь равна " + str(area)
        print(self.area)

    def print_perimeter(self, a, b, c):
        super().print_perimeter(a, b, c)
        self.radius = a
        area = 2 * (math.pi * self.radius)
        self.perimetr = "Периметр равен " + str(area) + '\n'
        print(self.perimetr)


example_triangle = Triangle(name="triangle", angles="3")
print(example_triangle.name, "\n", example_triangle.angles)
example_triangle.print_area(2, 7)
example_triangle.print_perimeter(1, 2, 3)

example_circle = Circle(name="circle", angles="0")
print(example_circle.name, "\n", example_circle.angles)
example_circle.print_area(2, math.pi)
example_circle.print_perimeter(10, math.pi, 0)

example_rectangle = Rectangle(name="rectangle", angles="4")
print(example_rectangle.name, "\n", example_rectangle.angles)
example_rectangle.print_area(2, 10)
example_rectangle.print_perimeter(1, 10, 0)

example_square = Square(name="square", angles="4")
print(example_square.name, "\n", example_square.angles)
example_square.print_area(10, 0)
example_square.print_perimeter(10, 0, 0)
