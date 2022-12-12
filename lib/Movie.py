from datetime import datetime

from lib import People


class Show:
    def __init__(self, id, played_at, movie, start_time, end_time):
        self.__show_id = id
        self.__created_on = datetime.date.today()
        self.__start_time = start_time
        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie


class Movie:
    def __init__(self, title: str,
                 description: str,
                 duration_in_mins: int,
                 language: str, release_date: datetime,
                 city: str,
                 genre: str,
                 added_by: People.Admin):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__city = city
        self.__genre = genre
        self.__movie_added_by = added_by

        self.__shows = []
