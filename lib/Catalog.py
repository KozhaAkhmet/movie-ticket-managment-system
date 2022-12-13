from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

from lib.Movie import Movie


class Search(ABC):

    @abstractmethod
    def search_by_title(self, title: str) -> List[Movie]:
        pass

    @abstractmethod
    def search_by_language(self, language: str) -> List[Movie]:
        pass

    @abstractmethod
    def search_by_genre(self, genre: str) -> List[Movie]:
        pass

    @abstractmethod
    def search_by_release_date(self, rel_date: datetime) -> List[Movie]:
        pass

    @abstractmethod
    def search_by_city(self, city_name: str) -> List[Movie]:
        pass

    @abstractmethod
    def add_movie(self, movie: Movie):
        pass

    @abstractmethod
    def remove_movie(self, movie: Movie):
        pass

    @abstractmethod
    def search_by_filter(self, genre, release_date, language, title, city, date, seat) -> List[Movie]:
        pass


class Catalog(Search, ABC):
    def __init__(self):
        self.__movie_titles: Dict[str, List[Movie]] = {}
        self.__movie_languages: Dict[str, List[Movie]] = {}
        self.__movie_genres: Dict[str, List[Movie]] = {}
        self.__movie_release_dates: Dict[datetime, List[Movie]] = {}
        self.__movie_cities: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie):
        if movie.language in self.__movie_languages.keys():
            self.__movie_languages[movie.language].append(movie)
        else:
            self.__movie_languages[movie.language] = [movie]

        if movie.title in self.__movie_titles.keys():
            self.__movie_titles[movie.title].append(movie)
        else:
            self.__movie_titles[movie.title] = [movie]

        if movie.genre in self.__movie_genres.keys():
            self.__movie_genres[movie.genre].append(movie)
        else:
            self.__movie_genres[movie.genre] = [movie]

        if movie.release_date in self.__movie_release_dates.keys():
            self.__movie_release_dates[movie.release_date].append(movie)
        else:
            self.__movie_release_dates[movie.release_date] = [movie]

        if movie.city in self.__movie_cities.keys():
            self.__movie_cities[movie.city].append(movie)
        else:
            self.__movie_cities[movie.city] = [movie]

    def remove_movie(self, movie: Movie):
        del self.__movie_languages[movie.language]
        del self.__movie_cities[movie.city]
        del self.__movie_titles[movie.title]
        del self.__movie_genres[movie.genre]
        del self.__movie_release_dates[movie.release_date]

    def search_by_title(self, title) -> List[Movie]:
        return self.__movie_titles.get(title)

    def search_by_language(self, language) -> List[Movie]:
        return self.__movie_languages.get(language)

    def search_by_genre(self, genre) -> List[Movie]:
        return self.__movie_genres.get(genre)

    def search_by_release_date(self, rel_date) -> List[Movie]:
        return self.__movie_release_dates.get(rel_date)

    def search_by_city(self, city_name) -> List[Movie]:
        return self.__movie_cities.get(city_name)

    # def search_by_filter(self, genre, release_date, language, title, city, date, seat):
    #     if genre is not None:
    #         return Catalog.search_by_genre(genre)
    #     if release_date is not None:
    #         return Catalog.search_by_release_date(release_date)
    #     if language is not None:
    #         return Catalog.search_by_language(language)
    #     if title is not None:
    #         return Catalog.search_by_title(title)
    #     if city is not None:
    #         return Catalog.search_by_city(city)
    #     # Print search output

    def print_this(self):
        print(self)


