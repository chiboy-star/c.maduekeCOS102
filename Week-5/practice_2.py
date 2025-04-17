import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk

def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Admin box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is python GUI with TKinter\n")
    label_2.pack()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")
root.geometry("500x200")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()