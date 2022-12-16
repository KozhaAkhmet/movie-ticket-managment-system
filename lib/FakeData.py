import datetime
from typing import List

from lib.Catalog import Catalog
from lib.Movie import Movie,Show
from lib.Cinema import Cinema,CinemaHall,CinemaHallSeat
import lib.Customer as Customer
from lib.Constants import BookingStatus,PaymentStatus,Address,SeatType

movie_catalog = Catalog()

my_movie = Movie(
        "Harry Potter", "DESCRIPTION", 30, "TR", 2012, "England", "Fantasy", "ME","images"
    )
my_movie2 = Movie(
        "The End", "DESCRIPTION2", 31, "EN", 2013, "England", "Action", "ME2","images"
    )

movie_catalog.add_movie(my_movie)
movie_catalog.add_movie(my_movie2)



# Creating Cinema
address = Address("Piri Reis", "Istanbul", "Esenler", "asda", "Turkey")

# Cinema Hall
cinema_hall_1 = CinemaHall("1",10)
cinema_hall_1_seats = []
seat1 =  CinemaHallSeat(1,1,SeatType.ACCESSIBLE)
cinema_hall_1_seats.append(seat1)

# Creating Show
show1 = Show(cinema_hall_1,my_movie,datetime.date(2022,12,23),datetime.date(2022,12,31))
show_list = [show1]

Cinema("Tin Cinema",5,address=address,halls=cinema_hall_1)

# The customer
test_customer = Customer

# Making Booking
payment = test_customer.Payment(amount=100, transaction_id=123, payment_status=PaymentStatus.PENDING)
test_customer.Booking("123",2,BookingStatus.CONFIRMED,show1,cinema_hall_1_seats[0],payment)

# Making payment


CinemaHall(name="Tim Sinema", total_seats= 20)