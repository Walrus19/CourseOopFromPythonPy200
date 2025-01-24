class Square:
    def __init__(self, side :(int,float)):
        if not isinstance(side, (int, float)):
            raise TypeError("Сторона квадрата должна быть типа int или float")
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительным числом")
        self.side = side

    def area(self):
        return self.side * self.side
