from tkinter.messagebox import showinfo


def control_str(text):
    text = str(text)
    for i in text:
        if i.isdigit():
            showinfo("Error", "Invalid Entry")
            return ""
    return text
