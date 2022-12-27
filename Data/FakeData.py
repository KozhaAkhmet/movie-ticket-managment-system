import datetime
import random
import calendar
from Data.FakeCinema import cinemas_dict
from lib.Catalog import Catalog
from lib.Movie import Movie, Show
import lib.Customer as Customer

# --------------------------Movie Catalog----------------------------------
movie_catalog = Catalog()

movies = [
Movie("Minions", "Descriptionnnnn", 91.0, "EN", 2001, "Saudi Arabia", "Western", "ME", "images"),
Movie("Big Hero 6", "Descriptionnnnn", 102.0, "EN", 1990, "Australia", "Romance", "ME", "images"),
Movie("Deadpool", "Descriptionnnnn", 108.0, "EN", 2004, "South Korea", "War", "ME", "images"),
Movie("Guardians of the Galaxy Vol. 2", "Descriptionnnnn", 137.0, "EN", 2014, "South Korea", "Fantasy", "ME", "images"),
Movie("Avatar", "Descriptionnnnn", 162.0, "EN", 2004, "China", "TV Movie", "ME", "images"),
Movie("John Wick", "Descriptionnnnn", 101.0, "EN", 2018, "Germany", "Crime", "ME", "images"),
Movie("Gone Girl", "Descriptionnnnn", 145.0, "EN", 1986, "Iran", "Drama", "ME", "images"),
Movie("The Hunger Games: Mockingjay - Part 1", "Descriptionnnnn", 123.0, "EN", 1988, "South Korea", "Foreign", "ME", "images"),
Movie("Captain America: Civil War", "Descriptionnnnn", 147.0, "EN", 1995, "Spain", "Fantasy", "ME", "images"),
Movie("Pulp Fiction", "Descriptionnnnn", 154.0, "EN", 1996, "Russia", "Music", "ME", "images"),
Movie("Pirates of the Caribbean: Dead Men Tell No Tales", "Descriptionnnnn", 129.0, "EN", 1982, "China", "Science Fiction", "ME", "images"),
Movie("The Dark Knight", "Descriptionnnnn", 152.0, "EN", 1993, "UK", "Thriller", "ME", "images"),
Movie("Blade Runner", "Descriptionnnnn", 117.0, "EN", 2011, "India", "Horror", "ME", "images"),
Movie("The Avengers", "Descriptionnnnn", 143.0, "EN", 2013, "Egypt", "Drama", "ME", "images"),
Movie("The Maze Runner", "Descriptionnnnn", 113.0, "EN", 2008, "Brazil", "Foreign", "ME", "images"),
Movie("Dawn of the Planet of the Apes", "Descriptionnnnn", 130.0, "EN", 1990, "Egypt", "Action", "ME", "images"),
Movie("Whiplash", "Descriptionnnnn", 105.0, "EN", 1984, "South Korea", "Fantasy", "ME", "images"),
Movie("Fight Club", "Descriptionnnnn", 139.0, "EN", 2012, "Japan", "Music", "ME", "images"),
Movie("Thor: Ragnarok", "Descriptionnnnn", 0.0, "EN", 1992, "Nigeria", "Thriller", "ME", "images"),
Movie("Guardians of the Galaxy", "Descriptionnnnn", 121.0, "EN", 2010, "Saudi Arabia", "Drama", "ME", "images"),
Movie("The Shawshank Redemption", "Descriptionnnnn", 142.0, "EN", 2015, "Spain", "Romance", "ME", "images"),
Movie("Forrest Gump", "Descriptionnnnn", 142.0, "EN", 1994, "Japan", "Mystery", "ME", "images"),
Movie("Pirates of the Caribbean: The Curse of the Black Pearl", "Descriptionnnnn", 143.0, "EN", 2002, "UK", "Mystery", "ME", "images"),
Movie("Doctor Strange", "Descriptionnnnn", 115.0, "EN", 1985, "Canada", "TV Movie", "ME", "images"),
Movie("Suicide Squad", "Descriptionnnnn", 123.0, "EN", 2005, "Egypt", "Comedy", "ME", "images"),
Movie("Star Wars", "Descriptionnnnn", 121.0, "EN", 1984, "Iran", "Science Fiction", "ME", "images"),
Movie("Ted 2", "Descriptionnnnn", 115.0, "EN", 1992, "Spain", "War", "ME", "images"),
Movie("Rise of the Planet of the Apes", "Descriptionnnnn", 105.0, "EN", 2016, "Brazil", "Documentary", "ME", "images"),
Movie("Maze Runner: The Scorch Trials", "Descriptionnnnn", 132.0, "EN", 2017, "Canada", "TV Movie", "ME", "images"),
Movie("The Godfather", "Descriptionnnnn", 175.0, "EN", 1995, "Russia", "Action", "ME", "images"),
Movie("Fantastic Beasts and Where to Find Them", "Descriptionnnnn", 133.0, "EN", 1993, "China", "Comedy", "ME", "images"),
Movie("Spirited Away", "Descriptionnnnn", 125.0, "JA", 2009, "Nigeria", "Foreign", "ME", "images"),
Movie("Life Is Beautiful", "Descriptionnnnn", 116.0, "IT", 2006, "South Korea", "Romance", "ME", "images"),
Movie("Avengers: Age of Ultron", "Descriptionnnnn", 141.0, "EN", 1982, "India", "Comedy", "ME", "images"),
Movie("Psycho", "Descriptionnnnn", 109.0, "EN", 2005, "Egypt", "War", "ME", "images"),
Movie("Fury", "Descriptionnnnn", 135.0, "EN", 2008, "Turkey", "Drama", "ME", "images"),
Movie("The Godfather: Part II", "Descriptionnnnn", 200.0, "EN", 2019, "Turkey", "Comedy", "ME", "images"),
Movie("Lucy", "Descriptionnnnn", 89.0, "EN", 1991, "Japan", "Romance", "ME", "images"),
Movie("Thor: The Dark World", "Descriptionnnnn", 112.0, "EN", 1985, "Egypt", "Western", "ME", "images"),
Movie("Dilwale Dulhania Le Jayenge", "Descriptionnnnn", 190.0, "HI", 2013, "Canada", "Animation", "ME", "images"),
Movie("The Mother of Tears", "Descriptionnnnn", 102.0, "IT", 2013, "Italy", "Romance", "ME", "images"),
Movie("The Twilight Saga: Eclipse", "Descriptionnnnn", 124.0, "EN", 2010, "UK", "Thriller", "ME", "images"),
Movie("Pacific Rim", "Descriptionnnnn", 131.0, "EN", 2018, "USA", "Western", "ME", "images"),
Movie("The Matrix", "Descriptionnnnn", 136.0, "EN", 1982, "Germany", "Animation", "ME", "images"),
Movie("Fifty Shades of Grey", "Descriptionnnnn", 125.0, "EN", 1996, "Nigeria", "Family", "ME", "images"),
Movie("Jurassic World", "Descriptionnnnn", 124.0, "EN", 1993, "South Korea", "TV Movie", "ME", "images"),
Movie("Interstellar", "Descriptionnnnn", 169.0, "EN", 2000, "Nigeria", "Comedy", "ME", "images"),
Movie("Once Upon a Time in America", "Descriptionnnnn", 229.0, "EN", 1992, "Italy", "Documentary", "ME", "images"),
Movie("The Lord of the Rings: The Fellowship of the Ring", "Descriptionnnnn", 178.0, "EN", 2018, "Spain", "War", "ME", "images"),
Movie("Edge of Tomorrow", "Descriptionnnnn", 113.0, "EN", 1996, "Saudi Arabia", "Comedy", "ME", "images"),
Movie("The Hobbit: The Battle of the Five Armies", "Descriptionnnnn", 144.0, "EN", 2019, "Iran", "War", "ME", "images"),
Movie("Star Wars: The Force Awakens", "Descriptionnnnn", 136.0, "EN", 2011, "Russia", "War", "ME", "images"),
Movie("The Imitation Game", "Descriptionnnnn", 113.0, "EN", 2004, "Iran", "Horror", "ME", "images"),
Movie("Batman v Superman: Dawn of Justice", "Descriptionnnnn", 151.0, "EN", 1995, "Japan", "Western", "ME", "images"),
Movie("Twilight", "Descriptionnnnn", 122.0, "EN", 2011, "USA", "Mystery", "ME", "images"),
Movie("The Amazing Spider-Man", "Descriptionnnnn", 136.0, "EN", 1993, "Spain", "Documentary", "ME", "images"),
Movie("12 Years a Slave", "Descriptionnnnn", 134.0, "EN", 1984, "Australia", "Mystery", "ME", "images"),
Movie("Chappie", "Descriptionnnnn", 120.0, "EN", 1994, "Mexico", "War", "ME", "images"),
Movie("Terminator Genisys", "Descriptionnnnn", 126.0, "EN", 1987, "Russia", "Mystery", "ME", "images"),
Movie("The Twilight Saga: New Moon", "Descriptionnnnn", 130.0, "EN", 2017, "Germany", "Foreign", "ME", "images"),
Movie("Harry Potter and the Chamber of Secrets", "Descriptionnnnn", 161.0, "EN", 1994, "Mexico", "War", "ME", "images"),
Movie("The Lord of the Rings: The Two Towers", "Descriptionnnnn", 179.0, "EN", 1993, "Canada", "Documentary", "ME", "images"),
Movie("Spider-Man", "Descriptionnnnn", 121.0, "EN", 1993, "Egypt", "Western", "ME", "images"),
Movie("Mad Max: Fury Road", "Descriptionnnnn", 120.0, "EN", 1987, "UK", "Western", "ME", "images"),
Movie("The Lord of the Rings: The Return of the King", "Descriptionnnnn", 201.0, "EN", 1986, "Iran", "History", "ME", "images"),
Movie("Thor", "Descriptionnnnn", 115.0, "EN", 1981, "France", "War", "ME", "images"),
Movie("Inception", "Descriptionnnnn", 148.0, "EN", 2007, "Russia", "Science Fiction", "ME", "images"),
Movie("X-Men: Apocalypse", "Descriptionnnnn", 144.0, "EN", 1989, "Germany", "TV Movie", "ME", "images"),
Movie("Batman Begins", "Descriptionnnnn", 140.0, "EN", 1985, "China", "Music", "ME", "images"),
Movie("Harry Potter and the Prisoner of Azkaban", "Descriptionnnnn", 141.0, "EN", 2018, "Spain", "History", "ME", "images"),
Movie("Kingsman: The Secret Service", "Descriptionnnnn", 130.0, "EN", 2009, "Iran", "Horror", "ME", "images"),
Movie("Pirates of the Caribbean: On Stranger Tides", "Descriptionnnnn", 136.0, "EN", 1989, "France", "Thriller", "ME", "images"),
Movie("Insurgent", "Descriptionnnnn", 119.0, "EN", 2001, "Russia", "Family", "ME", "images"),
Movie("The Purge: Anarchy", "Descriptionnnnn", 104.0, "EN", 1982, "Spain", "Drama", "ME", "images"),
Movie("Spider-Man 3", "Descriptionnnnn", 139.0, "EN", 2005, "Germany", "Comedy", "ME", "images"),
Movie("Sex Tape", "Descriptionnnnn", 97.0, "EN", 1994, "India", "Family", "ME", "images"),
Movie("Furious 7", "Descriptionnnnn", 137.0, "EN", 1983, "Russia", "Music", "ME", "images"),
Movie("Dark Skies", "Descriptionnnnn", 97.0, "EN", 2018, "China", "Science Fiction", "ME", "images"),
Movie("Titanic", "Descriptionnnnn", 194.0, "EN", 1981, "South Korea", "Music", "ME", "images"),
Movie("Ant-Man", "Descriptionnnnn", 117.0, "EN", 2003, "USA", "History", "ME", "images"),
Movie("The Hunger Games: Mockingjay - Part 2", "Descriptionnnnn", 137.0, "EN", 1993, "Australia", "Family", "ME", "images"),
Movie("Monsters, Inc.", "Descriptionnnnn", 92.0, "EN", 2019, "Turkey", "Family", "ME", "images"),
Movie("The Amazing Spider-Man 2", "Descriptionnnnn", 142.0, "EN", 1990, "South Korea", "Animation", "ME", "images"),
Movie("World War Z", "Descriptionnnnn", 116.0, "EN", 1996, "Germany", "TV Movie", "ME", "images"),
Movie("The Twilight Saga: Breaking Dawn - Part 2", "Descriptionnnnn", 115.0, "EN", 1987, "Saudi Arabia", "Foreign", "ME", "images"),
Movie("X-Men: Days of Future Past", "Descriptionnnnn", 131.0, "EN", 2015, "Russia", "Crime", "ME", "images"),
Movie("The Twilight Saga: Breaking Dawn - Part 1", "Descriptionnnnn", 117.0, "EN", 2008, "Russia", "Documentary", "ME", "images"),
Movie("Justice League", "Descriptionnnnn", 0.0, "EN", 2017, "Iran", "Documentary", "ME", "images"),
Movie("Back to the Future", "Descriptionnnnn", 116.0, "EN", 2000, "India", "Action", "ME", "images"),
Movie("The Martian", "Descriptionnnnn", 141.0, "EN", 1996, "Egypt", "Family", "ME", "images"),
Movie("Finding Nemo", "Descriptionnnnn", 100.0, "EN", 2016, "UK", "Crime", "ME", "images"),
Movie("The Hunger Games: Catching Fire", "Descriptionnnnn", 146.0, "EN", 2012, "USA", "Western", "ME", "images"),
Movie("Self/less", "Descriptionnnnn", 116.0, "EN", 1994, "USA", "Fantasy", "ME", "images"),
Movie("Kill Bill: Vol. 1", "Descriptionnnnn", 111.0, "EN", 1984, "Japan", "Comedy", "ME", "images"),
Movie("The Hangover Part III", "Descriptionnnnn", 100.0, "EN", 1990, "Nigeria", "Action", "ME", "images"),
Movie("Harry Potter and the Deathly Hallows: Part 2", "Descriptionnnnn", 130.0, "EN", 1988, "Saudi Arabia", "Comedy", "ME", "images"),
Movie("Spectre", "Descriptionnnnn", 148.0, "EN", 1995, "Australia", "Romance", "ME", "images"),
Movie("Harry Potter and the Goblet of Fire", "Descriptionnnnn", 157.0, "EN", 1985, "South Korea", "Thriller", "ME", "images"),
Movie("Despicable Me 2", "Descriptionnnnn", 98.0, "EN", 2005, "UK", "History", "ME", "images"),
Movie("No Good Deed", "Descriptionnnnn", 83.0, "EN", 2002, "Saudi Arabia", "History", "ME", "images"),
Movie("The Fifth Element", "Descriptionnnnn", 126.0, "EN", 1982, "China", "Family", "ME", "images"),
Movie("Frozen", "Descriptionnnnn", 102.0, "EN", 2002, "Russia", "Western", "ME", "images"),
Movie("Inside Out", "Descriptionnnnn", 94.0, "EN", 2018, "Russia", "Comedy", "ME", "images"),
Movie("The Mummy", "Descriptionnnnn", 124.0, "EN", 1998, "Brazil", "Music", "ME", "images"),
Movie("Grown Ups", "Descriptionnnnn", 102.0, "EN", 2012, "China", "Family", "ME", "images"),
Movie("The Hangover", "Descriptionnnnn", 100.0, "EN", 2012, "Spain", "War", "ME", "images"),
Movie("Iron Man 3", "Descriptionnnnn", 130.0, "EN", 2015, "Russia", "Animation", "ME", "images"),
Movie("DragonHeart", "Descriptionnnnn", 103.0, "EN", 2015, "China", "Foreign", "ME", "images"),
Movie("Saw", "Descriptionnnnn", 103.0, "EN", 1999, "Australia", "History", "ME", "images"),
Movie("The Revenant", "Descriptionnnnn", 156.0, "EN", 2014, "Russia", "Western", "ME", "images"),
Movie("Beauty and the Beast", "Descriptionnnnn", 84.0, "EN", 2018, "South Korea", "Drama", "ME", "images"),
Movie("Alien", "Descriptionnnnn", 117.0, "EN", 2016, "Australia", "Documentary", "ME", "images"),
Movie("Harry Potter and the Deathly Hallows: Part 1", "Descriptionnnnn", 146.0, "EN", 1996, "UK", "Mystery", "ME", "images"),
Movie("The Hobbit: An Unexpected Journey", "Descriptionnnnn", 169.0, "EN", 2004, "Saudi Arabia", "Science Fiction", "ME", "images"),
Movie("Annabelle", "Descriptionnnnn", 99.0, "EN", 2014, "France", "TV Movie", "ME", "images"),
Movie("The Purge", "Descriptionnnnn", 86.0, "EN", 2006, "Canada", "History", "ME", "images"),
Movie("Gladiator", "Descriptionnnnn", 155.0, "EN", 1997, "Mexico", "Mystery", "ME", "images"),
Movie("Casino Royale", "Descriptionnnnn", 144.0, "EN", 1991, "India", "Science Fiction", "ME", "images"),
Movie("The Jungle Book", "Descriptionnnnn", 78.0, "EN", 2012, "Italy", "War", "ME", "images"),
Movie("Terminator 2: Judgment Day", "Descriptionnnnn", 137.0, "EN", 2000, "China", "TV Movie", "ME", "images"),
Movie("2001: A Space Odyssey", "Descriptionnnnn", 149.0, "EN", 1997, "Japan", "History", "ME", "images"),
Movie("Teenage Mutant Ninja Turtles", "Descriptionnnnn", 101.0, "EN", 1987, "Turkey", "Mystery", "ME", "images"),
Movie("Tomorrowland", "Descriptionnnnn", 130.0, "EN", 1996, "UK", "Action", "ME", "images"),
Movie("Despicable Me", "Descriptionnnnn", 95.0, "EN", 1993, "Japan", "Action", "ME", "images"),
Movie("The Incredibles", "Descriptionnnnn", 115.0, "EN", 2004, "Iran", "Crime", "ME", "images"),
Movie("Angels & Demons", "Descriptionnnnn", 138.0, "EN", 2016, "Brazil", "Mystery", "ME", "images"),
Movie("Penguins of Madagascar", "Descriptionnnnn", 92.0, "EN", 1984, "Germany", "Family", "ME", "images"),
Movie("Ghostbusters", "Descriptionnnnn", 107.0, "EN", 2002, "USA", "Mystery", "ME", "images"),
Movie("Iron Man", "Descriptionnnnn", 126.0, "EN", 1984, "Canada", "Music", "ME", "images"),
Movie("The Wizard of Oz", "Descriptionnnnn", 102.0, "EN", 1986, "Iran", "TV Movie", "ME", "images"),
Movie("Charlie and the Chocolate Factory", "Descriptionnnnn", 115.0, "EN", 2017, "Germany", "Horror", "ME", "images"),
Movie("Stonehearst Asylum", "Descriptionnnnn", 112.0, "EN", 1998, "USA", "TV Movie", "ME", "images"),
Movie("Toy Story", "Descriptionnnnn", 81.0, "EN", 1994, "Mexico", "Crime", "ME", "images"),
Movie("The Hangover Part II", "Descriptionnnnn", 102.0, "EN", 1994, "UK", "Science Fiction", "ME", "images"),
Movie("Aliens", "Descriptionnnnn", 137.0, "EN", 2007, "Brazil", "TV Movie", "ME", "images"),
Movie("Saving Private Ryan", "Descriptionnnnn", 169.0, "EN", 1986, "Egypt", "Science Fiction", "ME", "images"),
Movie("Seven Pounds", "Descriptionnnnn", 123.0, "EN", 1981, "Iran", "History", "ME", "images"),
Movie("The Lion King", "Descriptionnnnn", 89.0, "EN", 2007, "UK", "Horror", "ME", "images"),
Movie("Divergent", "Descriptionnnnn", 139.0, "EN", 2005, "Russia", "War", "ME", "images"),
Movie("Kill Bill: Vol. 2", "Descriptionnnnn", 136.0, "EN", 1988, "Turkey", "Action", "ME", "images"),
Movie("Enigma", "Descriptionnnnn", 119.0, "EN", 1997, "Spain", "War", "ME", "images"),
Movie("Jupiter Ascending", "Descriptionnnnn", 124.0, "EN", 1999, "Australia", "Romance", "ME", "images"),
Movie("Harry Potter and the Order of the Phoenix", "Descriptionnnnn", 138.0, "EN", 2001, "Brazil", "Comedy", "ME", "images"),
Movie("Cast Away", "Descriptionnnnn", 143.0, "EN", 2005, "South Korea", "Comedy", "ME", "images"),
Movie("Nightcrawler", "Descriptionnnnn", 117.0, "EN", 1989, "South Korea", "Music", "ME", "images"),
Movie("TRON: Legacy", "Descriptionnnnn", 125.0, "EN", 1994, "Egypt", "Foreign", "ME", "images"),
Movie("Straight Outta Compton", "Descriptionnnnn", 147.0, "EN", 1986, "USA", "Foreign", "ME", "images"),
Movie("Mulan", "Descriptionnnnn", 88.0, "EN", 1986, "Iran", "War", "ME", "images"),
Movie("Pixels", "Descriptionnnnn", 105.0, "EN", 1991, "Germany", "Drama", "ME", "images"),
Movie("The Key", "Descriptionnnnn", 110.0, "IT", 1988, "Iran", "History", "ME", "images"),
Movie("The Bourne Identity", "Descriptionnnnn", 119.0, "EN", 2013, "India", "Music", "ME", "images"),
Movie("The Pursuit of Happyness", "Descriptionnnnn", 117.0, "EN", 2018, "Australia", "Animation", "ME", "images"),
Movie("Horrible Bosses 2", "Descriptionnnnn", 108.0, "EN", 1985, "India", "Drama", "ME", "images"),
Movie("Terminator 3: Rise of the Machines", "Descriptionnnnn", 109.0, "EN", 1986, "Japan", "TV Movie", "ME", "images"),
Movie("Braveheart", "Descriptionnnnn", 177.0, "EN", 1984, "Brazil", "Fantasy", "ME", "images"),
Movie("American Beauty", "Descriptionnnnn", 122.0, "EN", 2013, "Australia", "Foreign", "ME", "images"),
Movie("Scouts Guide to the Zombie Apocalypse", "Descriptionnnnn", 93.0, "EN", 2003, "UK", "Mystery", "ME", "images"),
Movie("Minority Report", "Descriptionnnnn", 145.0, "EN", 2008, "France", "Documentary", "ME", "images"),
Movie("Star Trek Beyond", "Descriptionnnnn", 122.0, "EN", 2018, "Saudi Arabia", "War", "ME", "images"),
Movie("The Hobbit: The Desolation of Smaug", "Descriptionnnnn", 161.0, "EN", 1999, "Japan", "Action", "ME", "images"),
Movie("Underworld", "Descriptionnnnn", 121.0, "EN", 1993, "Nigeria", "Science Fiction", "ME", "images"),
Movie("Sin City: A Dame to Kill For", "Descriptionnnnn", 102.0, "EN", 1982, "Italy", "Romance", "ME", "images"),
Movie("The Dark Knight Rises", "Descriptionnnnn", 165.0, "EN", 2006, "France", "Romance", "ME", "images"),
Movie("San Andreas", "Descriptionnnnn", 114.0, "EN", 1983, "UK", "Fantasy", "ME", "images"),
Movie("Ratatouille", "Descriptionnnnn", 111.0, "EN", 1984, "Mexico", "Family", "ME", "images"),
Movie("Beautiful Creatures", "Descriptionnnnn", 124.0, "EN", 1992, "Saudi Arabia", "Foreign", "ME", "images"),
Movie("Leon: The Professional", "Descriptionnnnn", 110.0, "FR", 2009, "Brazil", "Crime", "ME", "images"),
Movie("The Bourne Supremacy", "Descriptionnnnn", 108.0, "EN", 1998, "South Korea", "Drama", "ME", "images"),
Movie("It Follows", "Descriptionnnnn", 100.0, "EN", 1987, "Spain", "Comedy", "ME", "images"),
Movie("Amazing Grace", "Descriptionnnnn", 117.0, "EN", 2009, "Saudi Arabia", "Action", "ME", "images"),
Movie("The Hateful Eight", "Descriptionnnnn", 167.0, "EN", 1998, "Brazil", "Documentary", "ME", "images"),
Movie("Skyfall", "Descriptionnnnn", 143.0, "EN", 1983, "Brazil", "Action", "ME", "images"),
Movie("Top Gun", "Descriptionnnnn", 110.0, "EN", 1998, "Turkey", "War", "ME", "images"),
Movie("V for Vendetta", "Descriptionnnnn", 132.0, "EN", 1993, "Canada", "Romance", "ME", "images"),
Movie("The Hunger Games", "Descriptionnnnn", 142.0, "EN", 1988, "China", "Fantasy", "ME", "images"),
Movie("Derailed", "Descriptionnnnn", 89.0, "EN", 1997, "Italy", "Animation", "ME", "images"),
Movie("The Green Mile", "Descriptionnnnn", 189.0, "EN", 2003, "UK", "Family", "ME", "images"),
Movie("Crouching Tiger, Hidden Dragon", "Descriptionnnnn", 120.0, "ZH", 2017, "Spain", "Animation", "ME", "images"),
Movie("Dr. No", "Descriptionnnnn", 110.0, "EN", 2008, "Brazil", "Documentary", "ME", "images"),
Movie("War of the Worlds", "Descriptionnnnn", 116.0, "EN", 1997, "China", "Crime", "ME", "images"),
Movie("Dead Poets Society", "Descriptionnnnn", 129.0, "EN", 2002, "Iran", "Foreign", "ME", "images"),
Movie("Raiders of the Lost Ark", "Descriptionnnnn", 115.0, "EN", 1993, "Turkey", "Science Fiction", "ME", "images"),
Movie("The Woman in Red", "Descriptionnnnn", 87.0, "EN", 2012, "Turkey", "Romance", "ME", "images"),
Movie("Catch Me If You Can", "Descriptionnnnn", 141.0, "EN", 1991, "Spain", "Drama", "ME", "images"),
Movie("Equals", "Descriptionnnnn", 101.0, "EN", 2001, "Japan", "Crime", "ME", "images"),
Movie("Cinderella", "Descriptionnnnn", 105.0, "EN", 1986, "Germany", "War", "ME", "images"),
Movie("Django Unchained", "Descriptionnnnn", 165.0, "EN", 2002, "UK", "Family", "ME", "images"),
Movie("King Kong", "Descriptionnnnn", 187.0, "EN", 2011, "USA", "Foreign", "ME", "images"),
Movie("Jaws", "Descriptionnnnn", 124.0, "EN", 2013, "Australia", "TV Movie", "ME", "images"),
Movie("Factory Girl", "Descriptionnnnn", 90.0, "EN", 2010, "USA", "Fantasy", "ME", "images"),
Movie("Non-Stop", "Descriptionnnnn", 106.0, "EN", 1981, "South Korea", "History", "ME", "images"),
Movie("Harry Potter", "DESCRIPTION", 30, "TR", 2012, "England", "Fantasy", "ME", "images"),
Movie("The End", "DESCRIPTION2", 31, "EN", 2013, "England", "Action", "ME2", "images"),
Movie("Avengers", "DESCRIPTION2", 31, "EN", 2013, "USA", "Action", "ME2", "images")
]

for movie in movies:
    movie_catalog.add_movie(movie)
# ---------------------------------------------------------------------------------------------

# -------------------------Show List---------------------------
tin_cinema = cinemas_dict["Tin Cinema"]
print(tin_cinema)
tin_cinema_halls = tin_cinema.get_cinema_halls()
print(tin_cinema_halls["A"])
# Creating Show
shows = []
for movie in movies:

    year = random.randint(2022, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, calendar.monthrange(year, month)[1])
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    random_date = datetime.datetime(year, month, day, hour, minute, second)

    random_hall = random.choice(list(tin_cinema_halls.keys()))

    show = Show(tin_cinema_halls[random_hall], movie, random_date)
    shows.append(show.to_dict())

show_list = shows
# --------------------------------------------------------------

booking_list = []

