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

        self.service=service
        self.refreh_transactions=lambda: None  # Placeholder for the refresh function
        
        self.create_widgets()
        self.update_total()  # Update the total spent label when the dashboard is initialized
       
       

    def create_widgets(self):
        dashboard=tk.Frame(
            self,bg="#f4f4f4"
        )
        dashboard.pack(fill="both", expand=True, padx=30, pady=10)
        dashboard.columnconfigure((0, 1), weight=1)
        dashboard.rowconfigure(0, weight=1)

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
        self.total.pack(anchor="w", padx=25, pady=10)

        #add expense button
        ttk.Button(
            add_card, text="Add Expense",
            command=self.add_expense
        ).pack(pady=(5,20))

        # Create the spending breakdown chart.
        self.fig, self.ax=plt.subplots(figsize=(4, 3))

        totals=self.get_category_total()
        categories=list(totals.keys())
        amounts=list(totals.values())

        self.ax.pie(amounts, labels=categories, autopct="%1.1f%%")
        self.ax.set_title("Spending Breakdown")

        self.canvas=FigureCanvasTkAgg(self.fig, master=spending_card)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=20, pady=10)

    def get_category_total(self):
        totals={}

        for expense in self.service.get_expenses():
            totals[expense.category]=totals.get(expense.category,0)+expense.amount

        return totals

    def update_total(self):
        total=self.service.get_total()
        self.total.config(text=f"Total Spent: Rs. {total:.2f}")


    def update_chart(self):
        self.ax.clear()

        totals=self.get_category_total()

        if totals:
            self.ax.pie(
                totals.values(),
                labels=totals.keys(),
                autopct="%1.1f%%"
            )
        else:
            self.ax.text(0.5, 0.5, "No Data", ha="center", va="center")

        self.ax.set_title("Spending Breakdown")
        self.canvas.draw()

    def clear_form(self):
    # Clear all expense input fields.
        self.amount.delete(0, tk.END)
        self.category.set("")
        self.method.set("")
        self.description.delete(0, tk.END)

    def add_expense(self):

        if not validate_amount(self.amount.get()):
            tk.messagebox.showerror("Invalid Amount",
                                     "Please enter a valid positive number for the amount.")
            return

        if not validate_expense(self.category.get(), self.method.get()):
            tk.messagebox.showerror("Missing Fields",
                                     "Please select a category and payment method.")
            return

        transaction_id=generate_transaction_id() if self.method.get()=="Online" else "_"

        expense=Expenses(
            category=self.category.get(),
            amount=float(self.amount.get()),
            description=self.description.get(),
            method=self.method.get(),
            txn_id=transaction_id,
            date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )

        self.service.add_expense(expense)
        self.update_total()
        self.update_chart()
        self.refresh_transactions()
        self.clear_form()