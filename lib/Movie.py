from datetime import datetime
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
                 start_time: datetime,
                 end_time: datetime):
        self.__created_on = datetime.date.today()
        self.__start_time = start_time
        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie
