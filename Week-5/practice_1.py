import tkinter as tk
from tkinter import messagebox as msgbox

def button_click():
    #print("Button clicked!")

    msgbox.showinfo("Info","Welcome to COS102 GUI App!\n")

    result = msgbox.askyesno("Confirmation", "Do you want to continue?")

root = tk.Tk()
root.title("Home page")
root.geometry("300x100")

label = tk.Label(root, text="Hello Friend \n!")
label.pack()

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

button.config(fg="red",bg="yellow")

root.mainloop()