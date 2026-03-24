import tkinter as tk
from tkinter import messagebox

stored_username = ""
stored_password = ""

# MAIN WINDOW
def main_window():
    window = tk.Tk()
    window.title("CAPUCHINO HO Exam")
    window.geometry("300x200")

    label = tk.Label(window, text="Welcome!", font=("Arial", 16))
    label.pack(pady=10)

    register_btn = tk.Button(window, text="Register", bg="blue", fg="black",
                             width=20, height=2, command=register_window)
    register_btn.pack(pady=5)

    login_btn = tk.Button(window, text="Log In", bg="green", fg="black",
                          width=20, height=2, command=login_window)
    login_btn.pack(pady=5)

    window.mainloop()

# REGISTER WINDOW
def register_window():
    reg = tk.Toplevel()
    reg.title("Register")
    reg.geometry("300x250")
    reg.configure(bg="green")

    tk.Label(reg, text="Register", bg="green", font=("Arial", 14)).pack(pady=5)

    tk.Label(reg, text="Username:", bg="green").pack()
    username_entry = tk.Entry(reg)
    username_entry.pack()

    tk.Label(reg, text="Password:", bg="green").pack()
    password_entry = tk.Entry(reg, show="*")
    password_entry.pack()

    # Show password toggle
    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    show_var = tk.BooleanVar()
    show_check = tk.Checkbutton(reg, text="See Password", variable=show_var,
                                command=toggle_password, bg="green")
    show_check.pack()

    # Register function
    def register_user():
        global stored_username, stored_password

        username = username_entry.get()
        password = password_entry.get()

        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters!")
        else:
            stored_username = username
            stored_password = password
            messagebox.showinfo("Success", "You have successfully registered!")
            reg.destroy()

    tk.Button(reg, text="Register", command=register_user).pack(pady=10)

# LOGIN WINDOW
def login_window():
    log = tk.Toplevel()
    log.title("Log In")
    log.geometry("300x250")
    log.configure(bg="red")

    tk.Label(log, text="Log In", bg="red", font=("Arial", 14)).pack(pady=5)

    tk.Label(log, text="Username:", bg="red").pack()
    username_entry = tk.Entry(log)
    username_entry.pack()

    tk.Label(log, text="Password:", bg="red").pack()
    password_entry = tk.Entry(log, show="*")
    password_entry.pack()

    # Show password toggle
    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    show_var = tk.BooleanVar()
    show_check = tk.Checkbutton(log, text="See Password", variable=show_var,
                                command=toggle_password, bg="red")
    show_check.pack()

    # Login function
    def login_user():
        username = username_entry.get()
        password = password_entry.get()

        if username == stored_username and password == stored_password:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Your user credentials are incorrect!")

    tk.Button(log, text="Log In", bg="green", command=login_user).pack(pady=10)


main_window()
