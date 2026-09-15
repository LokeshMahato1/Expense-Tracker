import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Models.expense import Expenses
from utils.transaction_id import generate_transaction_id
from utils.validator import validate_amount, validate_expense
from datetime import datetime


class Dashboard(tk.Frame):

    def __init__(self, parent,service):
        super().__init__(
            parent,
            bg="#f4f4f4"
        )
        
        self.create_widgets()
        self.service=service
        self.refreh_transactions=lambda: None  # Placeholder for the refresh function
       

    def create_widgets(self):
        dashboard=tk.Frame(
            self,bg="#f4f4f4"
        )
        dashboard.pack(fill="both", expand=True, padx=30, pady=10)
        dashboard.columnconfigure((0, 1), weight=1)

        #add expense card
        add_card=tk.Frame(
            dashboard,
            bg="white",
            highlightbackground="#dddddd",
            highlightthickness=1
        )
        add_card.grid(row=0, column=0, padx=(0,10), sticky="nsew")


        #spending breakdown 

        spending_card=tk.Frame(
            dashboard,
            bg="white",
            highlightbackground="#dddddd",
            highlightthickness=1

        )

        spending_card.grid(row=0, column=1, padx=(10,0), sticky="nsew")


        #create add expense form

        tk.Label(
            add_card,
            text="Add Expense",
            bg="white",
            font=("Arial",20,"bold")
        ).pack(anchor="w", padx=25, pady=(20,15))

        tk.Label(add_card, text="Amount", bg="white").pack(anchor="w", padx=25)
        self.amount=ttk.Entry(add_card)
        self.amount.pack(fill="x",padx=25,pady=(3,10))

        tk.Label(add_card, text="Category", bg="white").pack(anchor="w", padx=25)
        self.category=ttk.Combobox(
            add_card,
            values=[
                "Food",
                "Entertainment",
                "Travel",
                "Health",
                "Housing",
                "Shopping",
                "Education",
                "Other"

            ], state="readonly"
        )
        self.category.pack(fill="x", padx=25, pady=(3,10))

        tk.Label(add_card, text="Payment Method", bg="white").pack(anchor="w",padx=25)
        self.method=ttk.Combobox(
            add_card,
            values=["Cash", "Online"],
            state="readonly"
        )
        self.method.pack(fill="x",padx=25, pady=(3,10))

        tk.Label(add_card, text="Description", bg="white").pack(anchor="w", padx=25)
        self.description=ttk.Entry(add_card)
        self.description.pack(fill="x",padx=25, pady=(3,15))


        #display total spending

        self.total=tk.Label(
            add_card, text="Total Spent: Rs. 0.00",
            bg="white",
            font=("Arial", 12, "bold")
        )
        self.total.pack(anchor="w", padx=20, pady=10)

        #add expense button
        ttk.Button(
            add_card, text="Add Expense",
            command=self.add_expense
        ).pack(pady=(5,20))

        # Create the spending breakdown chart.
        fig, ax = plt.subplots(figsize=(4, 3))

        categories = ["Food",
                        "Entertainment",
                        "Travel",
                        "Health",
                        "Housing",
                        "Shopping",
                        "Education",
                        "Other"]
        amounts = [300, 200, 150, 100,50,80,150,200]

        ax.pie(amounts, labels=categories, autopct="%1.1f%%")
        ax.set_title("Spending Breakdown")

        canvas = FigureCanvasTkAgg(fig, spending_card)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=20, pady=10)

    def add_expense(self):

        if not validate_amount(self.amount.get()):
            tk.messagebox.showerror("Invalid Amount",
                                     "Please enter a valid positive number for the amount.")
            return

        if not validate_expense(self.category.get(), self.method.get()):
            tk.messagebox.showerror("Missing Fields",
                                     "Please select a category and payment method.")
            return
        

        expense=Expenses(
            category=self.category.get(),
            amount=float(self.amount.get()),
            description=self.description.get(),
            method=self.method.get(),
            txn_id=generate_transaction_id(),
            date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )

        self.service.add_expense(expense)
        self.refresh_transactions()