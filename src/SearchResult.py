import tkinter as tk
from lib.People import Customer, Guest

show_instance = 4


class search_result_ui:
    def __init__(self, result_dict, frame, row, user):
        # self.show_scroll = tk.Scrollbar(frame)
        # self.show_scroll.grid(row=row, column=0)
        i = 0
        self.__tmp_user = user
        for show in result_dict.values():
            #self.show_image = tk.PhotoImage(file="Data/Voando-Harry-Potter-PNG-2245377973.png")
            self.show_label = tk.Label(frame, text="show")
            self.show_label.grid(row=row + i, column=0)


            self.show_text = tk.Text(self.show_label, height=1, width=145)
            self.show_text.insert("1.0", str(show["Title"]) +
                                  " genre: " + str(show["Genre"]) +
                                  " seats: " + str(show['Seat']) +
                                  " day: " + str(show['Date']))
            self.show_text.config(state='disabled')
            self.show_text.grid(row=row + i, column=0)

            self.show_button = tk.Button(self.show_label, text="To Show", command=self.to_show)
            self.show_button.grid(row=row + i, column=1)

            i = i + 1


    def to_show(self):
        if type(self.__tmp_user) == Customer:
            self.window = tk.Toplevel()
            self.window.title("Show Info")
            self.window.resizable(False, False)

            self.frame = tk.Frame(self.window)
            self.frame.pack()

            self.payment_button = tk.Button(self.frame, text="Make Payment")
            self.payment_button.pack()

        elif type(self.__tmp_user) == Guest:

            pass


    def delete(self):
        self.show_text.destroy()
        self.show_label.destroy()
        # self.show_scroll.destroy()
