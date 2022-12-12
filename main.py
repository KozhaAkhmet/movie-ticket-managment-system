from lib import Constants
from lib import Cinema

from lib import Customer
from lib import Movie
from lib import People
from lib import Catalog

import tkinter
from tkinter import ttk



my_movie = Movie.Movie(
    "TITLE","DESCRIPTION",30,"TR",2012,"TR","HORROR","ME"
)

my_catalog = Catalog()
my_catalog.add_movie(my_movie)

print(my_catalog.search_by_city(my_movie.__country))





#TODO Search Method
def search_by_filter(genre,release_date,language,title,city,date,seat):
    Catalog.search_by_genre(genre=genre)
    Catalog.search_by_release_date(rel_date=release_date)
    Catalog.search_by_language(language=language)
    Catalog.search_by_title(title=title)
    Catalog.search_by_city(city_name=city)
    #Print search output

window = tkinter.Tk()
window.title("Movie Ticket Management System")

frame = tkinter.Frame(window)
frame.pack()

#Main Frame
main_frame = tkinter.LabelFrame(frame, text="Searh Movie")
main_frame.grid(row=0, column=0, padx=25,pady=10)

#------------Search Bar--------------

#Genre filter 
genre_label = tkinter.Label(main_frame, text="Genre")
genre_label.grid(row=0,column=3)

genre_entry = tkinter.Entry(main_frame)
genre_entry.grid(row=1, column=3)
genre_filter_value = genre_entry.get()

#Realese Date filter 
realese_date_label = tkinter.Label(main_frame, text="Realese Date")
realese_date_label.grid(row=0,column=4)

realese_date_entry = tkinter.Entry(main_frame)
realese_date_entry.grid(row=1, column=4)
realese_date_filter_value = realese_date_entry.get()

#Language filter
language_label = tkinter.Label(main_frame, text="Language")
language_label.grid(row=0,column=2)

language_entry = tkinter.Entry(main_frame)
language_entry.grid(row=1, column=2)
language_filter_value = language_entry.get()

#Title filter
title_label = tkinter.Label(main_frame, text="Title")
title_label.grid(row=0,column=1)

title_entry = tkinter.Entry(main_frame)
title_entry.grid(row=1, column=1)
title_filter_value = title_entry.get()

#City filter
city_label = tkinter.Label(main_frame, text="City")
city_label.grid(row=0,column=5)

city_entry = tkinter.Entry(main_frame)
city_entry.grid(row=1, column=5)

#Seat filter
seat_label = tkinter.Label(main_frame, text="Seat")
seat_label.grid(row=0,column=6)

seat_entry = tkinter.Entry(main_frame)
seat_entry.grid(row=1, column=6)
seat_filter_value = seat_entry.get()

#Date filter
date_label = tkinter.Label(main_frame, text="Date")
date_label.grid(row=0,column=7)

date_entry = tkinter.Entry(main_frame)
date_entry.grid(row=1, column=7)
date_filter_value = date_entry.get()

search_button = tkinter.Button(main_frame,text="Search",command=search_by_filter) 
search_button.grid(row=1,column=8,)
#--------------------------------------------

window.mainloop()