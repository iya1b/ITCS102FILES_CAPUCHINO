import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator Application")
window.resizable(True, True)
window.configure(bg="lightpink",cursor="arrow")
window.geometry("300x300")

result = tk.Label(window, text="Please enter the numbers:")
result.grid(row=0,column=0,columnspan=2)

label1 =  tk.Label(window, text="Enter the First number:")
label1.grid(row=1,column=0)

num1 = tk.Entry(window)
num1.grid(row=1, column=1)

label2 = tk.Label(window, text="Enter the Second number:")
label2.grid(row=2, column=0)

num2 = tk.Entry(window)
num2.grid(row=2, column=1)


def add():
    n1 = int(num1.get())
    n2 = int(num2.get())
    result["text"] = "The sum of " + str(n1) + " and " + str(n2) + " is " + str(n1 + n2)

def subtract():
    n1 = int(num1.get())
    n2 = int(num2.get())
    result["text"] = "The difference of " + str(n1) + " and " + str(n2) + " is " + str(n1 - n2)

def multiply():
    n1 = int(num1.get())
    n2 = int(num2.get())
    result["text"] = "The product of " + str(n1) + " and " + str(n2) + " is " + str(n1 * n2)

def divide():
    n1 = int(num1.get())
    n2 = int(num2.get())
    result["text"] = "The product of " + str(n1) + " and " + str(n2) + " is " + str(n1 / n2)

btn_add = tk.Button(window, text="Add", command=add)
btn_add.grid(row=3, column=0)

btn_sub = tk.Button(window, text="Subtract", command=subtract)
btn_sub.grid(row=3,column=1)

btn_mul = tk.Button(window, text="Multiply", command=multiply)
btn_mul.grid(row=4, column=0)

btn_div = tk.Button(window, text="Divide", command=divide)
btn_div.grid(row=4, column=1)

window.mainloop()