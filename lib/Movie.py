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
                 city: str,
                 genre: str,
                 added_by: Admin,
                 image: str):
        self.image = image
        self.title = title
        self.description = description
        self.duration_in_mins = duration_in_mins
        self.language = language
        self.release_date = release_date
        self.city = city
        self.genre = genre
        self.movie_added_by = added_by
        self.shows = []

    def to_dict(self):
        tmp_dict = {'Title': self.title,
                    'Language': self.language,
                    "Rel_date": self.release_date,
                    "City": self.city,
                    "Genre": self.genre}
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
        self.__end_time = start_time + datetime.timedelta(minutes=self.__movie.duration_in_mins)

    def get_cinema_hall(self):
        return self.__played_at

    def to_dict(self):
        tmp_dict = {'Played_at': self.__played_at,
                    'Seat':self.__played_at.seats_available(),
                    'Title': self.__movie.title,
                    'Language': self.__movie.language,
                    "Rel_date": self.__movie.release_date,
                    "City": self.__movie.city,
                    "Genre": self.__movie.genre}
        return tmp_dict
