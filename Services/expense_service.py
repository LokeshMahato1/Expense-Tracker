from Storage.csv_manager import CSVManager

class ExpenseService:

    def __init__(self):
        self.csv_manager=CSVManager()
        self.expenses=self.csv_manager.load()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.csv_manager.save(self.expenses)

    def get_expenses(self):
        return self.expenses

    def get_total(self):
        return sum(
            expense.amount for expense in self.expenses
        )
