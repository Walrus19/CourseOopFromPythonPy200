import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    # TODO определить конструктор
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал
    def area(self):
        super().area()
        return self.a * self.b

class Circle(Figure):
    """ Производный класс. Круг. """
    # TODO определить конструктор
    def __init__(self, r):
        self.r = r
    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал"
    def area(self):
       super().area()
       return round(math.pi * math.pow(self.r, 2), 2)

if __name__ == "__main__":
    fig = Figure()
    print(fig.area())

    rect = Rectangle(5, 10)
    print(rect.area())

    circle = Circle(5)
    print(circle.area())
