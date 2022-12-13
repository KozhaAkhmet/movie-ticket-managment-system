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


def main():
    my_movie = Movie(
        "Harry Poter", "DESCRIPTION", 30, "TR", 2012, "Turkey", "HORROR", "ME"
    )
    my_movie2 = Movie(
        "TITLE2", "DESCRIPTION2", 31, "TR", 2013, "Turkey", "HORROR2", "ME2"
    )
    my_catalog = Catalog()
    my_catalog.add_movie(my_movie)
    my_catalog.add_movie(my_movie2)

    window = tk.Tk()
    window.title("Movie Ticket Management System")
    window.resizable(False, False)

    frame = tkinter.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tkinter.LabelFrame(frame, text="Searh Movie")
    main_frame.grid(row=0, column=0, padx=25, pady=10)

    # -----------------------Combo Box---------------------------------

    selected_filter = tk.StringVar()
    filter_combobox = ttk.Combobox(main_frame, textvariable=selected_filter)

    filter_combobox['values'] = ["No Filter",
                                 "Title",
                                 "Language",
                                 "Genre",
                                 "Release Date",
                                 "City"]
    filter_combobox.set("No Filter")

    filter_combobox['state'] = 'readonly'

    filter_combobox.grid(row=1, column=2)

    # -----------------------------------------------------------------

    # -----------------------Search Bar---------------------------
    search_bar_label = tkinter.Label(main_frame, text="Search Bar")

    search_bar_entry = tkinter.Entry(main_frame)

    def search_by_filter():
        print("Search pressed!")
        if selected_filter.get() == "Title" and search_bar_entry.get() != "":
            result = my_catalog.search_by_title(search_bar_entry.get())
            if result is not None:
                for i in result:
                    print(i.title)
                    show_result(i.title)
            else:
                show_result("Film is not found!")
        if selected_filter.get() == "Language" and search_bar_entry.get() != "":
            result = my_catalog.search_by_language(search_bar_entry.get())
            if result is not None:
                for i in result:
                    print(i.language)
                    show_result(i.language)
            else:
                show_result("Film is not found!")
        if selected_filter.get() == "Genre" and search_bar_entry.get() != "":
            result = my_catalog.search_by_genre(search_bar_entry.get())
            if result is not None:
                for i in result:
                    print(i.genre)
                    show_result(i.genre)
            else:
                show_result("Film is not found!")
        if selected_filter.get() == "Release Date" and search_bar_entry.get() != "":
            result = my_catalog.search_by_release_date(search_bar_entry.get())
            if result is not None:
                for i in result:
                    print(i.release_date)
                    show_result(i.release_date)
            else:
                show_result("Film is not found!")
        if selected_filter.get() == "City" and search_bar_entry.get() != "":
            result = my_catalog.search_by_city(search_bar_entry.get())
            if result is not None:
                for i in result:
                    print(i.city)
                    show_result(i.city)
            else:
                show_result("Film is not found!")

    # Search Button
    search_button = tkinter.Button(main_frame, text="Search", command=search_by_filter)

    # ---------------------------------------------------------------------------------

    def filter_changed(event):
        show_result(selected_filter.get())

        # Enable search bar and search button after selecting filter
        if selected_filter.get() != "No Filter":
            search_bar_label.grid(row=0, column=1)
            search_bar_entry.grid(row=1, column=1)
            search_button.grid(row=1, column=3)

    filter_combobox.bind('<<ComboboxSelected>>', filter_changed)

    window.mainloop()


if __name__ == '__main__':
    main()
