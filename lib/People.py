from abc import ABC

from lib.Constants import AccountStatus, Address
from lib.Customer import Booking
# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self,
                 user_id: str,
                 password: str,
                 status: AccountStatus):
        self.__user_id = user_id
        self.__password = password
        self.__status = status

    def reset_password(self):
        None

    def get_password(self):
        return self.__password

    def get_user_id(self):
        return self.__user_id

    def get_status(self):
        return self.__status


class Person(ABC):
    def __init__(self,
                 name: str,
                 address: Address,
                 email: str,
                 phone: str,
                 account: Account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account

    def get_name(self):
        return self.__name

    def __str__(self):
        return str(self.__account.get_user_id())


class Customer(Person):
    def __init__(self,
                 name: str,
                 address: Address,
                 email: str,
                 phone: str,
                 account: Account):
        super().__init__(name, address, email, phone, account)
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account
        self.__bookings = []

    # def compare_accounts(self,
    #                      compare_with: Account):
    #     if (self.__account.get_user_id() == compare_with.get_user_id()) &&
    #         self.__account.get_password() == compare_with.get_password():
    #         return True
    #
    #     return False

    def get_account(self):
        return self.__account

    def make_booking(self, booking: Booking):
        self.__bookings.append(booking)

    def get_bookings(self):
        return self.__bookings


class Admin(Person):
    def add_movie(self, movie):
        None

    def add_show(self, show):
        None

    def block_user(self, customer):
        None


class Guest:
    def register_account(self):
        None
