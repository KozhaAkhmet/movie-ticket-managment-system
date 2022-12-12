
# YouTube Video link https://www.youtube.com/watch?v=vusUfPBsggw
import tkinter as tk

tk

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

#Header
user_info_frame = tk.LabelFrame(frame, text="User Information") #how our application going to be organized, #first parameter is not windows,frame. 
user_info_frame.grid(row=0, column=0) #cunku pythonda tüm indekslemeler 0dan başlıyor

#Header 2
first_name_label = tk.Label(user_info_frame, text="First Name") #first parameter user_int.. oldu çünkü parent bu oldu.
first_name_label.grid(row=0, column=0) #this is where we placing our label grid
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

#Input Fields
first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

window.mainloop()