import tkinter as tk


def user_login():
    padx = 13
    width = 18
    window = tk.Tk()
    window.title("User Login")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="User Login")
    main_frame.grid(row=0, column=0, padx=25, pady=10)
    # Genre filter
    name_label = tk.Label(main_frame, text="Name")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(main_frame)
    name_entry.grid(row=1, column=0,padx= padx)

    pwd_label = tk.Label(main_frame, text="Password")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame)
    pwd_entry.grid(row=3, column=0,padx= padx)
    genre_filter_value = pwd_entry.get()

    login_button = tk.Button(main_frame, text="Login", )
    login_button.grid(row=4, column=0)
    window.mainloop()

    window.mainloop()
