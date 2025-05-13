import tkinter as tk
from tkinter import messagebox
import random

class Employee:
    def __init__(self, master):
        self.master = master
        master.title("Employee Attendance System")
        master.geometry("400x300")
        master.resizable(False, False)

      
        self.list_of_employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
                                  "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo",
                                  "Abraham Jones", "Nicole Anide", "Kosi Korso", "Adele Martins",
                                  "Emmanuel Ojo", "Ajayi Fatima"]
        self.tasklist = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]
        self.count = 0
        self.attendance_count = 0

       
        self.label = tk.Label(master, text="Enter your name:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_employee, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=("Arial", 11), fg="green")
        self.message_label.pack(pady=5)

        self.sign_button = tk.Button(master, text="Sign Attendance", command=self.take_attendance, font=("Arial", 12))
        self.sign_button.pack(pady=10)
        self.sign_button.config(state="disabled")

        self.task_label = tk.Label(master, text="", font=("Arial", 11), fg="blue")
        self.task_label.pack(pady=5)

        self.next_button = tk.Button(master, text="Next Employee", command=self.refuse_access, font=("Arial", 10))
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")

    def check_employee(self):
        name = self.entry.get().strip()
        if name in self.list_of_employees:
            self.message_label.config(text=f"Welcome {name}! You're logged in.")
            self.sign_button.config(state="normal")
            self.entry.config(state="disabled")
            self.submit_button.config(state="disabled")
        else:
            self.count += 1
            attempts_left = 10 - self.count
            self.message_label.config(text=f"Name not found. {attempts_left} attempts left.", fg="red")
            if self.count == 10:
                messagebox.showerror("Access Denied", "Too many failed attempts. Contact Admin.")
                self.master.destroy()

    def take_attendance(self):
        self.attendance_count += 1
        self.message_label.config(text="Attendance signed successfully!")
        task = random.choice(self.tasklist)
        self.task_label.config(text=f"Your task is: {task}")
        self.sign_button.config(state="disabled")
        self.next_button.config(state="normal")

    def refuse_access(self):
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.message_label.config(text="", fg="green")
        self.task_label.config(text="")
        self.submit_button.config(state="normal")
        self.sign_button.config(state="disabled")
        self.next_button.config(state="disabled")


root = tk.Tk()
app = Employee(root)
root.mainloop()
