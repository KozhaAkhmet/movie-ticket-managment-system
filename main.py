import tkinter as tk
from tkinter.messagebox import showinfo

from lib import Catalog
from lib.FakeData import show_list,movie_catalog


def show_result(txt: str):
    showinfo(
        message=f'Result {txt}!'
    )


movie_instance = 4


class movie_ui:
    def __init__(self, result_dict, frame):
        try:
            if movie_instance is not None:
                movie_instance.delete()
        except AttributeError:
            print("movie instance not deleted")
            pass
        i = 0
        row = 1
        for movie in result_dict.values():
            self.movie_label = tk.Label(frame, text="Movie")
            self.movie_label.grid(row=row + i, column=0)

            self.movie_text = tk.Text(self.movie_label, height=1, width=154)
            self.movie_text.insert("1.0", str(movie["Title"]) + " genre: " + str(movie["Genre"]) + " seats: " + str(movie['Seat']))
            self.movie_text.config(state='disabled')
            self.movie_text.grid(row=row + i, column=0)

            i = i + 1

    def delete(self):
        self.movie_text.destroy()
        self.movie_label.destroy()


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
    main_frame = tk.LabelFrame(frame, text="Search Movie")
    main_frame.grid(row=0, column=0, padx=25, pady=10)
    # Genre filter
    genre_label = tk.Label(main_frame, text="Genre")
    genre_label.grid(row=0, column=3)

    genre_entry = tk.Entry(main_frame)
    genre_entry.grid(row=1, column=3)

    # Release Date filter
    release_date_label = tk.Label(main_frame, text="Release Date")
    release_date_label.grid(row=0, column=4)

    release_date_entry = tk.Entry(main_frame)
    release_date_entry.grid(row=1, column=4)

    # Language filter
    language_label = tk.Label(main_frame, text="Language")
    language_label.grid(row=0, column=2)

    language_entry = tk.Entry(main_frame)
    language_entry.grid(row=1, column=2)

    # Title filter
    title_label = tk.Label(main_frame, text="Title")
    title_label.grid(row=0, column=1)

    title_entry = tk.Entry(main_frame)
    title_entry.grid(row=1, column=1)

    # City filter
    city_label = tk.Label(main_frame, text="City")
    city_label.grid(row=0, column=5)

    city_entry = tk.Entry(main_frame)
    city_entry.grid(row=1, column=5)

    # Seat filter
    seat_label = tk.Label(main_frame, text="Seat")
    seat_label.grid(row=0, column=6)

    seat_entry = tk.Entry(main_frame)
    seat_entry.grid(row=1, column=6)

    # Date filter
    date_label = tk.Label(main_frame, text="Date")
    date_label.grid(row=0, column=7)

    date_entry = tk.Entry(main_frame)
    date_entry.grid(row=1, column=7)

    # --------------------------------------------

    def search_by_filter():
        global movie_instance
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
        movie_instance = movie_ui(result_dict, frame)

    # Search Button
    search_button = tk.Button(main_frame, text="Search", command=search_by_filter)
    search_button.grid(row=1, column=8)
    window.mainloop()


if __name__ == '__main__':
    main()
