import tkinter as tk
from tkinter import messagebox

class Delivery_servic:
    def __init__(self,master):
        self.master = master
        master.title("Delivery Service")
        master.geometry("400x300")
        master.resizable(False, False)

        self.label_1 = tk.Label(master, text="Where do you want to deliver this product to?: ", font=("Arial", 12))
        self.label_1.pack(pady=10)

        self.entry1 = tk.Entry(master, font=("Arial", 12))
        self.entry1.pack(pady=5)

        self.label_2 = tk.Label(master, text="What is the mass of this product?: ", font=("Arial", 12))
        self.label_2.pack(pady=10)

        self.entry2 = tk.Entry(master, font=("Arial", 12))
        self.entry2.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_cost, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(master, text="", font=("Arial", 11), fg="green")
        self.message_label.pack(pady=5)

    def check_cost(self):
        location = self.entry1.get().strip()
        mass = float(self.entry2.get().strip())
        if location == "PAU":
            if mass >= 10:
                self.message_label.config(text="This is going to cost you N2000", fg="green")
            else:
                self.message_label.config(text="This is going to cost you N1500", fg="green")
        elif location == "Epe":
            if mass >= 10:
                self.message_label.config(text="This is going to cost you N5000", fg="green")
            else:
                self.message_label.config(text="This is going to cost you N4000", fg="green")
            
    
root = tk.Tk()
app = Delivery_servic(root)
root.mainloop()