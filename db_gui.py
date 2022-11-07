import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk()  # root is the standard name for the root window
    root.title('Blood Donor Database')
    root.geometry('600x300')  # Set the default size of the window. You
    # provide a
    # str of width and height for the
    # window you want to it to be

    ttk.Label(root, text='Blood Donor Database').grid(column=0, row=0)  # As
    # long as there's any content, tkinter will shrink the window to the
    # child widget. grid(column=0, row=0) will go the upper left corner
    ttk.Label(root, text='Name:').grid(column=0, row=1)  # column and row
    # needs to be in sequence so using grid(column=0, row=2) will give you
    # the same thing since there's now row 1 yet
    ttk.Entry(root, width=50).grid(column=1, row=1)

    root.mainloop()  # Start the interface. It's a loop because you're waiting
    # for the user to make some events and then to react correspondngly


if __name__ == '__main__':
    main_window()
