import tkinter as tk
from tkinter import ttk
from UI.header import Header
from UI.dashboard import Dashboard
from UI.transaction import Transaction
from Services.expense_service import ExpenseService
from PIL import Image, ImageTk 


class ExpenseTrackerApp:
    def __init__(self):
        self.root=tk.Tk()

        self.root.title("Expense Tracker")
        icon=Image.open("Assets/logo.png")
        self.icon=ImageTk.PhotoImage(icon)
        self.root.iconphoto(False, self.icon)
        self.root.geometry("1150x780")

        self.create_ui()

    def create_ui(self):
        self.service=ExpenseService()

        self.header=Header(self.root)
        self.header.pack(fill="x")

        self.dashboard=Dashboard(self.root,self.service)
        self.dashboard.pack(fill="both", expand=True)

        self.transactions=Transaction(self.root,self.service)
        self.transactions.pack(fill="both", expand=True)

        self.dashboard.refresh_transactions=self.transactions.load_transactions

    def run(self):
        self.root.mainloop()
