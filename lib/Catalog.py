from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

from lib.Cinema import CinemaHall
from lib.Movie import Movie, Show
import pandas as pd

__result_filter = 0
__tmp = 0
__i = 0


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

    def get_all_movies(self):
        pass

    @abstractmethod
    def search_by_filter(self, filter_values: list):
        pass


class Catalog(Search, ABC):
    def __init__(self):
        self.__movie_titles: Dict[str, List[Movie]] = {}
        self.__movie_languages: Dict[str, List[Movie]] = {}
        self.__movie_genres: Dict[str, List[Movie]] = {}
        self.__movie_release_dates: Dict[datetime, List[Movie]] = {}
        self.__movie_cities: Dict[str, List[Movie]] = {}
        self.__all_movies: List[Dict] = []
        self.__data_frame: pd.DataFrame = pd.DataFrame()

    def add_movie(self, movie: Movie):
        if movie.get_language() in self.__movie_languages.keys():
            self.__movie_languages[movie.get_language()].append(movie)
        else:
            self.__movie_languages[movie.get_language()] = [movie]

        if movie.get_title() in self.__movie_titles.keys():
            self.__movie_titles[movie.get_title()].append(movie)
        else:
            self.__movie_titles[movie.get_title()] = [movie]

        if movie.get_genre() in self.__movie_genres.keys():
            self.__movie_genres[movie.get_genre()].append(movie)
        else:
            self.__movie_genres[movie.get_genre()] = [movie]

        if movie.get_rel_date() in self.__movie_release_dates.keys():
            self.__movie_release_dates[movie.get_rel_date()].append(movie)
        else:
            self.__movie_release_dates[movie.get_rel_date()] = [movie]

        if movie.get_city() in self.__movie_cities.keys():
            self.__movie_cities[movie.get_city()].append(movie)
        else:
            self.__movie_cities[movie.get_city()] = [movie]

        if movie not in self.__all_movies:
            self.__all_movies.append(movie.to_dict())

    def remove_movie(self, movie: Movie):
        del self.__movie_languages[movie.get_language()]
        del self.__movie_cities[movie.get_city()]
        del self.__movie_titles[movie.get_title()]
        del self.__movie_genres[movie.get_genre()]
        del self.__movie_release_dates[movie.get_rel_date()]

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

    def get_all_movies(self) -> List[Dict]:
        return self.__all_movies

    def search_by_filter(self, filter_values: dict):
        global result_filter, tmp, i
        all_movie_df = pd.DataFrame(self.__all_movies)
        print(all_movie_df)
        i = 0
        try:
            for filter_key in filter_values.keys():
                # print(filter_values[filter_key])
                if filter_values[filter_key] != "":
                    result_filter = (all_movie_df[filter_key] == filter_values[filter_key])
                    if i != 0:
                        result_filter = result_filter & tmp
                    i = i + 1
                    tmp = result_filter

            return all_movie_df[result_filter].T.to_dict()
        except KeyError:
            return {}


def search_show_by_filter(show_list: List[Show], filter_values: dict):
    global __result_filter, __tmp, __i
    show_list = pd.DataFrame(show_list)
    print(show_list)
    __i = 0
    try:
        for filter_key in filter_values.keys():
            # print(filter_values[filter_key])
            if filter_values[filter_key] != "":
                if filter_key == "Seat":
                    __result_filter = (show_list[filter_key] >= int(filter_values[filter_key]))
                elif filter_key == "Date":
                    __result_filter = (show_list[filter_key] == int(filter_values[filter_key]))
                else:
                    __result_filter = (show_list[filter_key] == filter_values[filter_key])

                if __i != 0:
                    __result_filter = __result_filter & __tmp
                __i = __i + 1
                __tmp = __result_filter
        print(show_list[__result_filter].T.to_dict())
        return show_list[__result_filter].T.to_dict()
    except KeyError:
        return {}
