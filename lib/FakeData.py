from lib.Catalog import Catalog
from lib.Movie import Movie

my_movie = Movie(
        "TITLE", "DESCRIPTION", 30, "TR", 2012, "Turkey", "HORROR", "ME"
    )
my_movie2 = Movie(
        "TITLE2", "DESCRIPTION2", 31, "TR", 2013, "Turkey", "HORROR2", "ME2"
    )
my_catalog = Catalog()
my_catalog.add_movie(my_movie)
my_catalog.add_movie(my_movie2)