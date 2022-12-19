import datetime
import tkinter as tk
from tkinter.messagebox import showinfo

from lib import Catalog
from lib.People import Guest, Account, Customer
from lib.Constants import AccountStatus

from src.SearchResult import search_result_ui

from Data.FakeData import show_list
from Data.FakeAccounts import user_list

current_user = Guest()
current_datetime = datetime.datetime(2022, 12, 22, 10, 30)
result_instance = 4


def show_result(txt: str):
    showinfo(
        message=f'Result {txt}!'
    )


def update_user(user, frame=None):
    if frame is None:
        pass
    elif type(user) == Customer:
        user_name_text = tk.Text(frame, height=2, width=30)
        user_name_text.insert("1.0", "Name is Akhmet" + "\nStatus")
        user_name_text.config(state='disabled')
        user_name_text.grid(row=0, column=0)

    global current_user
    current_user = user
    print(current_user)


class UserSignIn(tk.Frame):
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("User Sign In")
        self.window.resizable(False, False)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Main Frame
        self.main_frame = tk.LabelFrame(self.frame, text="User Sign In")
        self.main_frame.grid(row=0, column=0, padx=15, pady=10)

        # Name
        self.name_label = tk.Label(self.main_frame, text="Nickname")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.main_frame, width=17)
        self.name_entry.grid(row=1, column=0, padx=13)

        # Password
        self.pwd_label = tk.Label(self.main_frame, text="Password")
        self.pwd_label.grid(row=2, column=0)

        self.pwd_entry = tk.Entry(self.main_frame, width=17)
        self.pwd_entry.grid(row=3, column=0, padx=13)

        # Password Retry
        self.pwd_retry_label = tk.Label(self.main_frame, text="Password Retry")
        self.pwd_retry_label.grid(row=4, column=0, padx=13)

        self.pwd_retry_entry = tk.Entry(self.main_frame, width=17)
        self.pwd_retry_entry.grid(row=5, column=0, padx=13)

        # ---------Buttons
        def sign_in_command():
            Account(self.name_entry.get(),
                    self.pwd_entry.get(),
                    AccountStatus.ACTIVE)

            return

        def cancel_command():
            self.window.destroy()

        self.button_label = tk.Label(self.main_frame)
        self.button_label.grid(row=6, column=0)

        # Login Button
        self.sign_in_button = tk.Button(self.button_label, text="Sign In", command=sign_in_command)
        self.sign_in_button.grid(row=0, column=1, padx=20, pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(self.button_label, text="Cancel", command=cancel_command)
        self.cancel_button.grid(row=0, column=0, padx=20, pady=5)

        # ----------------


class UserLogin(tk.Frame):
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("User Login")
        self.window.resizable(False, False)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Main Frame
        self.main_frame = tk.LabelFrame(self.frame, text="User Login")
        self.main_frame.grid(row=0, column=0, padx=15, pady=10)

        # Name
        self.name_label = tk.Label(self.main_frame, text="Name")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.grid(row=1, column=0, padx=13)

        # Password
        self.pwd_label = tk.Label(self.main_frame, text="Password")
        self.pwd_label.grid(row=2, column=0)

        self.pwd_entry = tk.Entry(self.main_frame)
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

        def cancel_command():
            self.window.destroy()

        self.button_label = tk.Label(self.main_frame)
        self.button_label.grid(row=4, column=0)

        # Login Button
        self.login_button = tk.Button(self.button_label, text="Login", command=login_command)
        self.login_button.grid(row=4, column=1, padx=20, pady=5)

        # Cancel Button
        self.cancel_button = tk.Button(self.button_label, text="Cancel", command=cancel_command)
        self.cancel_button.grid(row=4, column=0, padx=20, pady=5)

        # ----------------


def main():
    window = tk.Tk()
    window.title("Movie Ticket Management System")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()
    # --------------------First Row--------------------
    # Main Frame
    first_frame = tk.LabelFrame(frame, text="")
    first_frame.grid(row=0, column=0)

    # Time and Date
    time_text = tk.Text(first_frame, height=2, width=30)
    time_text.insert("1.0", "Current Time: " + str(current_datetime.time()) + "\nDate: " + str(current_datetime.date()))
    time_text.config(state='disabled')
    time_text.grid(row=0, column=1)

    # User Login
    def user_login_command():
        UserLogin()


    login_button = tk.Button(first_frame, text="Login", command=user_login_command)
    login_button.grid(row=0, column=2)

    # User Sign In
    def user_sign_in_command():
        UserSignIn()

    sign_in_button = tk.Button(first_frame, text="Sign In", command=user_sign_in_command)
    sign_in_button.grid(row=1, column=2)

    # --------------------Second Row-------------------
    # Main Frame
    second_frame = tk.LabelFrame(frame, text="Search Movie")
    second_frame.grid(row=1, column=0, padx=25, pady=10)
    # Genre filter
    genre_label = tk.Label(second_frame, text="Genre")
    genre_label.grid(row=0, column=3)

    genre_entry = tk.Entry(second_frame)
    genre_entry.grid(row=1, column=3)

    # Release Date filter
    release_date_label = tk.Label(second_frame, text="Release Date")
    release_date_label.grid(row=0, column=4)

    release_date_entry = tk.Entry(second_frame)
    release_date_entry.grid(row=1, column=4)

    # Language filter
    language_label = tk.Label(second_frame, text="Language")
    language_label.grid(row=0, column=2)

    language_entry = tk.Entry(second_frame)
    language_entry.grid(row=1, column=2)

    # Title filter
    title_label = tk.Label(second_frame, text="Title")
    title_label.grid(row=0, column=1)

    title_entry = tk.Entry(second_frame)
    title_entry.grid(row=1, column=1)

    # country filter
    country_label = tk.Label(second_frame, text="Country")
    country_label.grid(row=0, column=5)

    country_entry = tk.Entry(second_frame)
    country_entry.grid(row=1, column=5)

    # Seat filter
    seat_label = tk.Label(second_frame, text="Seat")
    seat_label.grid(row=0, column=6)

    seat_entry = tk.Entry(second_frame)
    seat_entry.grid(row=1, column=6)

    # Date filter
    date_label = tk.Label(second_frame, text="Date")
    date_label.grid(row=0, column=7)

    date_entry = tk.Entry(second_frame)
    date_entry.grid(row=1, column=7)

    # --------------------------------------------

    def search_by_filter():
        global result_instance
        # dict = UserSignIn.user_sign_in()
        print("Search pressed!")

        filter_values = {"Title": title_entry.get(),
                         "Language": language_entry.get(),
                         "Genre": genre_entry.get(),
                         "Rel_date": release_date_entry.get(),
                         "Country": country_entry.get(),
                         "Seat": seat_entry.get(),
                         "Date": date_entry.get()
                         }

        result_dict = Catalog.search_show_by_filter(show_list, filter_values)
        print(result_dict)
        # dict_result = movie_catalog.search_by_filter(filter_values)
        # print(dict_result)
        try:
            if result_instance is not None:
                result_instance.delete()
        except AttributeError:
            print("movie instance not deleted")
            pass
        result_instance = search_result_ui(result_dict, frame, 2)

    # Search Button
    search_button = tk.Button(second_frame, text="Search", command=search_by_filter)
    search_button.grid(row=1, column=8)
    window.mainloop()


if __name__ == '__main__':
    main()
