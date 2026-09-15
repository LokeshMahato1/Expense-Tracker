import tkinter as tk
from tkinter import ttk

class Transaction(tk.Frame):
    def __init__(self, parent,service):
        super().__init__(
            parent, bg="#f4f4f4"
        )
        self.service=service
        self.create_widgets()
        self.load_transactions()


    def create_widgets(self):
        card=tk.Frame(
            self,
            bg="white",
            highlightbackground="#dddddd",
            highlightthickness=1
        )
        card.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        tk.Label(card, text="Recent Transactions", bg="white",
                  fg="#222222", font=("Arial", 18, "bold")).pack(
                      anchor="w", padx=5, pady=5)

        columns = ("Category", "Amount","Description","Method", "TXN ID","Date")
        self.table = ttk.Treeview(card, columns=columns, show="headings")
        self.table.column("Category", width=120, anchor="center")
        self.table.column("Amount", width=110, anchor="center")
        self.table.column("Description", width=150, anchor="center")
        self.table.column("Method", width=100, anchor="center")
        self.table.column("TXN ID", width=150, anchor="center")
        self.table.column("Date", width=140, anchor="center")

        for columns in columns:
            self.table.heading(columns, text=columns, anchor="center")
            self.table.pack(fill="both", expand=True, padx=20, pady=(0,20))

    def load_transactions(self):
        self.table.delete(*self.table.get_children())

        for expense in self.service.get_expenses():
            self.table.insert("", "end", values=(
                expense.category,
                f"Rs.{expense.amount:.2f}",
                expense.description,
                expense.method,
                expense.txn_id or "-",
                expense.date
            ))