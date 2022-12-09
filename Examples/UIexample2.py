# YouTube Video link https://www.youtube.com/watch?v=vusUfPBsggw
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Header
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0)

#Header 2
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

#Input Fields
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text= "Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.","Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)



window.mainloop()