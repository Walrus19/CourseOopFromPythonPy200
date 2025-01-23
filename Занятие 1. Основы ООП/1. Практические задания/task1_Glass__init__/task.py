from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)



        if not isinstance(capacity_volume, Union[int,float]) or not isinstance(occupied_volume, Union[int,float]):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0 or occupied_volume < 0 :
            raise ValueError("Объем стакана должен быть положительным числом")
        if capacity_volume < occupied_volume:
            raise ValueError("Занятый объем не может быть больше объема стакана")



        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    a = Glass(100,50)
    b = Glass(200,100)
    try:
        c = Glass('litr', 100.5)
        d = Glass(50,100)
        # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


