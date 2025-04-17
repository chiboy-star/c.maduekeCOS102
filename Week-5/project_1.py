import tkinter as tk
from tkinter import messagebox
import csv

# Load data from CSV into a list of dictionaries
def load_users_from_csv(filename="students.csv"):
    users = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Verification popup with employee list
def verfication(username):
    window = tk.Toplevel(root)
    window.title("Admin box")
    window.geometry("500x400")

    # Welcome message
    label_1 = tk.Label(window, text=f"Welcome, {username}!")
    label_1.pack(pady=10)

    label_2 = tk.Label(window, text="GIG logistics employee list:")
    label_2.pack()

    # Scrollable list of employees
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=50)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=listbox.yview)

    # Load and display all employees
    users = load_users_from_csv()
    for user in users:
        listbox.insert(tk.END, f"{user['Name']} - {user['Department']}")

# Submit button handler
def submit():
    username = username_entry.get().strip()
    department = department_entry.get().strip()

    users = load_users_from_csv()

    for user in users:
        if user["Name"] == username and user["Department"] == department:
            verfication(username)
            return

    messagebox.showerror("Error", "This user does not exist")

# GUI setup
root = tk.Tk()
root.title("Verification Page")
root.geometry("500x200")

username_label = tk.Label(root, text="Employee name:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Department:")
password_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()
