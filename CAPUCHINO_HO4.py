import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.resizable(True, True)
window.configure(bg="gray", cursor="arrow")
window.geometry("500x500")

def create_id():
    fname = entry_fname.get()
    mname = entry_mname.get()
    lname = entry_lname.get()
    byear = entry_byear.get()
    gender = gender_val.get()

    current_year = 2026
    age = current_year - int(byear)

    full_name = fname + " " + mname + " " + lname

    id_window = tk.Toplevel(window)
    id_window.title("Student ID")
    id_window.geometry("300x200")
    id_window.configure(bg="Pink")

    title = tk.Label(id_window, text="Student ID")
    title.pack(pady=10)

    name_label = tk.Label(id_window, text=)





window.mainloop()
