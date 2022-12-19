import tkinter as tk


def payment_ui():
    window = tk.Tk()
    window.title("Payment")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    # Main Frame
    main_frame = tk.LabelFrame(frame, text="Payment")
    main_frame.grid(row=0, column=0, padx=25, pady=10)
    # Genre filter
    name_label = tk.Label(main_frame, text="Card Number")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(main_frame)
    name_entry.grid(row=1, column=0)

    pwd_label = tk.Label(main_frame, text="Card Name")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame)
    pwd_entry.grid(row=3, column=0)
    genre_filter_value = pwd_entry.get()

    pwd_label = tk.Label(main_frame, text="Card Name")
    pwd_label.grid(row=2, column=0)

    pwd_entry = tk.Entry(main_frame)
    pwd_entry.grid(row=3, column=0)
    genre_filter_value = pwd_entry.get()

    login_button = tk.Button(main_frame, text="Login", )
    login_button.grid(row=4, column=0)
    window.mainloop()

    window.mainloop()
