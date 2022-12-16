from lib.Constants import Address, SeatType
from lib.Movie import Show


class City:
    def __init__(self,
                 name: str,
                 state: str,
                 zip_code: str):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code


class CinemaHall:
    def __init__(self,
                 name: str,
                 total_seats: int,
                 shows: Show):
        self.__name = name
        self.__total_seats = total_seats
        self.__shows = shows


class Cinema:
    def __init__(self, name: str,
                 total_cinema_halls: int,
                 address: Address,
                 halls: CinemaHall):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
        self.__location = address
        self.__halls = halls


class CinemaHallSeat:
    def __init__(self,
                 seat_row: int,
                 seat_coulomn: int,
                 seat_type: SeatType):
        self.__seat_row = seat_row
        self.__seat_coulomn = seat_coulomn
        self.__seat_type = seat_type
