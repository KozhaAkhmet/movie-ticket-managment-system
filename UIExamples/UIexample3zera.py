import tkinter as tk
from tkinter import ttk

root =tk.Tk()
root.title("Data Entry Form")

frame= tk.Frame(root)
frame.pack()


#Header
user_info_frame=tk.LabelFrame(frame,text=" User Information",)
user_info_frame.grid(row= 0, column=0)

#Header2
user_firstname_label=tk.Label(user_info_frame, text= "First Name", )
user_firstname_label.grid(row=0,column=0)
user_lastname_label=tk.Label(user_info_frame, text= "Last Name")
user_lastname_label.grid(row=0,column=1)


#Input Fields

first_name_entry= tk.Entry(user_info_frame)
first_name_entry.grid(row=1 , column=0 )
last_name_entry= tk.Entry(user_info_frame)
last_name_entry.grid(row= 1, column= 1)

#Combobox

title_label= tk. Label(user_info_frame, text= "Gender" )
title_label.grid(row=0, column=2)
title_combobox= ttk.Combobox(user_info_frame, values= ["Mr", "Mrs", "Non-binary", "I dont want to specify"])
title_combobox.grid(row=1, column=2)

#Spinbox

age_label= tk.Label(user_info_frame, text="Age")
age_label.grid(row=0, column=3)
age_spinbox= tk.Spinbox(user_info_frame, from_=0 , to=120)
age_spinbox.grid(row=1,column=3)

#mail
mail_label=tk.Label(user_info_frame, text="E mail")
mail_label.grid(row=0 , column=4 )
mail_entry= tk.Entry(user_info_frame, text="E mail")
mail_entry.grid(row=1 , column=4 )


for widget in user_info_frame.winfo_children():

    widget.grid_configure(padx= 10, pady=5)

#Second Label Frame

course_frame=tk.LabelFrame(frame)
course_frame.grid(row=1, column=0,sticky="news", padx=10, pady=10)

#Check Button 
registered_label=tk.Label(course_frame,text= "Registiration Status")
registered_label.grid(row=0,column=0)
registered_check=tk.Checkbutton(course_frame,text= "Currently Registered")
registered_check.grid(row=1, column=0)
















root.mainloop()

