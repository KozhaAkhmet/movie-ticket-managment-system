import datetime
from lib.People import Admin
from lib.Cinema import CinemaHall


class Movie:

    def __str__(self) -> str:
        return "{" + self.title + "," + self.genre + "," + self.description + "}"

    def __init__(self, title: str,
                 description: str,
                 duration_in_mins: int,
                 language: str,
                 release_date: datetime,
                 country: str,
                 genre: str,
                 added_by: Admin,
                 image: str):
        self.__image = image
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country  # Turkey
        self.__genre = genre
        self.__movie_added_by = added_by
        self.__shows = []

    def get_title(self):
        return self.__title

    def get_language(self):
        return self.__language

    def get_rel_date(self):
        return self.__release_date

    def get_genre(self):
        return self.__genre

    def get_country(self):
        return self.__country

    def get_duration(self):
        return self.__duration_in_mins

    def to_dict(self):
        tmp_dict = {'Title': self.__title,
                    'Language': self.__language,
                    "Rel_date": self.__release_date,
                    "Country": self.__country,
                    "Genre": self.get_genre()}
        return tmp_dict


class Show:
    def __init__(self,
                 played_at: CinemaHall,
                 movie: Movie,
                 start_time: datetime.datetime
                 ):
        self.__created_on = datetime.date.today()
        self.__start_time = start_time
        self.__played_at = played_at
        self.__movie = movie
        # TODO endtime = start_time + movie_duration but with correct types
        self.__end_time = start_time + datetime.timedelta(minutes=self.__movie.get_duration())

    def get_cinema_hall(self):
        return self.__played_at

    def get_date(self):
        return self.__start_time

    def to_dict(self):
        tmp_dict = {'Played_at': self.__played_at,
                    'Seat': self.__played_at.seats_available(),
                    'Title': self.__movie.get_title(),
                    'Language': self.__movie.get_language(),
                    "Rel_date": self.__movie.get_rel_date(),
                    "Country": self.__movie.get_country(),
                    "Genre": self.__movie.get_genre(),
                    "Date": self.__start_time.date().day}
        return tmp_dict
