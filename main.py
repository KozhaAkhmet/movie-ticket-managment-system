import datetime
import tkinter as tk
from tkinter.messagebox import showinfo

from lib import Catalog
from Data.FakeData import show_list

from src.SearchResult import search_result_ui
from src.User import user_login, user_sign_in


# import src.UserLogin as UserLogin
# import src.UserSignIn as UserSignIn


def show_result(txt: str):
    showinfo(
        message=f'Result {txt}!'
    )


current_datetime = datetime.datetime(2022, 12, 22, 10, 30)
result_instance = 4


def main():
    # for movie in movie_catalog.get_all_movies():
    #     print(movie.title)
    # print("\n")
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
    time_text.grid(row=0, column=0)

    # User Login
    def user_login_command():
        user_login()

    login_button = tk.Button(first_frame, text="Login", command=user_login_command)
    login_button.grid(row=0, column=1)

    # User Sign In
    def user_sign_in_command():
        result = user_sign_in()
        print(result)
    sign_in_button = tk.Button(first_frame, text="Sign In", command=user_sign_in_command)
    sign_in_button.grid(row=1, column=1)

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

    # City filter
    city_label = tk.Label(second_frame, text="City")
    city_label.grid(row=0, column=5)

    city_entry = tk.Entry(second_frame)
    city_entry.grid(row=1, column=5)

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
                         "City": city_entry.get(),
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
