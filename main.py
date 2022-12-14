import pandas as pd
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
# def my_combo_box()
from typing import List

from lib.Catalog import Catalog
from lib.Movie import Movie


def show_result(txt: str):
    showinfo(
        message=f'Result {txt}!'
    )
def movie_ui(frame,row,coulomn):
    genre_label = tkinter.Label(frame, text="Genre")
    genre_label.grid(row=row, column=coulomn)


def main():
    my_movie = Movie(
        "Harry Potter", "DESCRIPTION", 30, "TR", 2012, "Turkey", "HORROR", "ME"
    )
    my_movie2 = Movie(
        "TITLE2", "DESCRIPTION2", 31, "TR", 2013, "Turkey", "HORROR2", "ME2"
    )
    my_catalog = Catalog()
    my_catalog.add_movie(my_movie)
    my_catalog.add_movie(my_movie2)
    # for movie in my_catalog.get_all_movies():
    #     print(movie.title)
    # print("\n")
    window = tk.Tk()
    window.title("Movie Ticket Management System")
    window.resizable(False, False)

    frame = tkinter.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tkinter.LabelFrame(frame, text="Searh Movie")
    main_frame.grid(row=0, column=0, padx=25, pady=10)
    # Genre filter
    genre_label = tkinter.Label(main_frame, text="Genre")
    genre_label.grid(row=0, column=3)

    genre_entry = tkinter.Entry(main_frame)
    genre_entry.grid(row=1, column=3)
    genre_filter_value = genre_entry.get()

    # Realese Date filter
    realese_date_label = tkinter.Label(main_frame, text="Realese Date")
    realese_date_label.grid(row=0, column=4)

    realese_date_entry = tkinter.Entry(main_frame)
    realese_date_entry.grid(row=1, column=4)
    realese_date_filter_value = realese_date_entry.get()

    # Language filter
    language_label = tkinter.Label(main_frame, text="Language")
    language_label.grid(row=0, column=2)

    language_entry = tkinter.Entry(main_frame)
    language_entry.grid(row=1, column=2)
    language_filter_value = language_entry.get()

    # Title filter
    title_label = tkinter.Label(main_frame, text="Title")
    title_label.grid(row=0, column=1)

    title_entry = tkinter.Entry(main_frame)
    title_entry.grid(row=1, column=1)
    title_filter_value = title_entry.get()

    # City filter
    city_label = tkinter.Label(main_frame, text="City")
    city_label.grid(row=0, column=5)

    city_entry = tkinter.Entry(main_frame)
    city_entry.grid(row=1, column=5)
    city_filter_value = city_entry.get()

    # Seat filter
    seat_label = tkinter.Label(main_frame, text="Seat")
    seat_label.grid(row=0, column=6)

    seat_entry = tkinter.Entry(main_frame)
    seat_entry.grid(row=1, column=6)
    seat_filter_value = seat_entry.get()

    # Date filter
    date_label = tkinter.Label(main_frame, text="Date")
    date_label.grid(row=0, column=7)

    date_entry = tkinter.Entry(main_frame)
    date_entry.grid(row=1, column=7)
    date_filter_value = date_entry.get()

    # --------------------------------------------

    def search_by_filter():
        print("Search pressed!")
        filter_value = { "Title": "Harry Potter",
                         "Genre": "HORROR"

                         }
        my_list = my_catalog.search_by_filter(filter_value)


    # Search Button
    search_button = tkinter.Button(main_frame, text="Search", command=search_by_filter)
    search_button.grid(row=1, column=8)
    window.mainloop()



if __name__ == '__main__':
    main()




