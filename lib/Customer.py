import datetime
from typing import List

from lib.Cinema import CinemaHallSeat
from lib.Constants import BookingStatus, PaymentStatus, SeatType
from lib.Movie import Show
import lib.Constants as Constants


class ShowSeat(CinemaHallSeat):
    def __init__(self, seat_number: int,
                 is_reserved: bool,
                 price: float,
                 seat_row: int,
                 seat_coulomn: int,
                 seat_type: SeatType):
        super().__init__(seat_row, seat_coulomn, seat_type)
        self.__show_seat_number = seat_number
        self.__is_reserved = is_reserved
        self.__price = price


class Payment:
    def __init__(self,
                 amount,
                 transaction_id: int,
                 payment_status: PaymentStatus):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status


class Booking:
    def __init__(self, booking_number: str,
                 number_of_seats: int,
                 status: BookingStatus,
                 show: Show,
                 show_seats: ShowSeat,
                 payment: Payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def make_payment(self, payment: Payment):
        pass

    def cancel(self):
        None

    def assign_seats(self, seats):
        None
