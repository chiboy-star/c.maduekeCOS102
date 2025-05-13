import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk  # This is unused currently, can be removed if not needed

def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("400x150")
    window.resizable(False, False)

    label_1 = tk.Label(window, text=f"Welcome {username}!", font=("Arial", 14))
    label_1.pack(pady=10)

    label_2 = tk.Label(window, text="This is a Python GUI built with Tkinter.", font=("Arial", 10))
    label_2.pack()

def submit():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Username:", font=("Arial", 12)).pack(pady=(20, 5))
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack()

tk.Label(root, text="Password:", font=("Arial", 12)).pack(pady=(10, 5))
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit, font=("Arial", 12), bg="lightblue")
submit_button.pack(pady=20)

root.mainloop()
