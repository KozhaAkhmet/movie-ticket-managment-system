import pandas as pd
import tkinter as tk
from tkinter.messagebox import showinfo

from lib.Catalog import Catalog
from lib.Movie import Movie
from lib.FakeData import movie_catalog
import src.UserLogin as UserLogin
import src.UserSignIn as UserSignIn


def show_result(txt: str):
    showinfo(
        message=f'Result {txt}!'
    )


def movie_ui(result_dict, frame):
    i = 0
    row = 1
    for movie in result_dict.values():
        print(movie)
        movie_label = tk.Label(frame, text="Movie")
        movie_label.grid(row=row + i, column=0)

        movie_text = tk.Text(movie_label, height=1, width=154)
        movie_text.insert("1.0", str(movie["Title"]) + " genre: " + str(movie["Genre"]))
        movie_text.config(state='disabled')
        movie_text.grid(row=row + i, column=0)

        i = i + 1


def main():
    # for movie in movie_catalog.get_all_movies():
    #     print(movie.title)
    # print("\n")
    window = tk.Tk()
    window.title("Movie Ticket Management System")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="Searh Movie")
    main_frame.grid(row=0, column=0, padx=25, pady=10)
    # Genre filter
    genre_label = tk.Label(main_frame, text="Genre")
    genre_label.grid(row=0, column=3)

    genre_entry = tk.Entry(main_frame)
    genre_entry.grid(row=1, column=3)
    genre_filter_value = genre_entry.get()

    # Realese Date filter
    realese_date_label = tk.Label(main_frame, text="Realese Date")
    realese_date_label.grid(row=0, column=4)

    realese_date_entry = tk.Entry(main_frame)
    realese_date_entry.grid(row=1, column=4)
    realese_date_filter_value = realese_date_entry.get()

    # Language filter
    language_label = tk.Label(main_frame, text="Language")
    language_label.grid(row=0, column=2)

    language_entry = tk.Entry(main_frame)
    language_entry.grid(row=1, column=2)
    language_filter_value = language_entry.get()

    # Title filter
    title_label = tk.Label(main_frame, text="Title")
    title_label.grid(row=0, column=1)

    title_entry = tk.Entry(main_frame)
    title_entry.grid(row=1, column=1)
    title_filter_value = title_entry.get()

    # City filter
    city_label = tk.Label(main_frame, text="City")
    city_label.grid(row=0, column=5)

    city_entry = tk.Entry(main_frame)
    city_entry.grid(row=1, column=5)
    city_filter_value = city_entry.get()

    # Seat filter
    seat_label = tk.Label(main_frame, text="Seat")
    seat_label.grid(row=0, column=6)

    seat_entry = tk.Entry(main_frame)
    seat_entry.grid(row=1, column=6)
    seat_filter_value = seat_entry.get()

    # Date filter
    date_label = tk.Label(main_frame, text="Date")
    date_label.grid(row=0, column=7)

    date_entry = tk.Entry(main_frame)
    date_entry.grid(row=1, column=7)
    date_filter_value = date_entry.get()

    # --------------------------------------------

    def search_by_filter():
        #UserSignIn.user_sign_in()
        print("Search pressed!")
        filter_value = {"City": "England"
                        }

        dict_result = movie_catalog.search_by_filter(filter_value)
        print(dict_result)
        movie_ui(dict_result, frame)

    # Search Button
    search_button = tk.Button(main_frame, text="Search", command=search_by_filter)
    search_button.grid(row=1, column=8)
    window.mainloop()


if __name__ == '__main__':
    main()
