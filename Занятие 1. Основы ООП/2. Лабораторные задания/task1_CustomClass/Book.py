import doctest
class Book:
    def __init__(self, author :str, last_read_page :int, year :int):
        """

        :param author:
        :param last_read_page:
        :param year:
        >>> book = book("Пушкин",-500, 1978)  # Неверная инициализация класса
        ...
        ValueError: Количество страниц не может быть меньше нуля
        """
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        self.author = author
        if not isinstance(last_read_page, int):
            raise TypeError("Количество страниц должно быть типа int")
        if last_read_page <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self.last_read_page = last_read_page
        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        if last_read_page <= 0:
            raise ValueError("Год не может быть меньше нуля")
        self.year = year

    def increment_last_read_page(self, read_pages: int):
        """
        Увеличение количества просмотренных страниц
        :param read_pages:

        >>>book.increment_last_read_page(-200)
        ...
        raise ValueError("Количество страниц не может быть меньше нуля")
        :return:
        """
        if not isinstance(read_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if read_pages <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self.last_read_page += read_pages
        return self.last_read_page


book = Book("Пушкин",-100,1878)
book.increment_last_read_page(200)
print(a.__dict__)
