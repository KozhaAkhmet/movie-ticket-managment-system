import tkinter as tk


movie_instance = 4


class search_result_ui:
    def __init__(self, result_dict, frame, row):

        i = 0

        for movie in result_dict.values():
            self.movie_label = tk.Label(frame, text="Movie")
            self.movie_label.grid(row=row + i, column=0)

            self.movie_text = tk.Text(self.movie_label, height=1, width=154)
            self.movie_text.insert("1.0", str(movie["Title"]) +
                                   " genre: " + str(movie["Genre"]) +
                                   " seats: " + str(movie['Seat']) +
                                   " day: " + str(movie['Date']))
            self.movie_text.config(state='disabled')
            self.movie_text.grid(row=row + i, column=0)

            i = i + 1

    def delete(self):
        self.movie_text.destroy()
        self.movie_label.destroy()

