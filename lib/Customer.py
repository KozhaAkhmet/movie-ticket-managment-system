from datetime import datetime
from lib.Cinema import CinemaHallSeat
from lib.Constants import BookingStatus,PaymentStatus
from lib.Movie import Show
from abc import ABC, abstractmethod


class ShowSeat(CinemaHallSeat):
    def __init__(self, id, is_reserved, price, seat_type):
        super().__init__(id, seat_type)
        self.__show_seat_id = id
        self.__is_reserved = is_reserved
        self.__price = price


class Payment(ABC):
    def __init__(self,
                 amount,
                 transaction_id: int,
                 payment_status: PaymentStatus):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status


class CreditCardTransaction(Payment):
    def __init__(self, name_on_card: str, amount, transaction_id, payment_status):
        super().__init__(amount, transaction_id, payment_status)
        self.__name_on_card = name_on_card


class CashTransaction(Payment):
    def __init__(self, amount, transaction_id, payment_status):
        super().__init__(amount, transaction_id, payment_status)


class Booking:
    def __init__(self, booking_number: str,
                 number_of_seats: int,
                 status: BookingStatus,
                 show: Show,
                 show_seats, payment: Payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def make_payment(self, payment):
        None

    def cancel(self):
        None

    def assign_seats(self, seats):
        None
