import tkinter as tk
import src.UserLogin as UserLogin


def to_user_login():
    UserLogin.user_login()


def user_sign_in():
    padx = 13
    width = 18
    window = tk.Tk()
    window.title("User Sign In")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="User Sign In")
    main_frame.grid(row=0, column=0)
    # Genre filter
    name_label = tk.Label(main_frame, text="Name")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(main_frame,width=width)
    name_entry.grid(row=1, column=0, padx=padx)
    # enry value add

    pwd_label = tk.Label(main_frame, text="Password")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame,width=width)
    pwd_entry.grid(row=3, column=0, padx= padx)
    genre_filter_value = pwd_entry.get()

    pwd_retry_label = tk.Label(main_frame, text="Password Retry")
    pwd_retry_label.grid(row=4, column=0, padx= padx)

    pwd_retry_entry = tk.Entry(main_frame,width=width)
    pwd_retry_entry.grid(row=5, column=0, padx= padx)
    genre_filter_value = pwd_entry.get()

    login_button = tk.Button(main_frame, text="Sign In", command=to_user_login)
    login_button.grid(row=6, column=0, padx= padx)

    window.mainloop()

