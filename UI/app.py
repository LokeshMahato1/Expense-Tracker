import tkinter as tk
from tkinter import ttk
from UI.header import Header
from UI.dashboard import Dashboard
from UI.transaction import Transaction
from Services.expense_service import ExpenseService


class ExpenseTrackerApp:
    def __init__(self):
        self.root=tk.Tk()

        self.root.title("Expense Tracker")
        self.root.geometry("1150x780")

        self.create_ui()

    def create_ui(self):
        self.service=ExpenseService()
        
        self.header=Header(self.root)
        self.header.pack(fill="x")

        self.dashboard=Dashboard(self.root)
        self.dashboard.pack(fill="both", expand=True)

        self.transactions=Transaction(self.root)
        self.transactions.pack(fill="both", expand=True)

        self.dashboard.refresh_transactions=self.transactions.load_transactions

    def run(self):
        self.root.mainloop()
