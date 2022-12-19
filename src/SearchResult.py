import tkinter as tk

show_instance = 4


class search_result_ui:
    def __init__(self, result_dict, frame, row):
        # self.show_scroll = tk.Scrollbar(frame)
        # self.show_scroll.grid(row=row, column=0)
        i = 0

        for show in result_dict.values():
            self.show_label = tk.Label(frame, text="show")
            self.show_label.grid(row=row + i, column=0)

            self.show_text = tk.Text(self.show_label, height=1, width=154)
            self.show_text.insert("1.0", str(show["Title"]) +
                                  " genre: " + str(show["Genre"]) +
                                  " seats: " + str(show['Seat']) +
                                  " day: " + str(show['Date']))
            self.show_text.config(state='disabled')
            self.show_text.grid(row=row + i, column=0)

            i = i + 1

    def delete(self):
        self.show_text.destroy()
        self.show_label.destroy()
        # self.show_scroll.destroy()
