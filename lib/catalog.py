from abc import ABC, abstractmethod


class Search(ABC):

    @abstractmethod
    def search_by_title(self, title):
        pass
    @abstractmethod
    def search_by_language(self, language):
        pass
    @abstractmethod
    def search_by_genre(self, genre):
        pass
    @abstractmethod
    def search_by_release_date(self, rel_date):
        pass
    @abstractmethod
    def search_by_city(self, city_name):
        pass


class Catalog(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

        def search_by_title(self, title):
            return self.__movie_titles.get(title)

        def search_by_language(self, language):
            return self.__movie_languages.get(language)

        def search_by_genre(self, genre):
            return self.__movie_genres.get(genre)

        def search_by_release_date(self, rel_date):
            return self.__movie_genres.get(rel_date)

        def search_by_city(self, city_name):
            return self.__movie_cities.get(city_name)
