import tkinter as tk
from lib.People import Account, Customer
from lib.Constants import AccountStatus

from Data.FakeAccounts import user_list

__padx = 13
__width = 18


def __cancel_command():
    return "Canceled"


def user_login():
    window = tk.Tk()
    window.title("User Login")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="User Login")
    main_frame.grid(row=0, column=0, padx=15, pady=10)

    # Name
    name_label = tk.Label(main_frame, text="Name")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(main_frame)
    name_entry.grid(row=1, column=0, padx=__padx)

    # Password
    pwd_label = tk.Label(main_frame, text="Password")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame)
    pwd_entry.grid(row=3, column=0, padx=__padx)

    # ---------Buttons
    def login_command():
        tmp_account = Account(name_entry.get(),
                              pwd_entry.get(),
                              AccountStatus.ACTIVE)
        print(name_entry.get() + " pwd " + pwd_entry.get())

        for tmp_user in user_list:
            if tmp_account == tmp_user.get_account():
                print("found")
            else:
                print(tmp_user.get_account().get_user_id())

                print("Not found")

        return

    button_label = tk.Label(main_frame)
    button_label.grid(row=4, column=0)

    # Login Button
    login_button = tk.Button(button_label, text="Login", command=login_command)
    login_button.grid(row=4, column=1, padx=20, pady=5)

    # Cancel Button
    cancel_button = tk.Button(button_label, text="Cancel", command=__cancel_command)
    cancel_button.grid(row=4, column=0, padx=20, pady=5)

    # ----------------

    window.mainloop()


def user_sign_in():
    window = tk.Tk()
    window.title("User Sign In")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="User Sign In")
    main_frame.grid(row=0, column=0, padx=15, pady=10)

    # Name
    name_label = tk.Label(main_frame, text="Nickname")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(main_frame, width=__width)
    name_entry.grid(row=1, column=0, padx=__padx)

    # Password
    pwd_label = tk.Label(main_frame, text="Password")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame, width=__width)
    pwd_entry.grid(row=3, column=0, padx=__padx)

    # Password Retry
    pwd_retry_label = tk.Label(main_frame, text="Password Retry")
    pwd_retry_label.grid(row=4, column=0, padx=__padx)

    pwd_retry_entry = tk.Entry(main_frame, width=__width)
    pwd_retry_entry.grid(row=5, column=0, padx=__padx)

    # ---------Buttons
    def sign_in_command():
        Account(name_entry.get(),
                pwd_entry.get(),
                AccountStatus.ACTIVE)

        return

    button_label = tk.Label(main_frame)
    button_label.grid(row=6, column=0)

    # Login Button
    sign_in_button = tk.Button(button_label, text="Sign In", )
    sign_in_button.grid(row=0, column=1, padx=20, pady=5)

    # Cancel Button
    cancel_button = tk.Button(button_label, text="Cancel", command=__cancel_command)
    cancel_button.grid(row=0, column=0, padx=20, pady=5)

    # ----------------

    window.mainloop()
