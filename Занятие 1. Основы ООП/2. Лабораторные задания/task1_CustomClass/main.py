# TODO Написать 3 класса с документацией и аннотацией типов



class Book:
    def __init__(self, author, pages, year):
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self.pages = pages
        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        if pages <= 0:
            raise ValueError("Год не может быть меньше нуля")
        self.year = year


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
