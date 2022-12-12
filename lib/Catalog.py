from abc import ABC, abstractmethod

from lib import Movie


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

    @abstractmethod
    def add_movie(self, movie: Movie.Movie):
        None

    @abstractmethod
    def remove_movie(self, movie: Movie.Movie):
        None


class Catalog(Search, ABC):
    def __init__(self):
        self.__movie_titles: map[str, list[Movie.Movie]] = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

        def add_movie(self, movie: Movie.Movie):
            if movie.__language in self.__movie_languages.keys:
                list(self.__movie_languages[movie.__language]).append(movie)
            else:
                self.__movie_languages[movie.__language] = [movie]

            if movie.__title in self.__movie_titles.keys:
                list(self.__movie_titles[movie.__title]).append(movie)
            else:
                self.__movie_titles[movie.__title] = [movie]

            if movie.__genre in self.__movie_genres.keys:
                list(self.__movie_genres[movie.__genre]).append(movie)
            else:
                self.__movie_genres[movie.__genre] = [movie]

            if movie.__release_date in self.__movie_release_dates.keys:
                list(self.__movie_release_dates[movie.__release_date]).append(movie)
            else:
                self.__movie_release_dates[movie.__release_date] = [movie]

            if movie.__country in self.__movie_cities.keys:
                list(self.__movie_cities[movie.__country]).append(movie)
            else:
                self.__movie_cities[movie.__country] = [movie]

        def remove_movie(self, movie: Movie.Movie):
            del self.__movie_languages[movie.__language]
            del self.__movie_cities[movie.__country]
            del self.__movie_titles[movie.__title]
            del self.__movie_genres[movie.__genre]
            del self.__movie_release_dates[movie.__release_date]

        def search_by_title(self, title) -> list(Movie.Movie):
            return self.__movie_titles.get(title)

        def search_by_language(self, language) -> list(Movie.Movie):
            return self.__movie_languages.get(language)

        def search_by_genre(self, genre) -> list(Movie.Movie):
            return self.__movie_genres.get(genre)

        def search_by_release_date(self, rel_date) -> list(Movie.Movie):
            return self.__movie_genres.get(rel_date)

        def search_by_city(self, city_name) -> list(Movie.Movie):
            return self.__movie_cities.get(city_name)
