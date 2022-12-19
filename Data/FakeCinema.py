import datetime
from typing import List

from lib.Catalog import Catalog
from lib.Movie import Movie, Show
from lib.Cinema import Cinema, CinemaHall, CinemaHallSeat
import lib.Customer as Customer
from lib.Constants import BookingStatus, PaymentStatus, Address, SeatType

# ----------------------------Creating Cinema--------------------------------------

# -----------Cinema Hall A

cinema_hall_A_seats = []
# 5 * 2 = 10 !!!
cinema_hall_A_row_size = 5
cinema_hall_A_coulomn_size = 2
# i ve j birden baslatmak lazim
for i in range(cinema_hall_A_row_size):
    for j in range(cinema_hall_A_coulomn_size):
        tmp_seat = CinemaHallSeat(i, j, SeatType.ACCESSIBLE)
        cinema_hall_A_seats.append(tmp_seat)
cinema_hall_A = CinemaHall("A", 10, cinema_hall_A_seats)

# -----------Cinema Hall B

cinema_hall_B_seats = []
cinema_hall_B_row_size = 5
cinema_hall_B_coulomn_size = 4
# i ve j birden baslatmak lazim
for i in range(cinema_hall_B_row_size):
    for j in range(cinema_hall_B_coulomn_size):
        tmp_seat = CinemaHallSeat(i, j, SeatType.ACCESSIBLE)
        cinema_hall_B_seats.append(tmp_seat)
cinema_hall_B = CinemaHall("B", 20, cinema_hall_B_seats)

# -----------Cinema Hall C

cinema_hall_C_seats = []
cinema_hall_C_row_size = 5
cinema_hall_C_coulomn_size = 3
# i ve j birden baslatmak lazim
for i in range(cinema_hall_C_row_size):
    for j in range(cinema_hall_C_coulomn_size):
        tmp_seat = CinemaHallSeat(i, j, SeatType.ACCESSIBLE)
        cinema_hall_C_seats.append(tmp_seat)
cinema_hall_C = CinemaHall("C", 15, cinema_hall_C_seats)

# -------------Cinema Hall D

cinema_hall_D_seats = []
cinema_hall_D_row_size = 5
cinema_hall_D_coulomn_size = 2
# i ve j birden baslatmak lazim
for i in range(cinema_hall_D_row_size):
    for j in range(cinema_hall_D_coulomn_size):
        tmp_seat = CinemaHallSeat(i, j, SeatType.ACCESSIBLE)
        cinema_hall_D_seats.append(tmp_seat)
cinema_hall_D = CinemaHall("D", 10, cinema_hall_D_seats)

# -------------Cinema Hall E

cinema_hall_E_seats = []
cinema_hall_E_row_size = 5
cinema_hall_E_coulomn_size = 3
# i ve j birden baslatmak lazim
for i in range(cinema_hall_E_row_size):
    for j in range(cinema_hall_E_coulomn_size):
        tmp_seat = CinemaHallSeat(i, j, SeatType.ACCESSIBLE)
        cinema_hall_E_seats.append(tmp_seat)
cinema_hall_E = CinemaHall("E", 15, cinema_hall_E_seats)

# --------------Tin Cinema
cinema_halls_dict = {"A": cinema_hall_A,
                     "B": cinema_hall_B,
                     "C": cinema_hall_C,
                     "D": cinema_hall_D,
                     "E": cinema_hall_E}

address = Address("Piri Reis", "Istanbul", "Esenler", "asda", "Turkey")

cinemas_dict = {
    "Tin Cinema": Cinema("Tin Cinema", cinema_halls_dict.__len__(), address=address, halls=cinema_halls_dict)}

# -----------------------------------------------------------------------
