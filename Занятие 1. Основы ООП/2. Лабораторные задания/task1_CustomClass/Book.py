class Book:
    def __init__(self, author :str, last_read_page :int, year :int):
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if last_read_page <= 0:
            raise ValueError("Количество страниц не может быть меньше нуля")
        self.last_read_page = last_read_page
        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        if pages <= 0:
            raise ValueError("Год не может быть меньше нуля")
        self.year = year

    def increment_last_read_page(self, read_pages: int):
        self.last_read_page += read_pages
