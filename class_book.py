class Book:
    def __init__(self, len_authors, authors, title, edition, city, publisher, year, book_number):
        self.__len_authors = len_authors
        self.__authors = authors
        self.__title = title
        self.__edition = edition
        self.__city = city
        self.__publisher = publisher
        self.__year = year
        self.__book_number = book_number

    @property
    def len_authors(self):
        return self.__len_authors

    @len_authors.setter
    def len_authors(self, len_authors):
        self.__len_authors = len_authors

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition):
        self.__edition = edition

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def book_number(self):
        return self.__book_number

    @book_number.setter
    def book_number(self, book_number):
        self.__book_number = book_number
