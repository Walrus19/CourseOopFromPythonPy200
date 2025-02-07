class Figure:
    def __init__(self, ser=None):
        self.ser = ser

    def print_name(self):
        print(self.ser)


class Rectangle(Figure):
    def __init__(self, a, b, name=None):
        # TODO вызвать конструктор базового класса с помощью super()
        super().__init__(name)
        self.a = a
        self.b = b


if __name__ == "__main__":
    rect = Rectangle(5, 10, 'rect_fig')
    rect.print_name()
