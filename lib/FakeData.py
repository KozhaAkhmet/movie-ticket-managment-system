from lib.Catalog import Catalog
from lib.Movie import Movie
import lib.Cinema as Cinema
import lib.Customer as Customer

movie_catalog = Catalog()
my_movie = Movie(
        "TITLE", "DESCRIPTION", 30, "TR", 2012, "Turkey", "HORROR", "ME","images"
    )
my_movie2 = Movie(
        "TITLE2", "DESCRIPTION2", 31, "TR", 2013, "Turkey", "HORROR2", "ME2","images"
    )

movie_catalog.add_movie(my_movie)
movie_catalog.add_movie(my_movie2)

test_customer = Customer
test_customer.Booking()

Cinema.CinemaHall(name="Tim Sinema", total_seats= 20, shows=)