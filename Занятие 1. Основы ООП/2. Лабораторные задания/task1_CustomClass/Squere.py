import doctest
class Square:
    def __init__(self, side :(int,float)):
        """
        >>> a = Square(-100)
        Traceback (most recent call last):
        ...
        ValueError: Сторона квадрата должна быть положительным числом
        :param side:
        """
        if not isinstance(side, (int, float)):
            raise TypeError("Сторона квадрата должна быть типа int или float")
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом")
        self.side = side

    def area(self):
        """

        :return:
        """
        return self.side * self.side

a = Square(-100)
b = a.area()
print(b)


