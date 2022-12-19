import datetime
from Data.FakeCinema import cinemas_dict
from lib.Catalog import Catalog
from lib.Movie import Movie, Show
import lib.Customer as Customer

# --------------------------Movie Catalog----------------------------------
movie_catalog = Catalog()

harry_potter = Movie(
    "Harry Potter", "DESCRIPTION", 30, "TR", 2012, "England", "Fantasy", "ME", "images"
)
the_end = Movie(
    "The End", "DESCRIPTION2", 31, "EN", 2013, "England", "Action", "ME2", "images"
)
avengers = Movie(
    "Avengers", "DESCRIPTION2", 31, "EN", 2013, "USA", "Action", "ME2", "images"
)
movie_catalog.add_movie(harry_potter)
movie_catalog.add_movie(the_end)
movie_catalog.add_movie(avengers)
# ---------------------------------------------------------------------------------------------

# -------------------------Show List---------------------------
tin_cinema = cinemas_dict["Tin Cinema"]
print(tin_cinema)
tin_cinema_halls = tin_cinema.get_cinema_halls()
print(tin_cinema_halls["A"])
# Creating Show
show1 = Show(tin_cinema_halls["A"], harry_potter, datetime.datetime(2022, 12, 24, 13, 10, 40))
show2 = Show(tin_cinema_halls["B"], the_end, datetime.datetime(2022, 12, 21, 10, 50))
show3 = Show(tin_cinema_halls["C"], avengers, datetime.datetime(2022, 12, 23, 13, 20))
show_list = [show1.to_dict(),
             show2.to_dict(),
             show3.to_dict()
             ]
# --------------------------------------------------------------


