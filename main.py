import datetime
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from typing import List

from lib.Cinema import CinemaHall, CinemaHallSeat
from lib import Catalog
from lib.People import Guest, Account, Customer
from lib.Constants import AccountStatus, SeatType, Address, PaymentStatus, BookingStatus
from lib.Customer import ShowSeat, Payment, Booking
from lib.Utility import control_str
# from src.SearchResult import search_result_ui

from Data.FakeData import show_list, booking_list
from Data.FakeAccounts import user_list

current_user = Guest()
current_datetime = datetime.datetime.now()
result_instance = []
user_frame_tmp = tk.Frame
show_instance = 4
selected = []


class BookingUI:
    def __init__(self, booking, frame, row):
        self.booking_label = tk.Label(frame, text="Booking", bg="#FAD8D6")
        self.booking_label.grid(row=row, column=0)

        self.booking_text = tk.Text(self.booking_label, height=5, width=50, bg="#f0f0f0")

        self.booking_text.insert("1.0",
                                 " Date: " + str(booking.get_date()) +
                                 "\n Booking Number: " + str(booking.get_booking_number()) +
                                 "\n Number of seats: " + str(booking.get_number_of_seats()) +
                                 "\n Show:" + str(booking.get_show()['Title']) +
                                 "\n Price: " + str(booking.get_price()))
        self.booking_text.config(state='disabled')
        self.booking_text.grid(row=row, column=0)

        def cancel_booking():
            self.booking_label.destroy()
            seats = booking.get_show_seats()
            for seat in seats:
                seat.set_seat_type(SeatType.ACCESSIBLE)
            current_user.cancel_booking(booking)
            booking_list.remove(booking)

        self.booking_button = tk.Button(self.booking_label, text="Cancel Booking", command=cancel_booking, bg="#890B59",
                                        fg="#FAD8D6")

        self.booking_button.grid(row=row, column=1)


class ViewBookings(tk.Frame):
    def __init__(self, bookings):

        self.window = tk.Toplevel(bg="#FAD8D6")

        self.window.title("Bookings")
        self.window.resizable(False, False)

        i = 0
        if len(bookings) == 0:
            self.window.destroy()
            showinfo(message="No bookings")
            return
        else:
            for booking in bookings:
                BookingUI(booking, self.window, i)
                i += 1

            self.back_button = tk.Button(self.window, text="Back", command=self.window.destroy, bg="#890B59",
                                         fg="#FAD8D6")

            self.back_button.grid(row=i + 1, column=0)


def update_user(user):
    frame = user_frame_tmp

    user_name_text = tk.Text(frame, height=2, width=30, bg="#f0f0f0")

    user_name_text.insert("1.0", f"Name {user.get_name()}"
                                 f"\nStatus {user.get_account().get_status()} ")
    user_name_text.config(state='disabled')
    user_name_text.grid(row=0, column=0)

    def view_bookings():
        ViewBookings(user.get_bookings())

    user_booking_button = tk.Button(frame, text="View Booking", command=view_bookings, fg="#FAD8D6", bg="#890B59")

    user_booking_button.grid(row=1, column=0)
    global current_user
    current_user = user
    print(current_user)


class MakeBooking(tk.Frame):
    def __init__(self, show):
        global selected

        amount = 0
        for select in selected:
            amount += select.get_price()

        self.window = tk.Toplevel(bg="#FAD8D6")

        self.window.title("Payment Window")
        self.window.resizable(False, False)

        # First Frame

        self.payment_label_frame = tk.LabelFrame(self.window, text="Payment", bg="#FAD8D6")
        self.payment_label_frame.grid(row=0, column=0, padx=15, pady=10)

        # Card Name
        self.payment_name_label = tk.Label(self.payment_label_frame, text="Card Name", bg="#FAD8D6")
        self.payment_name_label.grid(row=0, column=0)

        self.payment_name_entry = tk.Entry(self.payment_label_frame, bg="#f0f0f0")
        self.payment_name_entry.grid(row=1, column=0)

        # Card Number
        self.payment_card_number = tk.Label(self.payment_label_frame, text="Card Number", bg="#FAD8D6")
        self.payment_card_number.grid(row=2, column=0)

        self.payment_card_number_entry = tk.Entry(self.payment_label_frame, bg="#f0f0f0")
        self.payment_card_number_entry.grid(row=3, column=0)

        # Card CSV
        self.payment_card_csv_label = tk.Label(self.payment_label_frame, text="CSV", bg="#FAD8D6")
        self.payment_card_csv_label.grid(row=4, column=0)

        self.payment_card_csv_entry = tk.Entry(self.payment_label_frame, bg="#f0f0f0")

        self.payment_card_csv_entry.grid(row=5, column=0)

        # Second Frame

        self.details_label_frame = tk.LabelFrame(self.window, text="Booking Details", bg="#FAD8D6")
        self.details_label_frame.grid(row=0, column=1)

        self.show_text = tk.Text(self.details_label_frame, height=4, width=20, bg="#F0F0F0")

        self.show_text.insert("1.0", "Show: " + str(show["Title"]) +
                              "\nDate: " + str(show["Date"]) +
                              "\nPlayed at: " + show["Played_at"].get_name() +
                              "\nTotal Amount: " + str(amount) +
                              "")
        self.show_text.config(state="disabled")
        self.show_text.grid(row=0, column=0)

        def confirm_command():
            values = [self.payment_name_entry.get(),
                      self.payment_card_csv_entry.get(),
                      self.payment_card_number_entry.get()]

            if any(value == "" for value in values):
                showinfo(message="You need to fill all entries")
                return
                

            # Making payment at background..................

            tmp_payment = Payment(amount, datetime.time.hour, PaymentStatus.PENDING)
            tmp_booking = Booking(str(datetime.date.today()),
                                  len(selected),
                                  BookingStatus.PENDING,
                                  show,
                                  selected,
                                  tmp_payment
                                  )
            current_user.make_booking(tmp_booking)
            booking_list.append(tmp_booking)
            print(current_user.get_bookings())

            # Confirming if booking exist
            test_bookings = current_user.get_bookings()
            for test_booking in test_bookings:
                for booking in booking_list:
                    if test_booking == booking:
                        self.window.destroy()
                        showinfo(message="Thank you for using our platform")
                        tmp_payment.set_status(PaymentStatus.COMPLETED)
                        tmp_booking.set_status(BookingStatus.CONFIRMED)
                        for seat in selected:
                            seat.set_seat_type(SeatType.REGULAR)

        self.confirm_button = tk.Button(self.window, text="Confirm", command=confirm_command, fg="#FAD8D6",
                                        bg="#890B59")
        self.confirm_button.grid(row=6, column=1, pady=10)

        self.cancel_button = tk.Button(self.window, text="Cancel", command=self.window.destroy, fg="#FAD8D6",
                                       bg="#890B59")

        self.cancel_button.grid(row=6, column=0, pady=10)


class UserSignIn(tk.Frame):

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("User Sign In")
        self.window.resizable(False, False)

        self.frame = tk.Frame(self.window, bg="#FAD8D6")
        self.frame.grid(row=0, column=0)

        # First LabelFrame

        self.user_detail_label_frame = tk.LabelFrame(self.frame, text="User Detail", fg="#7c044c", bg='#FAD8D6')
        self.user_detail_label_frame.grid(row=0, column=1, padx=15, pady=10)

        self.user_name_label = tk.Label(self.user_detail_label_frame, text="Name", fg='#890B59', bg='#FAD8D6',
                                        font=('Arial', 12, 'bold'))
        self.user_name_label.grid(row=0, column=0)

        self.user_name_entry = tk.Entry(self.user_detail_label_frame, bg='white')
        self.user_name_entry.grid(row=1, column=0)

        self.user_email_label = tk.Label(self.user_detail_label_frame, text="Email", fg='#890B59', bg='#FAD8D6',
                                         font=('Arial', 12, 'bold'))
        self.user_email_label.grid(row=2, column=0)

        self.user_email_entry = tk.Entry(self.user_detail_label_frame, bg='white')
        self.user_email_entry.grid(row=3, column=0)

        self.user_phone_label = tk.Label(self.user_detail_label_frame, text="Phone Number", fg='#890B59', bg='#FAD8D6',
                                         font=('Arial', 12, 'bold'))
        self.user_phone_label.grid(row=4, column=0)

        self.user_phone_entry = tk.Entry(self.user_detail_label_frame, bg='white')
        self.user_phone_entry.grid(row=5, column=0)

        self.user_address_label = tk.Label(self.user_detail_label_frame, text="Address", fg='#890B59', bg='#FAD8D6',
                                           font=('Arial', 12, 'bold'))
        self.user_address_label.grid(row=6, column=0)

        self.address_entry = tk.Entry(self.user_detail_label_frame, bg='white')
        self.address_entry.grid(row=7, column=0)

        # Second LabelFrame

        self.main_frame = tk.LabelFrame(self.frame, text="User Sign In", fg="#7c044c", bg='#FAD8D6')
        self.main_frame.grid(row=0, column=2, padx=15, pady=10)

        # Name
        self.nickname_label = tk.Label(self.main_frame, text="Nickname", fg='#890B59', bg='#FAD8D6',
                                       font=('Arial', 12, 'bold'))
        self.nickname_label.grid(row=0, column=0)

        self.nickname_entry = tk.Entry(self.main_frame, width=17, bg='white')
        self.nickname_entry.grid(row=1, column=0, padx=13)

        # Password
        self.pwd_label = tk.Label(self.main_frame, text="Password", fg='#890B59', bg='#FAD8D6',
                                  font=('Arial', 12, 'bold'))
        self.pwd_label.grid(row=2, column=0)

        self.pwd_entry = tk.Entry(self.main_frame, show="*", width=17, bg='white')
        self.pwd_entry.grid(row=3, column=0, padx=13)

        # Password Retry
        self.pwd_retry_label = tk.Label(self.main_frame, text="Password Retry", fg='#890B59', bg='#FAD8D6',
                                        font=('Arial', 12, 'bold'))
        self.pwd_retry_label.grid(row=4, column=0, padx=13)

        self.pwd_retry_entry = tk.Entry(self.main_frame, show="*", width=17, bg='white')
        self.pwd_retry_entry.grid(row=5, column=0, padx=13)

        # ---------Buttons
        def sign_in_command():
            values = [self.nickname_entry.get(),
                      self.pwd_entry.get(),
                      self.address_entry.get().split(","),
                      self.user_name_entry.get(),
                      self.user_phone_entry.get(),
                      ]
            control = False
            for value in values:
                if value == "":
                    showinfo(message="You need to fill all entries")
                    return
            if self.pwd_entry.get() != self.pwd_retry_entry.get():
                showinfo(message="Password not match")
                return
            else:
                control = True

            # try:
            if control is True:
                tmp_account = Account(self.nickname_entry.get(),
                                      self.pwd_entry.get(),
                                      AccountStatus.ACTIVE)
                address_str = self.address_entry.get().split(",")
                tmp_address = Address(address_str[0],
                                      address_str[1],
                                      address_str[2],
                                      address_str[3],
                                      address_str[4]
                                      )
                tmp_customer = Customer(self.user_name_entry.get(),
                                        tmp_address,
                                        self.user_email_entry.get(),
                                        self.user_phone_entry.get(),
                                        tmp_account)

                user_list.append(tmp_customer)

                if tmp_customer in user_list:
                    print(tmp_customer)
                    self.window.destroy()
            # except:
            #    showinfo("Error", " Error Occurred")

        self.button_label = tk.Label(self.main_frame, bg="#FAD8D6")
        self.button_label.grid(row=6, column=0)

        # Login Button
        self.sign_in_button = tk.Button(self.button_label, text="Sign In", command=sign_in_command, fg="white",
                                        bg="#890B59")
        self.sign_in_button.grid(row=0, column=1, padx=20, pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(self.button_label, text="Cancel", command=self.window.destroy, fg="white",
                                       bg="#890B59")
        self.cancel_button.grid(row=0, column=0, padx=20, pady=5)

        # ----------------


class UserLogin(tk.Frame):
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("User Login")
        self.window.resizable(False, False)

        self.frame = tk.Frame(self.window, bg="#FAD8D6")
        self.frame.pack()

        # Main Frame
        self.main_frame = tk.LabelFrame(self.frame, text="User Login", fg="#7c044c", bg='#FAD8D6')
        self.main_frame.grid(row=0, column=0, padx=15, pady=10)

        # Name
        self.name_label = tk.Label(self.main_frame, text="Name", fg='#890B59', bg='#FAD8D6')
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.grid(row=1, column=0, padx=13)

        # Password
        self.pwd_label = tk.Label(self.main_frame, text="Password", fg='#890B59', bg='#FAD8D6')
        self.pwd_label.grid(row=2, column=0)

        self.pwd_entry = tk.Entry(self.main_frame, show="*")
        self.pwd_entry.grid(row=3, column=0, padx=13)

        # ---------Buttons
        def login_command():
            tmp_account = Account(self.name_entry.get(),
                                  self.pwd_entry.get(),
                                  AccountStatus.ACTIVE)
            print(self.name_entry.get() + " pwd " + self.pwd_entry.get())

            for tmp_user in user_list:
                if tmp_account.get_user_id() == tmp_user.get_account().get_user_id() and \
                        tmp_account.get_password() == tmp_user.get_account().get_password():
                    update_user(tmp_user)
                    print("found")
                    self.window.destroy()
                else:
                    print(tmp_user.get_account().get_user_id())
                    print("Not found")

            return

        self.button_label = tk.Label(self.main_frame, bg="#FAD8D6")
        self.button_label.grid(row=4, column=0)

        # Login Button
        self.login_button = tk.Button(self.button_label, text="Login", command=login_command, fg="white", bg="#890B59")
        self.login_button.grid(row=4, column=1, padx=20, pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(self.button_label, text="Cancel", command=self.window.destroy, fg="white",
                                       bg="#890B59")
        self.cancel_button.grid(row=4, column=0, padx=20, pady=5)

        # ----------------


class SeatButton:
    def __init__(self, frame, row, coulomn, show_seat: ShowSeat):
        global selected

        def selected_seat():
            if show_seat in selected:
                self.tmp_button.config(bg="green")
                selected.remove(show_seat)
                print("Already included. Selected seat removed")
                return 0
            self.tmp_button.config(bg="blue")
            selected.append(show_seat)

        self.tmp_button = tk.Button(frame, text="ロ", width=1, command=selected_seat)
        self.tmp_button.grid(row=row, column=coulomn)

        if show_seat.get_seat_type() == SeatType.REGULAR or \
                show_seat.get_seat_type() == SeatType.PREMIUM:

            self.tmp_button.config(state="disabled")
            self.tmp_button.config(bg="grey")
        else:
            self.tmp_button.config(bg="green")


class ToShow(tk.Frame):
    def __init__(self, show):
        self.window = tk.Toplevel(bg="#FAD8D6")
        self.window.title("Show Info")
        self.window.resizable(False, False)
        # LabelFrame 1
        self.label = tk.LabelFrame(self.window, text="Cinema Details", bg="#FAD8D6")
        self.label.grid(row=0, column=0)

        self.cinema_detail_txt = tk.Text(self.label, height=10, width=30, bg="#f0f0f0")
        self.cinema_detail_txt.insert("1.0", " Show:" + show["Title"])
        self.cinema_detail_txt.config(state="disabled")
        self.cinema_detail_txt.grid(row=0, column=0)

        # Label 2
        self.label2 = tk.LabelFrame(self.window, text="Select seats", bg="#FAD8D6")
        self.label2.grid(row=0, column=1)

        cinema_hall = show["Played_at"]
        cinema_hall_seats = cinema_hall.get_cinema_hall_seats()
        row = cinema_hall.get_total_row()
        coulomn = cinema_hall.get_total_coulomn()

        self.cinema_panel_text = tk.Text(self.label2, height=1, width=20, bg="#FFE15C")
        self.cinema_panel_text.insert("1.0", "   Cinema Monitor")
        self.cinema_panel_text.config(state="disabled")
        self.cinema_panel_text.grid(row=0, column=0)

        self.seat_button_label = tk.Label(self.label2)
        self.seat_button_label.grid(row=1, column=0, padx=10, pady=20)

        [SeatButton(self.seat_button_label, j, i, show_seat) for show_seat in cinema_hall_seats for i in range(0, coulomn) for j in range(0, row) if show_seat.get_seat_row() == j and show_seat.get_seat_coulomn() == i]

        # Label 3
        self.label3 = tk.Label(self.window)
        self.label3.grid(row=0, column=2)

        def make_payment():
            global selected
            for select in selected:
                print(str(select.print()))

            if len(selected) == 0:
                showinfo(message="You have not selected any seat yet")
                return
            self.window.destroy()
            MakeBooking(show)

        def cancel_command():
            global selected
            selected = []
            self.window.destroy()

        self.payment_button = tk.Button(self.window, text="Make Payment", command=make_payment, fg="white",
                                        bg="#890B59")
        self.payment_button.grid(row=5, column=1, pady=10)

        self.cancel_button = tk.Button(self.window, text="Cancel", command=cancel_command, fg="white", bg="#890B59")
        self.cancel_button.grid(row=5, column=0, pady=10)

        self.window.protocol("WM_DELETE_WINDOW", cancel_command)


class ShowUi:
    def __init__(self, show, frame, row):

        self.show_label = tk.Label(frame, text="show", background="#FAD8D6")
        self.show_label.grid(row=row, column=0)

        self.show_text = tk.Text(self.show_label, height=4, width=115)
        self.show_text.insert("1.0", str(show["Title"]) +
                              "\n genre: " + str(show["Genre"]) +
                              "\n seats: " + str(show['Seat']) +
                              "\n day: " + str(show['Date']))
        self.show_text.config(state='disabled')
        self.show_text.grid(row=row, column=0, pady=10)
        self.show = show
        self.show_button = tk.Button(self.show_label, text="To Show", command=self.to_show, fg="#FAD8D6", bg="#890B59")
        self.show_button.grid(row=row, column=1, pady=10)

    def to_show(self):
        if type(current_user) == Customer:
            ToShow(self.show)

        elif type(current_user) == Guest:
            self.window = tk.Toplevel(bg='#FAD8D6')
            self.window.title("Info")
            self.window.resizable(False, False)

            self.frame = tk.Frame(self.window, bg='#FAD8D6')
            self.frame.grid(row=0, column=0)

            def login_command():
                UserLogin()
                self.window.destroy()

            def sign_in_command():
                UserSignIn()
                self.window.destroy()

            def cancel_command():
                self.window.destroy()

            self.info_text = tk.Text(self.window, width=50, height=2, fg="#7c044c", bg='#FAD8D6')
            self.info_text.grid(row=0, column=0)
            self.info_text.insert("1.0", "            You have not login yet. \n"
                                         "      Please login or register an account.")
            self.info_text.config(state="disabled")

            self.button_label = tk.Label(self.window, bg='#FAD8D6')
            self.button_label.grid(row=1, column=0)

            # Login Button
            self.login_button = tk.Button(self.button_label, text="Login", command=login_command,
                                          fg="white", bg="#890B59")
            self.login_button.grid(row=1, column=1, padx=50, pady=5)

            # Sign In Button
            self.sign_in_button = tk.Button(self.button_label, text="Sign In", command=sign_in_command,
                                            fg="white", bg="#890B59")
            self.sign_in_button.grid(row=1, column=0, padx=50, pady=5)

            # Cancel Button
            self.cancel_button = tk.Button(self.button_label, text="Cancel", command=cancel_command,
                                           fg="white", bg="#890B59")
            self.cancel_button.grid(row=2, column=0, padx=20, pady=5)

    def delete(self):
        self.show_text.destroy()
        self.show_label.destroy()
        self.show_button.destroy()
        self.show_text.destroy()


class ResultFrameUI:
    def __init__(self, show, frame, row):
        self.show_label = tk.Label(frame, text="show", background="#FAD8D6")
        self.show_label.grid(row=row, column=0)

        self.show_text = tk.Text(self.show_label, height=4, )

        self.show_text.insert("1.0", str(show["Title"]) +
                              "\n genre: " + str(show["Genre"]) +
                              "\n seats: " + str(show['Seat']) +
                              "\n day: " + str(show['Date']))
        self.show_text.config(state='disabled')
        self.show_text.grid(row=row, column=0, pady=10)
        self.show = show
        self.show_button = tk.Button(self.show_label, text="To Show", command=self.to_show, )
        self.show_button.grid(row=row, column=1, pady=10)


def main():
    global user_frame_tmp

    window = tk.Tk()
    window.title("Movie Ticket Management System")
    window.resizable(False, False)
    window.geometry("1450x700")
    window.config(bg="#FAD8D6")

    # Image
    logo = tk.PhotoImage(file="WhatsApp_Image_2022-12-26_at_16.51.45-removebg-preview (2).png")
    w1 = tk.Label(window, image=logo)
    w1.grid(row=4, column=0)

    frame = tk.Frame(window, bg="#FAD8D6")
    frame.grid(row=1, column=0)

    # For empty space
    zero_frame = tk.LabelFrame(frame)
    zero_frame.grid(row=0, column=0, padx=40, pady=40)

    # --------------------First Row--------------------

    # Main Frame
    first_frame = tk.LabelFrame(frame, text="", bg="#FAD8D6", relief="groove", bd=4)
    user_frame_tmp = first_frame
    first_frame.grid(row=1, column=0)

    # Time and Date
    time_text = tk.Text(first_frame, height=2, width=80, font=("Helvatica", 10), pady=1, padx=1, spacing1=2)
    time_text.insert("1.0",
                     "Current Time: " + str(current_datetime.time())[:-7] + "\nDate: " + str(current_datetime.date()))
    time_text.config(state='disabled')
    time_text.grid(row=0, column=1)

    # User Info

    user_label = tk.Label(first_frame, bg="#FAD8D6")
    user_label.grid(row=0, column=2)

    # User Login
    def user_login_command():
        UserLogin()

    login_button = tk.Button(user_label, text="Login", command=user_login_command, fg="white", bg="#890B59")
    login_button.grid(row=0, column=2)

    # User Sign In
    def user_sign_in_command():
        UserSignIn()

    sign_in_button = tk.Button(user_label, text="Sign In", command=user_sign_in_command, fg="white", bg="#890B59")
    sign_in_button.grid(row=1, column=2)

    ################################################

    # --------------------Second Row-------------------
    # Main Frame
    second_frame = tk.LabelFrame(frame, text="Search Movie", bd=4, fg="#890B59", bg="#FAD8D6",
                                 font=("Helvetica", 16), labelanchor="n", relief="groove",
                                 pady=20, padx=4, height=200, width=200)

    second_frame.grid(row=2, column=0, padx=45, pady=20)

    # Title filter
    title_label = tk.Label(second_frame, text="Title", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12), width=20)
    title_label.grid(row=0, column=1)

    title_entry = tk.Entry(second_frame, bg="#f0f0f0")
    title_entry.grid(row=1, column=1)

    # Language filter
    language_label = tk.Label(second_frame, text="Language", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12),
                              width=20)
    language_label.grid(row=0, column=2)

    lang_combobox = ttk.Combobox(second_frame, values=['EN', 'FR', 'HI', 'IT', 'JA', 'ZH', 'TR'])
    lang_combobox.grid(row=1, column=2)

    # Genre filter
    genre_label = tk.Label(second_frame, text="Genre", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12), width=20)
    genre_label.grid(row=0, column=3)

    genre_combobox = ttk.Combobox(second_frame,
                                  values=[
                                      'Action',
                                      'Comedy',
                                      'Drama',
                                      'Horror',
                                      'Romance',
                                      'Thriller',
                                      'Western',
                                      'Animation',
                                      'Crime',
                                      'Documentary',
                                      'Family',
                                      'Fantasy',
                                      'History',
                                      'Music',
                                      'Mystery',
                                      'Science Fiction',
                                      'TV Movie',
                                      'War',
                                      'Foreign'])
    genre_combobox.grid(row=1, column=3)

    # Release Date filter
    release_date_label = tk.Label(second_frame, text="Release Date", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12),
                                  width=20)
    release_date_label.grid(row=0, column=4)

    release_date_entry = tk.Entry(second_frame, bg="#f0f0f0")
    release_date_entry.grid(row=1, column=4)

    # country filter
    country_label = tk.Label(second_frame, text="Country", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12), width=20)
    country_label.grid(row=0, column=5)

    country_combobox = ttk.Combobox(second_frame,
                                    values=['USA',
                                            'UK',
                                            'Canada',
                                            'France',
                                            'Germany',
                                            'Italy',
                                            'Spain',
                                            'Japan',
                                            'China',
                                            'India',
                                            'Australia',
                                            'Brazil',
                                            'Mexico',
                                            'Russia',
                                            'South Korea',
                                            'Turkey',
                                            'Iran',
                                            'Saudi Arabia',
                                            'Egypt',
                                            'Nigeria'])
    country_combobox.grid(row=1, column=5)

    # Seat filter
    seat_label = tk.Label(second_frame, text="Seat", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12), width=20)
    seat_label.grid(row=0, column=6)

    seat_entry = tk.Entry(second_frame, bg="#f0f0f0")
    seat_entry.grid(row=1, column=6)

    # Date filter
    date_label = tk.Label(second_frame, text="Date", fg="#7c044c", bg='#FAD8D6', font=("Helvetica", 12), width=20)
    date_label.grid(row=0, column=7)

    date_entry = tk.Entry(second_frame, bg="#f0f0f0")
    date_entry.grid(row=1, column=7)

    # --------------------------------------------

    def search_by_filter():
        global result_instance
        # dict = UserSignIn.user_sign_in()
        print("Search pressed!")

        filter_values = {"Title": title_entry.get(),
                         "Language": lang_combobox.get(),
                         "Genre": genre_combobox.get(),
                         "Rel_date": release_date_entry.get(),
                         "Country": country_combobox.get(),
                         "Seat": seat_entry.get(),
                         "Date": date_entry.get()
                         }

        result_dict = Catalog.search_show_by_filter(show_list, filter_values)

        try:
            for instance in result_instance:
                if instance is not None:
                    instance.delete()
        except AttributeError:
            print("movie instance not deleted")
            pass

        third_frame = tk.LabelFrame(frame, text="Results", bd=4, fg="#890B59", bg="#FAD8D6",
                                    font=("Helvetica", 16), labelanchor="n", relief="groove",
                                    pady=1, padx=4)

        # Create a main frame
        result_main_frame = tk.Frame(third_frame)
        result_instance.append(result_main_frame)
        result_main_frame.pack(fill=tk.BOTH, expand=1)

        # Create canvas
        result_canvas = tk.Canvas(result_main_frame, width=1010, bd=4, bg="#FAD8D6", )

        result_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # add scrollbar to canvas
        my_scrollbar = tk.Scrollbar(result_main_frame, orient="vertical", command=result_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # configure the canvas
        result_canvas.config(yscrollcommand=my_scrollbar.set)
        result_canvas.bind('<Configure>', lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))

        # Create another frame inside the canvas
        result_second_frame = tk.Frame(result_canvas)

        # Add that new frame to a window in the Canvas
        result_canvas.create_window((0, 0), window=result_second_frame, anchor=tk.NW)
        i = 0
        for show in result_dict.values():
            ShowUi(show, result_second_frame, i)
            i += 1
        third_frame.grid(row=3, column=0, padx=45, pady=20)

    # Search Button
    search_button = tk.Button(second_frame, text="Search", command=search_by_filter, fg="white", bg="#890B59")
    search_button.grid(row=1, column=8)

    window.mainloop()


if __name__ == '__main__':
    main()
