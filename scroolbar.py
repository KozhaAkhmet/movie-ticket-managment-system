
import tkinter as tk
from tkinter import *

root= tk.Tk()
root.title("movie management system")
root.geometry("400x600")

#Create Frame and scrollbar


my_Frame= Frame(root)
my_scrollbar= Scrollbar(my_Frame,orient=VERTICAL)



my_list_box=Listbox(my_Frame,width=50,yscrollcommand=my_scrollbar)

my_scrollbar.config(command= my_list_box.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_Frame.pack()


my_list_box.pack(pady=15)


root.mainloop()



