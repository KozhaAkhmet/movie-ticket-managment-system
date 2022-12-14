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

    def __str__(self) -> str:
        return "{" + self.title + "," + self.genre + "," + self.description + "}"

    def __init__(self, title: str,
                 description: str,
                 duration_in_mins: int,
                 language: str,
                 release_date: datetime,
                 city: str,
                 genre: str,
                 added_by: People.Admin):
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
