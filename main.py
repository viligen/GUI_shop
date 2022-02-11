from tkinter import Tk
from screens import render_main_screen

if __name__ == '__main__':
    window = Tk()
    window.geometry('750x750')
    window.title("My GUI Shop")
    render_main_screen(window)
    window.mainloop()
