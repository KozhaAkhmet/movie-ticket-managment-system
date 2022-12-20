import datetime
from typing import List

from lib.Cinema import CinemaHallSeat
from lib.Constants import BookingStatus, PaymentStatus, SeatType
# from lib.Movie import Show
import lib.Constants as Constants


class ShowSeat(CinemaHallSeat):
    def __init__(self, seat_id: int,
                 is_reserved: bool,
                 price: float,
                 seat_row: int,
                 seat_coulomn: int,
                 seat_type: SeatType):
        super().__init__(seat_row, seat_coulomn, seat_type)
        self.__show_seat_number = seat_id
        self.__is_reserved = is_reserved
        self.__price = price

    def get_price(self):
        return self.__price

    def print(self):
        return f"Row: {super().get_seat_row()}  Coulomn: {super().get_seat_coulomn()}  " \
               f"Type: {super().get_seat_type()} Price: {self.__price}"


class Payment:
    def __init__(self,
                 amount,
                 transaction_id: int,
                 payment_status: PaymentStatus):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status

    def set_status(self, status):
        self.__status = status

    def get_amount(self):
        return self.__amount


class Booking:
    def __init__(self, booking_number: str,
                 number_of_seats: int,
                 status: BookingStatus,
                 show,
                 show_seats: List[ShowSeat],
                 payment: Payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def set_status(self, status):
        self.__status = status

    def make_payment(self, payment: Payment):
        pass

    def cancel(self):
        del self

    def assign_seats(self, seats: List[ShowSeat]):
        None

    def get_date(self):
        return self.__created_on

    def get_booking_number(self):
        return self.__booking_number

    def get_nuber_of_seats(self):
        return self.__number_of_seats

    def get_show(self):
        return self.__show

    def get_price(self):
        return self.__payment.get_amount()
