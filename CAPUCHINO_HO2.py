
import tkinter as tk

window = tk.Tk()

window.title("Iya's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="pink",cursor="hand2")


label = tk.Label(window,text="STUDENT PROFILE",font=("Poppins",35),fg="white",bg="purple")
label.pack()

label = tk.Label(window,text="Name: Capuchino, Maria Sofia Kristelyn M. ",font=("Poppins",10),fg="white",bg="red")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Age: 18 yrs old",font=("Poppins",10),fg="white",bg="red")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Course % Section: BSIT - 1B ",font=("Poppins",10),fg="white",bg="red")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Birthday: April 2, 2007 ",font=("Poppins",10),fg="white",bg="red")
label.pack(anchor="w", pady=10)

label = tk.Label(window,text="Personal Motto: Ajinomotto ",font=("Poppins",10),fg="white",bg="red")
label.pack(anchor="w", pady=10)

window.mainloop()


