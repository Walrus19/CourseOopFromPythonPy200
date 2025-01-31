class Chair:
    color_pallet = ['red', 'black']
    def __init__(self, color: str, height: (int,float)):
        """

        :param color:
        :param height:
        """


        if not isinstance(color,(str)):
            raise TypeError("Цвет стула должен быть строкой")
        self.color = color

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стула должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стула должна быть положительным числом")
        self.height = height

    def change_color(self, new_color):
        if new_color in self.color_pallet:
            self.color = new_color
            print ("Удачное изменение цвета")
        return self.color

ch1 = Chair('red', 100)
ch1.change_color('black')
