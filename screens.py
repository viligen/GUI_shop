import tkinter as tk


def render_main_screen(window):
    tk.Button(window, text='Login', bg='light green', fg='white',
              command=lambda: print('login button check')).grid(row=0, column=0)
    tk.Button(window, text='Register', bg='light yellow', fg='black',
              command=lambda: render_register_screen(window)).grid(row=0, column=1)


def clear_screen(window):
    [child.destroy() for child in window.winfo_children()]


def render_register_screen(window):
    clear_screen(window)

    tk.Label(window, text='Please enter your username: ').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Please enter your email: ').grid(row=1, column=0)
    email = tk.Entry(window)
    email.grid(row=1, column=1)

    tk.Label(window, text='Please enter your password: ').grid(row=2, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=2, column=1)

    tk.Label(window, text='Please confirm your password: ').grid(row=3, column=0)
    confirmed_password = tk.Entry(window, show='*')
    confirmed_password.grid(row=3, column=1)

    def on_register_click():
        username_value = username.get()
        email_value = email.get()
        password_value = password.get()
        confirmed_password_value = confirmed_password.get()
        if password_value != confirmed_password_value:
            tk.Label(window, text='Passwords must match!', fg='red').grid(row=4, column=1)
        else:
            pass

    tk.Button(window, text='Register', bg='dark green', fg='white',
              command=on_register_click).grid(row=5, column=1)


