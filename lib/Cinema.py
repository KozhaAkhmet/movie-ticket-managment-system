from typing import List, Dict

from lib.Constants import Address, SeatType


class City:
    def __init__(self,
                 name: str,
                 state: str,
                 zip_code: str):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code


class CinemaHallSeat:
    def __init__(self,
                 seat_row: int,
                 seat_coulomn: int,
                 seat_type: SeatType):
        self.__seat_row = seat_row
        self.__seat_coulomn = seat_coulomn
        self.__seat_type = seat_type

    def get_seat_row(self):
        return self.__seat_row

    def get_seat_coulomn(self):
        return self.__seat_coulomn

    def get_seat_type(self):
        return self.__seat_type

    def set_seat_type(self, value: SeatType):
        self.__seat_type = value

    def __str__(self):
        return f"Row: {self.__seat_row}  Coulomn: {self.__seat_coulomn}  Type: {self.__seat_type}"


class CinemaHall:
    def __init__(self,
                 name: str,
                 total_row: int,
                 total_coulomn: int,
                 cinema_halls_seats: List):
        self.__name = name
        self.__total_seats = total_row * total_coulomn
        self.__total_row = total_row
        self.__total_coulomn = total_coulomn
        self.__cinema_halls_seats = cinema_halls_seats

    def get_name(self):
        return f"Hall '{self.__name}'"

    def get_total_sets(self):
        return self.__total_seats

    def get_total_row(self):
        return self.__total_row

    def get_total_coulomn(self):
        return self.__total_coulomn

    def get_cinema_hall_seats(self) -> List:
        return self.__cinema_halls_seats

    def seats_available(self):
        available_seats = 0
        for i in self.__cinema_halls_seats:
            if i.get_seat_type() == SeatType.ACCESSIBLE:
                available_seats = available_seats + 1
        return available_seats


class Cinema:
    def __init__(self, name: str,
                 total_cinema_halls: int,
                 address: Address,
                 halls: Dict[str, CinemaHall]):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
        self.__location = address
        self.__halls = halls

    def get_cinema_halls(self):
        return self.__halls

    def __str__(self):
        return "Cinema: " + self.__name + "| Total halls: " + str(self.__total_cinema_halls)
